

class SimulatedAnnealing():
    def __init__(self):
        pass

    def initial_candidate(self, tasks, mcp_core):
        task_ids = []
        mcp_ids = []
        core_ids = []

        # minimize WCET by checking all combinations of WCET*WCETFactor on all cores
        # don't miss deadlines: 
        # make sure to utilize only 0.69 of each core (utilization, slide 41 in real time systems)
        # utilization for each core: sum(WCET/Period for all tasks) < 0.69
        # fill up cores equally (by utilization percentages)

        return pd.DataFrame({
            'TaskId': [],
            'McpId': [],
            'CoreId': []
        })

    def generate_neighbor(self):
        pass

    def calc_prob(self):
        pass
