
class TaskSolution():
    def __init__(self, id: int, mcp: int, core: int, util: float):
        self.id = id
        self.mcp = mcp
        self.core = core
        self.utilizationPct = util
        self.wcrt = None