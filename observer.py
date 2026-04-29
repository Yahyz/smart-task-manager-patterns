class Observer:
    def update(self, message):
        pass

class EmailNotifier(Observer):
    def update(self, message):
        print(f"Email: {message}")

class SMSNotifier(Observer):
    def update(self, message):
        print(f"SMS: {message}")

class Task:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

    def change_status(self, status):
        self.notify(f"Task '{self.name}' changed to {status}")