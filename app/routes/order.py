from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.serializers.order import OrderCreate, OrderResponse
from app.controllers.order import OrderCRUD
from app.config.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[OrderResponse])
async def get_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return await OrderCRUD.get_orders(db, skip, limit)


@router.post("", response_model=OrderResponse)
async def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    return await OrderCRUD.create_order(db, payload)


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str, db: Session = Depends(get_db)):
    order = await OrderCRUD.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(
    order_id: str, payload: OrderCreate, db: Session = Depends(get_db)
):
    return await OrderCRUD.update_order(db, order_id, payload)


@router.delete("/{order_id}")
async def delete_order(order_id: str, db: Session = Depends(get_db)):
    return await OrderCRUD.delete_order(db, order_id)


order_router = router
