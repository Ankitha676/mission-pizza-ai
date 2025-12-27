import json
import uuid
import threading
import time

class MCPServer:
    """
    Dynamic MCPServer generated from OpenAPI.
    Supports /menu, /order, /order/{id}.
    """
    def __init__(self, openapi_path):
        with open(openapi_path) as f:
            self.spec = json.load(f)
        self.orders = {}

    def get_menu(self):
        # Dynamic menu (can extend via spec)
        return {
            "pizzas": ["Margherita", "Pepperoni", "Veggie", "BBQ Chicken"],
            "toppings": ["cheese", "mushrooms", "olives", "pepperoni", "jalapenos"]
        }

    def create_order(self, pizza, toppings=None):
        toppings = toppings or []
        order_id = str(uuid.uuid4())[:8]
        self.orders[order_id] = {"pizza": pizza, "toppings": toppings, "status": "Preparing"}
        threading.Thread(target=self._simulate_progress, args=(order_id,), daemon=True).start()
        return order_id

    def track_order(self, order_id):
        order = self.orders.get(order_id)
        if order:
            toppings_text = ", ".join(order["toppings"]) if order["toppings"] else "no toppings"
            return f"Order {order_id}: {order['pizza']} pizza with {toppings_text} — Status: {order['status']}"
        return f"No order found with ID {order_id}"

    def _simulate_progress(self, order_id):
        stages = ["Preparing", "Baking", "Out for Delivery", "Delivered"]
        for stage in stages:
            self.orders[order_id]["status"] = stage
            time.sleep(5)
