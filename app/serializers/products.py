from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    id: int
    title: str
    body_html: Optional[str] = None
    vendor: Optional[str] = None
    product_type: Optional[str] = None
    published_at: Optional[datetime] = None
    status: str = "active"
    handle: Optional[str] = None
    tags: Optional[str] = None
    image: Optional[str] = ""

    class Config:
        from_attributes = True


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
