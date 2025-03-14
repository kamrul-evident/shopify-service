from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON

from .base import BaseModelWithUUID

# from models.base import BaseModelWithUUID


class ShopifyShop(BaseModelWithUUID):
    __tablename__ = "shopify_shops"
    shop_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    channel_id = Column(Integer, unique=True, nullable=True)
    email = Column(String, nullable=True)
    domain = Column(String, nullable=True)
    country = Column(String, nullable=True)
    currency = Column(String, nullable=True)
    customer_email = Column(String, nullable=True)
    timezone = Column(String, nullable=True)
    shop_owner = Column(String, nullable=True)
    money_format = Column(String, nullable=True)
    weight_unit = Column(String, nullable=True)
    plan_display_name = Column(String, nullable=True)
    plan_name = Column(String, nullable=True)
    has_discounts = Column(Boolean, default=False)
    has_gift_cards = Column(Boolean, default=False)
    primary_location_id = Column(Integer, nullable=True)
    multi_location_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    enabled_presentment_currencies = Column(JSON, nullable=True)
    shop_metadata = Column(JSON, default={})  # Stores access_token and other metadata

    def __repr__(self):
        return f"<ShopifyShop(id={self.shop_id}, name='{self.name}', owner='{self.shop_owner}')>"
