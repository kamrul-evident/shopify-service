from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# Order Item Schemas
class OrderItemBase(BaseModel):
    product_id: Optional[int] = None
    variant_id: Optional[int] = None
    title: str
    variant_title: Optional[str] = None
    quantity: int
    price: float
    sku: Optional[str] = None

    class Config:
        from_attributes = True


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: int
    order_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


# Order Schemas
class OrderBase(BaseModel):
    shopify_id: int
    app_id: int
    name: str
    total_price: float
    currency: str
    financial_status: Optional[str] = None
    fulfillment_status: Optional[str] = None
    order_status_url: Optional[str] = None
    processed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OrderCreate(OrderBase):
    order_items: List[OrderItemCreate]  # Nested items for creation


class OrderResponse(OrderBase):
    id: int  # UUID from BaseModelWithUUID
    order_items: List[OrderItemResponse]  # Nested items in response
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
