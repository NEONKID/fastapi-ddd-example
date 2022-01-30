from starlette.responses import JSONResponse
from sqlalchemy.ext.associationproxy import _AssociationList
from typing import Any

try:
    import orjson
except ImportError:  # pragma: nocover
    orjson = None  # type: ignore


def default(obj):
    if isinstance(obj, _AssociationList):
        return list(obj)
    raise TypeError


class ORJSONResponse(JSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed to use ORJSONResponse"
        return orjson.dumps(content, default=default)
