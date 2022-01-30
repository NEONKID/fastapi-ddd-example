from fastapi import HTTPException


class BadRequestException(HTTPException):
    def __init__(self):
        super(BadRequestException, self).__init__(status_code=400)


class UnauthorizedException(HTTPException):
    def __init__(self):
        super(UnauthorizedException, self).__init__(status_code=401)


class UnsupportedMediaTypeException(HTTPException):
    def __init__(self):
        super(UnsupportedMediaTypeException, self).__init__(status_code=415)


class ForbiddenException(HTTPException):
    def __init__(self):
        super(ForbiddenException, self).__init__(status_code=403)


class NotFoundException(HTTPException):
    def __init__(self):
        super(NotFoundException, self).__init__(status_code=404)


class ConflictException(HTTPException):
    def __init__(self):
        super(ConflictException, self).__init__(status_code=409)


class InternalServerException(HTTPException):
    def __init__(self, detail):
        super(InternalServerException, self).__init__(status_code=500)
        self.detail = detail

    def __str__(self):
        return self.detail
