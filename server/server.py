import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .routes import collections, items, filesystem  # type:ignore

kyron_proxy = FastAPI()

SERVER_PORT = 4000
ACCEPTED_ORIGINS = [
    "http://localhost",
    f"http://localhost:{SERVER_PORT}",
]
ACCEPTED_HOSTS = [
    "localhost",
    "127.0.0.1"
]

kyron_proxy.add_middleware(
    CORSMiddleware,
    allow_origins=ACCEPTED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
kyron_proxy.add_middleware(
    TrustedHostMiddleware, allowed_hosts=ACCEPTED_HOSTS
)


@kyron_proxy.get("/")
async def root():
    return {"message": "it's me"}

kyron_proxy.include_router(collections.router, tags=["collections", "fs"])
kyron_proxy.include_router(items.router, tags=["items", "fs"])
kyron_proxy.include_router(filesystem.router, prefix="/fs", tags=["fs"])

if __name__ == "__main__":
    uvicorn.run("server:kyron_proxy", host="localhost",
                port=SERVER_PORT, reload=True)
