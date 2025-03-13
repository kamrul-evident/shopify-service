from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict
from datetime import datetime


class ShopifyShopBase(BaseModel):
    shop_id: int
    name: str
    channel_id: int
    email: Optional[EmailStr] = None
    domain: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = None
    shop_owner: Optional[str] = None
    timezone: Optional[str] = None
    plan_name: Optional[str] = None
    multi_location_enabled: bool = False
    enabled_presentment_currencies: List[str] = []
    shop_metadata: Optional[Dict[str, str]] = None


class ShopifyShopCreate(ShopifyShopBase):
    pass


class ShopifyShopUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    domain: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = None
    shop_owner: Optional[str] = None
    timezone: Optional[str] = None
    plan_name: Optional[str] = None
    multi_location_enabled: Optional[bool] = None
    enabled_presentment_currencies: Optional[List[str]] = None
    shop_metadata: Optional[Dict[str, str]] = None


class ShopifyShopResponse(ShopifyShopBase):
    id: int
    uid: str
    # created_at: datetime = None
    # updated_at: datetime = None

    class Config:
        from_attributes = True
