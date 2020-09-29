from . import TaskSolution, Core


class Solution():
    def __init__(self, cores: [Core]):
        self.cores = cores
        self.laxity = None
        self.calc_wcrt()

    def calc_wcrt(self):
        for core in self.cores:
            for i, t in enumerate(core.tasks):

                interference = 0

                response_time = interference + (t.wcet * core.WCETFactor)
                for x in core.tasks[:i]:
                    interference += (response_time/x.period) * (x.wcet*core.WCETFactor)

                t.wcrt = interference + t.wcet

    def calc_laxity(self):
        n = 0
        laxity_score = 0

        for core in self.cores:
            for t in core.tasks:
                n += 1
                laxity_score += t.deadline-t.wcrt
        
        self.laxity = int(laxity_score / n)
        
        return self.laxity