from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.products import Product
from app.serializers.products import ProductCreate


class ProductCRUD:
    @staticmethod
    async def get_products(
        db: Session, skip: int = 0, limit: int = 100
    ) -> List[Product]:
        return db.query(Product).offset(skip).limit(limit).all()

    @staticmethod
    async def get_product(db: Session, product_id: str) -> Product:
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    async def create_product(db: Session, product_data: ProductCreate) -> Product:
        product = db.query(Product).filter(Product.id == product_data.id).first()
        if product:
            raise HTTPException(status_code=400, detail="Product already exists.")
        product = Product(
            id=product_data.id,  # Omit if UUID is auto-generated
            title=product_data.title,
            body_html=product_data.body_html,
            vendor=product_data.vendor,
            product_type=product_data.product_type,
            published_at=product_data.published_at,
            status=product_data.status,
            handle=product_data.handle,
            tags=product_data.tags,
            image=product_data.image,
        )
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    async def update_product(
        db: Session, product_id: str, product_data: ProductCreate
    ) -> Product:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        for key, value in product_data.model_dump(exclude_unset=True).items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    async def delete_product(db: Session, product_id: str) -> bool:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        db.delete(product)
        db.commit()
        return {"success": True, "message": f"{product_id} Deleted Successfully!!!"}
