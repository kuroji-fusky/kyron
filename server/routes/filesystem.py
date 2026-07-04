"""
Endpoints for dealing with the server's file system

It almost assumes the server its running on is likely running Linux
(or a UNIX variant), Windows might need a patchy workaround its quirks.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/get-tree", tags=["fs"])
async def get_dir_tree():
  ...
  
@router.get("/get-marked-archives", tags=["fs"])
async def get_marked_archives():
  ...

@router.delete("/safe-delete", tags=["fs", "delete"])
async def safe_file_delete():
  """
  Marks the file(s) as safe to be deleted in the future
  """
  ...

@router.delete("/delete", tags=["fs", "delete"])
async def perm_delete():
  """
  Performs a low-level file deletion, either by the 30-day
  period or user choice
  """
  ...