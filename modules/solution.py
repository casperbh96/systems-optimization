from . import TaskSolution


class Solution():
    def __init__(self, tasks: [TaskSolution]):
        self.tasks = tasks
        self.laxity = None

    def calc_laxity(self):
        pass
