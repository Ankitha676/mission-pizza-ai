import uuid
from datetime import datetime, timedelta

ORDERS = {}

def place_pizza_order(pizza: str, size: str):
    order_id = str(uuid.uuid4())
    eta = datetime.now() + timedelta(minutes=20)

    order = {
        "order_id": order_id,
        "pizza": pizza,
        "size": size,
        "status": "preparing",
        "eta": eta.isoformat()
    }

    ORDERS[order_id] = order
    return order


def track_order(order_id: str):
    return ORDERS.get(order_id, {"error": "Order not found"})
