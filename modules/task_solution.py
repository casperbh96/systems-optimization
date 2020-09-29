
class TaskSolution():
    def __init__(self, id: int, util: float, deadline: int, wcet: int, period: int):
        self.id = id
        self.utilizationPct = util
        self.deadline = deadline
        self.wcet = wcet
        self.period = period
        self.wcrt = None