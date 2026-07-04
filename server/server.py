import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

kyron_proxy = FastAPI()

ACCEPTED_ORIGINS = [
    "http://localhost",
    "http://localhost:4000",
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

if __name__ == "__main__":
    uvicorn.run("main:kyron_proxy", host="localhost", port=4000, reload=True)
