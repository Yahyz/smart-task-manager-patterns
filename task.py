class Task:
    def __init__(self, name):
        self.name = name
        self.priority = 0
        self.status = "Pending"   # ✅ ADD THIS
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

    def change_status(self, status):
        self.status = status   # ✅ STORE STATUS
        self.notify(f"Task '{self.name}' changed to {status}")