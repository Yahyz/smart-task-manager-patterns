class SortStrategy:
    def sort(self, tasks):
        pass

class SortByName(SortStrategy):
    def sort(self, tasks):
        return sorted(tasks, key=lambda x: x.name)

class SortByPriority(SortStrategy):
    def sort(self, tasks):
        return sorted(tasks, key=lambda x: x.priority)

class SortByNameLength(SortStrategy):
    def sort(self, tasks):
        return sorted(tasks, key=lambda x: len(x.name))

class TaskSorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort_tasks(self, tasks):
        return self.strategy.sort(tasks)