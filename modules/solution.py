from . import TaskSolution


class Solution():
    def __init__(self, tasks: [TaskSolution]):
        self.tasks = tasks
        self.laxity = None

    def calc_wcrt(self):
        for i, t in enumerate(self.tasks):
            interference_sum = 0
            interference = 0

            for x in self.tasks[:i]:
                response_time = interference + (t.wcet*t.core.WCETFactor)
                interference = (response_time/x.period) * (x.wcet*x.core.WCETFactor)
                interference_sum += interference

            t.wcrt = interference_sum + t.wcet

    def calc_laxity(self):
        pass
