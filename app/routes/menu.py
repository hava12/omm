from fastapi import APIRouter, HTTPException
from typing import ByteString

router = APIRouter(
    prefix="/menus"
)

@router.get("")
async def get_menus():
    return {"Hello": "메뉴"}