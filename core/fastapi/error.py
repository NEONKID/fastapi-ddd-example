from fastapi import status, Request, FastAPI
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.responses import PlainTextResponse
from pydantic import EmailStr

from core.fastapi.responses import ORJSONResponse


def init_error_handler(app: FastAPI, admin_email: str):
    @app.exception_handler(Exception)
    async def internal_server_error_handle(req: Request, exc: Exception):
        return ORJSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                'title': type(exc).__name__,
                'description': str(exc) + ', Contact me ({})'.format(admin_email)
            }
        )

    @app.exception_handler(RequestValidationError)
    async def request_exception_handle(req: Request, exc: RequestValidationError):
        return ORJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'title': 'invalid:data',
                'description': 'wrong value',
                'extra': exc.errors()
            }
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handle(req: Request, exc: StarletteHTTPException):
        if exc.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            return await internal_server_error_handle(req, exc)

        return PlainTextResponse(status_code=exc.status_code)
