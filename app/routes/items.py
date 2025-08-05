from fastapi import APIRouter, Depends, Query
from app.security import verify_token
from app.sheets import sheets
from typing import Optional

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", dependencies=[Depends(verify_token)])
async def get_items():
    return sheets.get_items()

@router.get("/{idx}", dependencies=[Depends(verify_token)])
async def get_item(idx: int):
    return sheets.get_item(idx)
