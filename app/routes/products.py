from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.serializers.products import ProductCreate, ProductResponse
from app.controllers.products import ProductCRUD
from app.config.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[ProductResponse])
async def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await ProductCRUD.get_products(db, skip, limit)


@router.post("", response_model=ProductResponse)
async def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    return await ProductCRUD.create_product(db, payload)


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    return await ProductCRUD.get_product(db, product_id)


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int, payload: ProductCreate, db: Session = Depends(get_db)
):
    return await ProductCRUD.update_product(db, product_id, payload)


@router.delete("/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    return await ProductCRUD.delete_product(db, product_id)


product_router = router
