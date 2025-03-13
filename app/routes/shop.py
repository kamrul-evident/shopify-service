from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.serializers.shop import (
    ShopifyShopResponse,
    ShopifyShopCreate,
    ShopifyShopUpdate,
)
from app.controllers.shop import ShopifyShopHelper
from app.config.database import get_db

router = APIRouter(
    prefix="/shops",
    tags=["shops"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[ShopifyShopResponse])
async def get_shops(db: Session = Depends(get_db)):
    return await ShopifyShopHelper.get_shops(db)


@router.post("", response_model=ShopifyShopResponse)
async def create_shop(shop_data: ShopifyShopCreate, db: Session = Depends(get_db)):
    return await ShopifyShopHelper.create_shop(db, shop_data)


@router.get("/{shop_id}", response_model=ShopifyShopResponse)
async def get_shop(shop_id: int, db: Session = Depends(get_db)):
    return await ShopifyShopHelper.get_shop(db, shop_id)


@router.put("/{shop_id}", response_model=ShopifyShopResponse)
async def update_shop(
    shop_id: int, shop_data: ShopifyShopUpdate, db: Session = Depends(get_db)
):
    return await ShopifyShopHelper.update_shop(db, shop_id, shop_data)


@router.delete("/{shop_id}")
async def delete_shop(shop_id: int, db: Session = Depends(get_db)):
    return await ShopifyShopHelper.delete_shop(db, shop_id)


shop_router = router
