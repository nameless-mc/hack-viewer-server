from fastapi.responses import JSONResponse

invalidParameterError = JSONResponse(
    status_code=400, content={"code": "InvalidParameter"})

forbiddenError = JSONResponse(status_code=403, content={"code": "Forbidden"})


def resourceNouFoundError(tag):
    return JSONResponse(status_code=404, content={"code": "NotFound", "tag": tag})
