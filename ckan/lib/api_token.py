# -*- coding: utf-8 -*-

from ckan.types import Schema
import jwt
import logging

from calendar import timegm

import ckan.plugins as plugins
import ckan.model as model
from ckan.common import config
from ckan.logic.schema import default_create_api_token_schema
from ckan.exceptions import CkanConfigurationException
from datetime import datetime
from typing import Any, Dict, Iterable, Optional

log = logging.getLogger(__name__)

_config_encode_secret = u"api_token.jwt.encode.secret"
_config_decode_secret = u"api_token.jwt.decode.secret"
_config_secret_fallback = u"beaker.session.secret"

_config_algorithm = u"api_token.jwt.algorithm"


def _get_plugins() -> Iterable[plugins.IApiToken]:
    return plugins.PluginImplementations(plugins.IApiToken)


def _get_algorithm() -> str:
    return config.get(_config_algorithm, u"HS256")


def _get_secret(encode: bool) -> bytes:
    config_key = _config_encode_secret if encode else _config_decode_secret
    secret: str = config.get(config_key, '')
    if not secret:
        secret = u"string:" + config.get(_config_secret_fallback, u"")
    type_, string = secret.split(u":", 1)
    if type_ == u"file":
        with open(string, u"rb") as key_file:
            value = key_file.read()
    else:
        value = bytes(string, u'utf8')
    if not value:
        raise CkanConfigurationException(
            (
                u"Neither `{key}` nor `{fallback}` specified. "
                u"Missing secret key is a critical security issue."
            ).format(
                key=config_key, fallback=_config_secret_fallback,
            )
        )
    return value


def into_seconds(dt: datetime) -> int:
    return timegm(dt.timetuple())


def get_schema() -> Schema:
    schema = default_create_api_token_schema()
    for plugin in _get_plugins():
        schema = plugin.create_api_token_schema(schema)
    return schema


def postprocess(data: Dict[str, Any], jti: str,
                data_dict: Dict[str, Any]) -> Dict[str, Any]:
    for plugin in _get_plugins():
        data = plugin.postprocess_api_token(data, jti, data_dict)
    return data


def decode(encoded: str, **kwargs: Any) -> Optional[Dict[str, Any]]:
    for plugin in _get_plugins():
        data = plugin.decode_api_token(encoded, **kwargs)
        if data:
            break
    else:
        try:
            data = jwt.decode(
                encoded,
                _get_secret(encode=False),
                algorithms=_get_algorithm(),
                **kwargs
            )
        except jwt.InvalidTokenError as e:
            # TODO: add signal for performing extra work, like removing
            # expired tokens
            log.error(u"Cannot decode JWT token: %s", e)
            data = None
    return data


def encode(data: Dict[str, Any], **kwargs: Any) -> bytes:
    for plugin in _get_plugins():
        token = plugin.encode_api_token(data, **kwargs)
        if token:
            break
    else:
        token = jwt.encode(
            data,
            _get_secret(encode=True),
            algorithm=_get_algorithm(),
            **kwargs
        )

    return token


def add_extra(result: Dict[str, Any]) -> Dict[str, Any]:
    for plugin in _get_plugins():
        result = plugin.add_extra_fields(result)
    return result


def get_user_from_token(token: str,
                        update_access_time: bool = True
                        ) -> Optional[model.User]:
    data = decode(token)
    if not data:
        return None
    # do preprocessing in reverse order, allowing onion-like
    # "unwrapping" of the data, added during postprocessing, when
    # token was created
    for plugin in reversed(list(_get_plugins())):
        data = plugin.preprocess_api_token(data)
    if not data or u"jti" not in data:
        return None
    token_obj = model.ApiToken.get(data[u"jti"])
    if not token_obj:
        return None
    if update_access_time:
        token_obj.touch(True)
    return token_obj.owner
