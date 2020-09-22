from . import TaskSolution, Core


class Solution():
    def __init__(self, tasks: [TaskSolution], cores: [Core]):
        self.tasks = tasks
        self.cores = cores
        self.laxity = None

    def calc_wcrt(self):
        for core in self.cores:
            for i, t in enumerate(core.tasks):
                interference_sum = 0
                interference = 0

                for x in core.tasks[:i]:
                    response_time = interference + (t.wcet*core.WCETFactor)
                    interference = (response_time/x.period) * (x.wcet*core.WCETFactor)
                    interference_sum += interference

                t.wcrt = interference_sum + t.wcet

    def calc_laxity(self):
        n = 0
        laxity_score = 0

        for core in self.cores:
            for t in core.tasks:
                n += 1
                laxity_score += t.deadline-t.wcrt
        
        self.laxity = int(laxity_score / n)