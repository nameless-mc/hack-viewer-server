class HTTPException(Exception):
    def __init__(self, status_code: int, code: str, **args) -> None:
        self.status_code = status_code
        self.content = {"code": code, **args}


class ResourceNouFoundException(HTTPException):
    def __init__(self, tag) -> None:
        super().__init__(status_code=404, code="NotFound", tag=tag)


class InvalidParameterException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=403, code="Forbidden")


class ForbiddenException(HTTPException):
    def __init__(self) -> None:
        super().__init__(status_code=403, code="Forbidden")
