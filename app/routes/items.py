from fastapi import APIRouter, Depends, Query
from app.schemas import ItemQuery, convert_query_to_item
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

@router.get("/id/{prod_name}", dependencies=[Depends(verify_token)])
async def get_id(prod_name: str):
    return sheets.get_id_by_prod_name(prod_name)

@router.post("/", dependencies=[Depends(verify_token)])
async def create(item: ItemQuery):
    return sheets.add_item(convert_query_to_item(item))

@router.put("/", dependencies=[Depends(verify_token)])
async def update(item: ItemQuery):
    return sheets.update_item(convert_query_to_item(item))

@router.delete("/{prod_name}", dependencies=[Depends(verify_token)])
async def remove(prod_name: str):
    return sheets.delete_row_by_prod_name(prod_name)
