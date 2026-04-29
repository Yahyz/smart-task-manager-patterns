class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
        self.tasks.append(task)