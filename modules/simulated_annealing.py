import operator

from . import Solution, Core, TaskSolution
import pandas as pd
from operator import attrgetter



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


        #sorted(test, key=operator.itemgetter(3))


        cores = []
        taskAssignments = []

        sortedCores = mcp_core.values.tolist()
        sortedCores.sort(key=lambda x: float(x[2]))
        for dfCore in sortedCores:
            core = Core(dfCore[0], dfCore[1], dfCore[2], 0)
            cores.append(core)

        sortedTasks = tasks.values.tolist()
        sortedTasks.sort(key=lambda x: int(x[3]) / int(x[2]), reverse=True)
        for task in sortedTasks:
            #find least loaded core
            core = min(cores, key=attrgetter('utilizationPct'))
            util = (float(task[3])/float(task[2]))*float(core.WCETFactor)
            taskObj = TaskSolution(task[0], core.MCPId, core.id, util)
            core.utilizationPct += util
            taskAssignments.append(taskObj)
            #set new percentage

        solution = Solution(taskAssignments)

        return solution

    def generate_neighbor(self):
        pass

    def calc_prob(self):
        pass
