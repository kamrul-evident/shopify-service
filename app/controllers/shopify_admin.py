import requests
from fastapi.responses import JSONResponse

from app.config.app_vars import ADMIN_API_ACCESS_TOKEN

base_url: str = "https://test-kamrul.myshopify.com/admin/api/2025-01/"


class ShopifyAdmin:

    @staticmethod
    async def get_single_product_details(product_id: int):
        url: str = base_url + f"products/{product_id}.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ADMIN_API_ACCESS_TOKEN,
        }
        response = requests.get(url=url, headers=headers)
        return JSONResponse(content=response.json(), status_code=response.status_code)

    @staticmethod
    async def get_all_products():
        url: str = base_url + "products.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ADMIN_API_ACCESS_TOKEN,
        }
        response = requests.get(url=url, headers=headers)
        print(response)
        return JSONResponse(content=response.json(), status_code=response.status_code)

    @staticmethod
    async def get_authorized_shops():
        url: str = base_url + "shop.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ADMIN_API_ACCESS_TOKEN,
        }
        response = requests.get(url=url, headers=headers)
        return JSONResponse(content=response.json(), status_code=response.status_code)

    @staticmethod
    async def get_orders():
        url: str = base_url + "orders.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ADMIN_API_ACCESS_TOKEN,
        }
        response = requests.get(url=url, headers=headers)
        return JSONResponse(content=response.json(), status_code=response.status_code)

    @staticmethod
    async def get_single_order(order_id: int):
        url: str = base_url + f"orders/{order_id}.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ADMIN_API_ACCESS_TOKEN,
        }
        response = requests.get(url=url, headers=headers)
        return JSONResponse(content=response.json(), status_code=response.status_code)

    @staticmethod
    async def get_inventory_level(inventory_id: int):
        url: str = base_url + "inventory_levels.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ADMIN_API_ACCESS_TOKEN,
        }
        params = {"inventory_item_ids": inventory_id}
        response = requests.get(url=url, headers=headers, params=params)
        return JSONResponse(content=response.json(), status_code=response.status_code)

    @staticmethod
    async def create_product(product_data: dict):
        url: str = base_url + "products.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ADMIN_API_ACCESS_TOKEN,
        }
        payload = {"product": product_data}
        response = requests.post(url=url, headers=headers, json=payload)
        return JSONResponse(content=response.json(), status_code=response.status_code)

    @staticmethod
    async def update_inventory_level(
        inventory_item_id: int, location_id: int, available: int
    ):
        url: str = base_url + "inventory_levels/set.json"
        headers = {
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": ADMIN_API_ACCESS_TOKEN,
        }
        payload = {
            "inventory_item_id": inventory_item_id,
            "location_id": location_id,
            "available": available,
        }
        response = requests.post(url=url, headers=headers, json=payload)
        return JSONResponse(content=response.json(), status_code=response.status_code)
