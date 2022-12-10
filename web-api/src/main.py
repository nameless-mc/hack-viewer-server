from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from utils.auth import SESSION_KEY
from utils.error import HTTPException, UnauthorizedException
from config import web_api_config, origins
import sys
import db
import model
import uvicorn
from router.events import router as events_router
from router.managements import router as managements_router


app = FastAPI()

origins = [origins]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def request_validation_handler(req: Request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content={"code": "InvalidParameter"})


@app.exception_handler(HTTPException)
async def unicorn_exception_handler(request: Request, exc: HTTPException):
    res = JSONResponse(
        status_code=exc.status_code,
        content=exc.content,
    )
    if(isinstance(exc, UnauthorizedException)):
        res.delete_cookie(key=SESSION_KEY)
    return res

app.include_router(events_router)
app.include_router(managements_router)


def main():
    uvicorn.run('main:app',
                port=int(web_api_config.get("PORT")),
                host=web_api_config.get("HOST"),
                reload=True,)


if __name__ == '__main__':
    main()
