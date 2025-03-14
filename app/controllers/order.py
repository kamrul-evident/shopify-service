from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.order import Order, OrderItem
from app.serializers.order import OrderCreate, OrderResponse


class OrderCRUD:
    @staticmethod
    async def get_orders(db: Session, skip: int = 0, limit: int = 100) -> List[Order]:
        return db.query(Order).offset(skip).limit(limit).all()

    @staticmethod
    async def get_order(db: Session, order_id: str) -> Order:
        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    async def create_order(db: Session, order_data: OrderCreate) -> Order:
        # Check for duplicate shopify_id
        if db.query(Order).filter(Order.shopify_id == order_data.shopify_id).first():
            raise HTTPException(status_code=400, detail="Order already exists.")

        # Create Order
        order = Order(
            id=order_data.shopify_id,
            app_id=order_data.app_id,
            shopify_id=order_data.shopify_id,
            name=order_data.name,
            total_price=order_data.total_price,
            currency=order_data.currency,
            financial_status=order_data.financial_status,
            fulfillment_status=order_data.fulfillment_status,
            order_status_url=order_data.order_status_url,
            processed_at=order_data.processed_at,
        )
        db.add(order)
        db.flush()  # Flush to get order.id before adding items

        # Create Order Items
        for item_data in order_data.order_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item_data.product_id,
                variant_id=item_data.variant_id,
                title=item_data.title,
                variant_title=item_data.variant_title,
                quantity=item_data.quantity,
                price=item_data.price,
                sku=item_data.sku,
            )
            db.add(order_item)

        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    async def update_order(
        db: Session, order_id: str, order_data: OrderCreate
    ) -> Order:
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")

        # Update Order fields
        for key, value in order_data.model_dump(
            exclude={"order_items"}, exclude_unset=True
        ).items():
            setattr(order, key, value)

        # Delete existing items and replace with new ones
        db.query(OrderItem).filter(OrderItem.order_id == order_id).delete()
        for item_data in order_data.order_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item_data.product_id,
                variant_id=item_data.variant_id,
                title=item_data.title,
                variant_title=item_data.variant_title,
                quantity=item_data.quantity,
                price=item_data.price,
                sku=item_data.sku,
            )
            db.add(order_item)

        db.commit()
        db.refresh(order)
        return order

    @staticmethod
    async def delete_order(db: Session, order_id: str) -> dict:
        order = db.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        db.delete(order)  # Cascades to order_items if configured
        db.commit()
        return {"success": True, "message": f"Order {order_id} Deleted Successfully!!!"}
