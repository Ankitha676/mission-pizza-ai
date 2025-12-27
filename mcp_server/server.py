# # from mcp_server import mock_backend
# #
# # class MCPServer:
# #     def call_tool(self, tool_name: str, payload: dict):
# #         if tool_name == "place_pizza_order":
# #             return mock_backend.place_pizza_order(
# #                 payload["pizza"], payload["size"]
# #             )
# #
# #         if tool_name == "track_order":
# #             return mock_backend.track_order(payload["order_id"])
# #
# #         raise ValueError("Unknown tool")
#
#
#
#
# # mcp_server/server.py
# import uuid
#
# class MCPServer:
#     def __init__(self):
#         self.orders = {}  # store orders as {order_id: order_details}
#
#     def create_order(self, pizza, toppings):
#         order_id = str(uuid.uuid4())[:8]  # short unique ID
#         self.orders[order_id] = {
#             "pizza": pizza,
#             "toppings": toppings,
#             "status": "Preparing"
#         }
#         return order_id
#
#     def track_order(self, order_id):
#         order = self.orders.get(order_id)
#         if order:
#             return f"Order {order_id}: {order['pizza'].capitalize()} pizza with {', '.join(order['toppings']) if order['toppings'] else 'no toppings'} — Status: {order['status']}"
#         else:
#             return f"No order found with ID {order_id}"


# mcp_server/server.py
import uuid
import time
import threading

class MCPServer:
    def __init__(self):
        self.orders = {}  # store orders as {order_id: order_details}

    def create_order(self, pizza, toppings):
        order_id = str(uuid.uuid4())[:8]  # short unique ID
        self.orders[order_id] = {
            "pizza": pizza,
            "toppings": toppings,
            "status": "Preparing"
        }
        # Start background thread to simulate order progress
        threading.Thread(target=self._simulate_order_progress, args=(order_id,), daemon=True).start()
        return order_id

    def track_order(self, order_id):
        order = self.orders.get(order_id)
        if order:
            toppings_text = ", ".join(order["toppings"]) if order["toppings"] else "no toppings"
            return f"Order {order_id}: {order['pizza'].capitalize()} pizza with {toppings_text} — Status: {order['status']}"
        else:
            return f"No order found with ID {order_id}"

    def _simulate_order_progress(self, order_id):
        # Simulate time delays for each stage
        stages = ["Preparing", "Baking", "Out for Delivery", "Delivered"]
        for stage in stages:
            self.orders[order_id]["status"] = stage
            time.sleep(5)  # wait 5 seconds between stages
