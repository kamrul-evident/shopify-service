from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import BaseModelWithUUID  # Adjust import based on your structure


class Order(BaseModelWithUUID):
    __tablename__ = "orders"

    shopify_id = Column(Integer, unique=True, index=True)  # Shopify order ID
    app_id = Column(Integer, nullable=True, default=0)
    name = Column(String, nullable=False)  # e.g., "#1002"
    total_price = Column(Float, nullable=False)  # e.g., 1148.85
    currency = Column(String, nullable=False)  # e.g., "BDT"
    financial_status = Column(String, nullable=True)  # e.g., "paid"
    fulfillment_status = Column(String, nullable=True)  # e.g., null
    order_status_url = Column(String, nullable=True)  # URL for order status
    processed_at = Column(DateTime, nullable=True)  # e.g., "2025-03-11T11:47:00-04:00"

    order_items = relationship("OrderItem", back_populates="order")


class OrderItem(BaseModelWithUUID):
    __tablename__ = "order_items"

    order_id = Column(
        Integer, ForeignKey("orders.id"), nullable=False
    )  # UUID from Order
    product_id = Column(
        Integer, nullable=True
    )  # Shopify product_id (e.g., 9052629467381)
    variant_id = Column(
        Integer, nullable=True
    )  # Shopify variant_id (e.g., 46464261193973)
    title = Column(String, nullable=False)  # e.g., "Men Jeans"
    variant_title = Column(String, nullable=True)  # e.g., "L"
    quantity = Column(Integer, nullable=False)  # e.g., 1
    price = Column(Float, nullable=False)  # e.g., 999.00
    sku = Column(String, nullable=True)  # e.g., "MJ-1234"

    order = relationship("Order", back_populates="order_items")
