from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def server_ping():
    return "Pong - got {}ms, see `/stats` for more"
  
@router.get("/stats")
async def server_stats():
    ...


@router.get("/stats/archives")
async def archive_stats():
    ...
