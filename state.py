class ConversationState:
    def __init__(self):
        self.step = "ask_order"
        self.order = None
        self.toppings = []
        self.last_order_id = None
