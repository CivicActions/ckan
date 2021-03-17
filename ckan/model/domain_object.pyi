from typing import Any, Dict, Generic, List, Set, Tuple, Type, TypeVar

from sqlalchemy.orm.scoping import ScopedSession

EnumMember = TypeVar("EnumMember")

class Enum(set, Generic[EnumMember]):
    def __init__(self, *names: EnumMember) -> None: ...
    def __getattr__(self, name: str) -> EnumMember: ...

DomainObjectOperation: Enum[str]

TDomain = TypeVar("TDomain")

class DomainObject(object):
    text_search_fields: List
    Session: ScopedSession
    def __init__(self, **kwargs: Any) -> None: ...
    @classmethod
    def count(cls) -> int: ...
    @classmethod
    def by_name(
        cls: Type[TDomain],
        name: str,
        autoflush: bool = ...,
        for_update: bool = ...,
    ) -> TDomain: ...
    @classmethod
    def text_search(cls, query: Any, term: str) -> Any: ...
    @classmethod
    def active(cls) -> Any: ...
    def save(self) -> None: ...
    def add(self) -> None: ...
    def commit_remove(self) -> None: ...
    def commit(self) -> None: ...
    def remove(self) -> None: ...
    def delete(self) -> None: ...
    def purge(self) -> None: ...
    def as_dict(self) -> Dict: ...
    def from_dict(self, _dict: Dict) -> Tuple[Set, Dict]: ...
    def __lt__(self: TDomain, other: TDomain) -> bool: ...