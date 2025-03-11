from typing import Any, Dict, List, Optional
from pydantic import BaseModel


# Pydantic models for product creation
class ProductOption(BaseModel):
    name: str
    values: List[str]


class ProductVariant(BaseModel):
    option1: str
    price: str
    sku: Optional[str] = None
    inventory_quantity: Optional[int] = None


class ProductCreate(BaseModel):
    title: str
    body_html: Optional[str] = None
    vendor: Optional[str] = None
    product_type: Optional[str] = None
    variants: List[ProductVariant]
    options: List[ProductOption]


# Pydantic model for Shopify webhook payload (simplified)
class OrderLineItem(BaseModel):
    id: int
    variant_id: int
    quantity: int
    price: str
    name: str
    sku: Optional[str] = None


class OrderWebhookPayload(BaseModel):
    id: int
    order_number: int
    app_id: int
    created_at: str
    current_total_price: str
    currency: str
    financial_status: str
    fulfillment_status: Optional[str] = None
    line_items: List[OrderLineItem]
    customer: Optional[Dict[str, Any]] = None
    total_tax: Optional[str] = None
    subtotal_price: Optional[str] = None
    shipping_address: Optional[Dict[str, Any]] = None
