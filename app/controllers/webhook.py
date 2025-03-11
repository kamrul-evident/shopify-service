from app.serializers.webhook import OrderWebhookPayload, ProductCreate

from app.helpers.order import process_order_data
from app.utils.publisher import publish_to_rabbitmq


class ShopifyWebhook:
    @staticmethod
    async def create_order_from_webhook(order: OrderWebhookPayload):
        payload = process_order_data(order)
        try:
            publish_to_rabbitmq(payload)
            return {"message": f"Order {order.order_number} placed in rabbit mq"}
        except Exception as e:
            return {
                "message": f"Order {order.order_number} failed to add in the queue",
                "error": str(e),
            }

    @staticmethod
    async def create_product(product: ProductCreate):
        print("Product Create Data", product)
        return {"message": "Product Created successfully!!!"}
