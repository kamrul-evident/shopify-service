# Serializers
from pydantic import BaseModel
from typing import List, Optional


# Model for product options
class ProductOption(BaseModel):
    name: str
    values: List[str]


# Model for product variants
class ProductVariant(BaseModel):
    option1: str
    price: str  # Shopify expects price as a string (e.g., "19.99")
    sku: Optional[str] = None
    inventory_quantity: Optional[int] = None


# Model for the full product payload
class ProductCreate(BaseModel):
    title: str
    body_html: Optional[str] = None
    vendor: Optional[str] = None
    product_type: Optional[str] = None
    variants: List[ProductVariant]
    options: List[ProductOption]
