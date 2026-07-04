from fastapi import APIRouter

router = APIRouter()

@router.get("/items", tags=["items"])
async def get_archive_items():
    ...

@router.post("/items/new", tags=["items"])
async def create_new_item():
    ...

@router.patch("/items/{item_slug}", tags=["items"])
async def update_archive_items():
    ...
    
@router.delete("/items/{item_slug}", tags=["items"])
async def delete_one_item():
    ...
