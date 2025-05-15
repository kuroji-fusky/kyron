import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware


SERVER_PORT = 4000

archive_app = FastAPI()

origins = [
    "http://localhost",
    f"http://localhost:{SERVER_PORT}",
]
hosts = ["localhost", "127.0.0.1"]


archive_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["*"],
)
archive_app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=hosts
)


@archive_app.get("/")
async def root():
    return {"message": "It's me, hi, I'm the problem it's me~"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=SERVER_PORT, reload=True)
