from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.shop import ShopifyShop
from app.serializers.shop import (
    ShopifyShopCreate,
    ShopifyShopUpdate,
    ShopifyShopResponse,
)


class ShopifyShopHelper:
    @staticmethod
    async def get_shops(db: Session):
        shops = db.query(ShopifyShop).all()
        return shops

    @staticmethod
    async def create_shop(db: Session, shop_data: ShopifyShopCreate):
        existing_shop = (
            db.query(ShopifyShop)
            .filter(ShopifyShop.shop_id == shop_data.shop_id)
            .first()
        )
        if existing_shop:
            raise HTTPException(status_code=400, detail="Shop already exists")

        new_shop = ShopifyShop(
            shop_id=shop_data.shop_id,
            name=shop_data.name,
            channel_id=shop_data.channel_id,
            email=shop_data.email,
            domain=shop_data.domain,
            country=shop_data.country,
            currency=shop_data.currency,
            shop_owner=shop_data.shop_owner,
            timezone=shop_data.timezone,
            plan_name=shop_data.plan_name,
            multi_location_enabled=shop_data.multi_location_enabled,
            enabled_presentment_currencies=shop_data.enabled_presentment_currencies,
            shop_metadata=shop_data.shop_metadata,
        )

        db.add(new_shop)
        db.commit()
        db.refresh(new_shop)
        return new_shop

    @staticmethod
    async def get_shop(db: Session, shop_id: int):
        shop = db.query(ShopifyShop).filter(ShopifyShop.shop_id == shop_id).first()
        if not shop:
            raise HTTPException(status_code=404, detail="Shop not found")
        return shop

    @staticmethod
    async def update_shop(db: Session, shop_id: int, shop_data: ShopifyShopUpdate):
        shop = db.query(ShopifyShop).filter(ShopifyShop.shop_id == shop_id).first()
        if not shop:
            raise HTTPException(status_code=404, detail="Shop not found")

        for key, value in shop_data.model_dump(exclude_unset=True).items():
            setattr(shop, key, value)

        db.commit()
        db.refresh(shop)
        return shop

    @staticmethod
    async def delete_shop(db: Session, shop_id: int):
        shop = db.query(ShopifyShop).filter(ShopifyShop.shop_id == shop_id).first()
        if not shop:
            raise HTTPException(status_code=404, detail="Shop not found")

        db.delete(shop)
        db.commit()
        return {"message": "Shop deleted successfully"}
