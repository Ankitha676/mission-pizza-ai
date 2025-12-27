from mcp_server.mcp_generator import MCPServer

class OrderingAgent:
    def __init__(self, mcp_server: MCPServer):
        self.mcp = mcp_server

    def respond(self, user_input, state):
        user_input = user_input.strip().lower()

        if user_input.startswith("track "):
            order_id = user_input.split(" ")[1]
            return self.mcp.track_order(order_id)

        if state.step == "ask_order":
            menu = [p.lower() for p in self.mcp.get_menu()["pizzas"]]
            if user_input in menu:
                state.order = user_input
                state.step = "ask_toppings"
                return f"Great! You selected {user_input.capitalize()}.Would you like extra toppings? (yes/no)"
            else:
                return f"Please choose a valid pizza: {', '.join(self.mcp.get_menu()['pizzas'])}"

        elif state.step == "ask_toppings":
            if user_input in ["yes", "y"]:
                state.step = "choose_topping"
                return "Type the topping you want (e.g., cheese, mushrooms)."
            elif user_input in ["no", "n"]:
                state.step = "confirm_order"
                return f"Confirming your order: {state.order.capitalize()} pizza with no toppings. (yes to confirm / no to cancel)"
            return "Please answer with yes/no."

        elif state.step == "choose_topping":
            state.toppings.append(user_input)
            state.step = "confirm_more_toppings"
            return "Topping added! Another topping? (yes/no)"

        elif state.step == "confirm_more_toppings":
            if user_input in ["yes", "y"]:
                state.step = "choose_topping"
                return "Type next topping."
            elif user_input in ["no", "n"]:
                state.step = "confirm_order"
                toppings_text = ", ".join(state.toppings)
                return f"Confirming order: {state.order.capitalize()} pizza with {toppings_text}. (yes to confirm / no to cancel)"
            return "Please answer yes/no."

        elif state.step == "confirm_order":
            if user_input in ["yes", "y"]:
                order_id = self.mcp.create_order(state.order, state.toppings)
                state.last_order_id = order_id
                state.step = "completed"
                toppings_text = ", ".join(state.toppings) if state.toppings else "no toppings"
                return f"Order placed! {state.order.capitalize()} pizza with {toppings_text}. Order ID: {order_id}. Track: track {order_id}"
            elif user_input in ["no", "n"]:
                state.step = "ask_order"
                state.order, state.toppings = None, []
                return "Order cancelled. Start again.What pizza would you like?"
            return "Please answer yes/no."

        # Step 6: completed
        elif state.step == "completed":
            return f"Order completed! Track: track {state.last_order_id} or start new order."

        return "I didn't understand that."
