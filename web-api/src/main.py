from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from config import web_api_config, origins
import sys
import db
import model
import uvicorn
from router.events import router as events_router


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
async def request_validation_handler(req, exc):
    return JSONResponse(status_code=400, content={"code": "InvalidParameter"})

app.include_router(events_router)

def main():
    uvicorn.run('main:app',
                port=int(web_api_config.get("PORT")),
                host=web_api_config.get("HOST"),
                reload=True,)

if __name__ == '__main__':
    main()
