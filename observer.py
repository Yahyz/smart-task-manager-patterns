class Observer:
    def update(self, message):
        pass

class EmailNotifier(Observer):
    def __init__(self, notifications):
        self.notifications = notifications

    def update(self, message):
        msg = f"Email: {message}"
        self.notifications.append(msg)

class SMSNotifier(Observer):
    def __init__(self, notifications):
        self.notifications = notifications

    def update(self, message):
        msg = f"SMS: {message}"
        self.notifications.append(msg)

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