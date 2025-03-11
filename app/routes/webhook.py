from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.serializers.webhook import OrderWebhookPayload, ProductCreate

from app.controllers.webhook import ShopifyWebhook


router = APIRouter(
    prefix="/webhook",
    tags=["webhook"],
    responses={404: {"description": "Not found"}},
)


@router.post("/order", response_model=dict, status_code=201)
async def create_product(product: ProductCreate):
    # response = await ShopifyWebhook.create_product(product.dict())
    # if response.status_code >= 400:
    #     raise HTTPException(status_code=response.status_code, detail=response.content)
    # return response.content
    return await ShopifyWebhook.create_product(product)


# Webhook endpoint for order creation
@router.post("/orders/create/", status_code=200)
async def handle_order_creation_webhook(order: OrderWebhookPayload):
    # Transform Shopify order to your service's format
    # service_order = transform_shopify_order_to_service_order(order)

    # Push to RabbitMQ
    # publish_to_rabbitmq(service_order)

    # Log for debugging
    print(f"Order {order.order_number} queued to RabbitMQ")
    return await ShopifyWebhook.create_order_from_webhook(order)


webhook_router = router
