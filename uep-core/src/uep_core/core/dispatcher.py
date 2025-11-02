class MessageDispatcher:
    def __init__(self, router):
        self.router = router

    def dispatch(self, message):
        message_type = message.get("type")
        handler = self.router.get_handler(message_type)
        
        if handler:
            return handler.handle(message)
        else:
            raise ValueError(f"No handler found for message type: {message_type}")