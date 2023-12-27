from fastapi import APIRouter, HTTPException
from typing import ByteString

router = APIRouter()

@router.get("/menus")
async def get_menus():
    return {"Hello": "메뉴"}