from mcp_server.mcp_generator import MCPServer
from agents.ordering_agent import OrderingAgent
from agents.scheduling_agent import SchedulingAgent
from state import ConversationState

def main():
    mcp = MCPServer("openapi/pizza_openapi.json")
    ordering_agent = OrderingAgent(mcp)
    scheduling_agent = SchedulingAgent()
    state = ConversationState()

    print("Mission Pizza AI Chatbot")
    print("Type 'exit' to quit\n")
    print("Bot: What would you like to order?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = ordering_agent.respond(user_input, state)
        print(f"\nBot: {response}\n")

        if state.step == "completed" and state.last_order_id:
            order_details = {
                "order_id": state.last_order_id,
                "pizza": state.order,
                "toppings": state.toppings
            }
            schedule_msg = scheduling_agent.schedule_delivery(order_details)
            print(f"Bot: {schedule_msg}\n")

if __name__ == "__main__":
    main()
