
class EventDispatcher:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event_name, handler):

        if event_name not in self.handlers:
            self.handlers[event_name] = []

        self.handlers[event_name].append(handler)

    def publish(self, event_name, data):

        print(f"\nEvent Published: {event_name}")

        for handler in self.handlers.get(event_name, []):
            handler(data)
