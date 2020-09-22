
class TaskSolution():
    def __init__(self, id: int, core_obj, util: float, deadline: int, wcet: int, period: int):
        self.id = id
        self.core_obj = core_obj
        self.utilizationPct = util
        self.deadline = deadline
        self.wcet = wcet
        self.period = period
        self.wcrt = None