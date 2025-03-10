from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.serializers.shopify_admin import ProductCreate

from app.controllers.shopify_admin import ShopifyAdmin


router = APIRouter(
    prefix="/shopify-admin",
    tags=["shopify-admin"],
    responses={404: {"description": "Not found"}},
)


@router.get("/shops")
async def get_shops():
    return await ShopifyAdmin.get_authorized_shops()


@router.get("/products")
async def get_products():
    return await ShopifyAdmin.get_all_products()


# Route to create a product
@router.post("/products/", response_model=dict, status_code=201)
async def create_product(product: ProductCreate):
    return await ShopifyAdmin.create_product(product.dict())


@router.get("/products/{product_id}")
async def get_single_product(product_id: int):
    return await ShopifyAdmin.get_single_product_details(product_id)


@router.get("/orders")
async def get_orders():
    return await ShopifyAdmin.get_orders()


@router.get("/orders/{order_id}")
async def get_single_order(order_id: int):
    return await ShopifyAdmin.get_single_order(order_id)


@router.get("/invenotry")
async def get_inventory_level(inventory_id: int):
    return await ShopifyAdmin.get_inventory_level(inventory_id)


@router.post("/inventory/update/", response_model=dict)
async def update_inventory(inventory_item_id: int, location_id: int, available: int):
    return await ShopifyAdmin.update_inventory_level(
        inventory_item_id=inventory_item_id,
        location_id=location_id,
        available=available,
    )


shopify_router = router
