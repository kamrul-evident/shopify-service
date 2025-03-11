from app.serializers.webhook import OrderWebhookPayload


# Transform Shopify order to your order service format
def process_order_data(shopify_order: OrderWebhookPayload) -> dict:
    # Extract shipping address if available, otherwise use defaults
    shipping_address = shopify_order.shipping_address or {}

    # Map Shopify line items to your order_items format
    order_items = [
        {
            "product_id": item.variant_id,  # Using variant_id as a proxy for product_id
            "quantity": item.quantity,
            "price": item.price,
            "name": item.name,
            "sku": item.sku or "",
        }
        for item in shopify_order.line_items
    ]

    # Build the payload for your order service
    service_order = {
        "channel": "shopify",  # Assuming Shopify as the channel
        "channel_order_id": str(shopify_order.id),
        "app_id": shopify_order.app_id,
        "payment_status": shopify_order.financial_status,
        "payment_method": "",  # Not directly available in webhook, set as needed
        "purchase_date": shopify_order.created_at,
        "currency": shopify_order.currency,
        "market_place": "shopify",
        "dispatch_status": shopify_order.fulfillment_status or "pending",
        "dispatch_identifier": "",
        "dispatched_by": "",
        "dispatched_at": None,
        "shipped_at": None,
        "order_meta": {
            "shopify_order_number": shopify_order.order_number,
            "total_tax": shopify_order.total_tax,
            "subtotal_price": shopify_order.subtotal_price,
        },
        "order_items": order_items,
        "shipping_address": {
            "buyer_name": shipping_address.get("name", ""),
            "address1": shipping_address.get("address1", ""),
            "address2": shipping_address.get("address2", ""),
            "city": shipping_address.get("city", ""),
            "state": shipping_address.get("province", ""),
            "post_code": shipping_address.get("zip", ""),
            "country": shipping_address.get("country", ""),
            "phone": shipping_address.get("phone", ""),
            "reference_id": "",  # Not available in webhook
            "email": shipping_address.get("email", ""),
        },
    }
    return service_order
