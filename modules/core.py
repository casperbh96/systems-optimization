
class Core():
    def __init__(self, id: int, mcp: int, WCETFactor: int, util: float, tasks):
        self.id = id
        self.MCPId = mcp
        self.WCETFactor = WCETFactor
        self.tasks = tasks
        self.utilizationPct = util
