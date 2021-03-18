from typing import Dict, Optional, Union
from flask import Blueprint
from flask.views import MethodView
from flask.wrappers import Response

new_user_form: str
edit_user_form: str

user: Blueprint

def set_repoze_user(user_id: str, resp: Response) -> None: ...
@user.before_request
def before_request() -> None: ...
def index() -> str: ...
def me() -> Response: ...
def read(id: str) -> Union[Response, str]: ...

class ApiTokenView(MethodView):
    def get(
        self,
        id: str,
        data: Optional[Dict] = ...,
        errors: Optional[Dict] = ...,
        error_summary: Optional[Dict] = ...,
    ) -> Union[Response, str]: ...
    def post(self, id: str) -> Union[Response, str]: ...

def api_token_revoke(id, jti: str) -> Response: ...

class EditView(MethodView):
    def post(self, id: Optional[str] = ...) -> Union[Response, str]: ...
    def get(
        self,
        id: Optional[str] = ...,
        data: Optional[Dict] = ...,
        errors: Optional[Dict] = ...,
        error_summary: Optional[Dict] = ...,
    ) -> str: ...

class RegisterView(MethodView):
    def post(self) -> Union[Response, str]: ...
    def get(
        self,
        data: Optional[Dict] = ...,
        errors: Optional[Dict] = ...,
        error_summary: Optional[Dict] = ...,
    ) -> str: ...

def login() -> Union[Response, str]: ...
def logged_in() -> Union[Response, str]: ...
def logout() -> Response: ...
def logged_out() -> Response: ...
def logged_out_page() -> str: ...
def delete(id: str) -> Response: ...
def generate_apikey(id: Optional[str] = ...) -> Response: ...
def activity(id: str, offset: int = ...) -> str: ...

class RequestResetView(MethodView):
    def post(self) -> Response: ...
    def get(self) -> str: ...

class PerformResetView(MethodView):
    def post(self, id: str) -> Union[Response, str]: ...
    def get(self, id: str) -> str: ...

def follow(id: str) -> Response: ...
def unfollow(id: str) -> Response: ...
def followers(id: str) -> str: ...
def sysadmin() -> Response: ...