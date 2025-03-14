from sqlalchemy import Column, String, Text, DateTime
from .base import BaseModelWithUUID


class Product(BaseModelWithUUID):
    __tablename__ = "products"
    title = Column(String, nullable=False)
    body_html = Column(Text, nullable=True)
    vendor = Column(String, nullable=True)
    product_type = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=True)
    status = Column(String, default="active")
    handle = Column(String, nullable=True)
    tags = Column(String, nullable=True)
    image = Column(String, nullable=True, default="")

    def __repr__(self):
        return f"{self.id} - {self.title} - {self.product_type}"
