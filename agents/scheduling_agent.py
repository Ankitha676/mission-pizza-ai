import time

class SchedulingAgent:
    def schedule_delivery(self, order_details):
        order_id = order_details["order_id"]
        pizza = order_details["pizza"]
        toppings = ", ".join(order_details["toppings"]) if order_details["toppings"] else "no toppings"
        # Simulate external MCP scheduling
        time.sleep(1)
        return f"📅 Delivery scheduled for Order {order_id}: {pizza} pizza with {toppings} in 30 minutes!"
