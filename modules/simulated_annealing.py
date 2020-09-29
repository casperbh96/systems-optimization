import copy
import itertools
import operator

from . import Solution, Core, TaskSolution
import pandas as pd
from operator import attrgetter
from random import randrange
import numpy as np
import random


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

        # Sort list of cores most efficient first from dataframe
        sortedCores = mcp_core.values.tolist()
        #sortedCores.sort(key=lambda x: float(x[2]))

        # Create core objects and append to core object list
        for dfCore in sortedCores:
            core = Core(dfCore[0], dfCore[1], float(dfCore[2]), 0, [])
            cores.append(core)

        # Sort list of tast heaviest tast first from dataframe
        sortedTasks = tasks.values.tolist()
        #sortedTasks.sort(key=lambda x: int(x[3]) / int(x[2]), reverse=True)

        # For each task assign to core with least load and create TaskSolution obj
        for task in sortedTasks:
            #find least loaded core
            core = min(cores, key=attrgetter('utilizationPct'))
            util = (float(task[3])/float(task[2]))*float(core.WCETFactor)
            taskObj = TaskSolution(task[0], util, int(task[1]), int(task[3]), int(task[2]))
            core.utilizationPct += util
            taskAssignments.append(taskObj)
            core.tasks.append(taskObj)

        # Create solution object from assigned
        solution = Solution(taskAssignments,cores)

        return solution

    def generate_neighbor(self, solution):
        selectedCores = []
        selectedTasks = []
        
        while len(selectedCores) != 4 and len(selectedTasks) != 4:
            core = solution.cores[random.randint( 0,len(solution.cores)-1 )]
            task = core.tasks[random.randint( 0,len(core.tasks)-1 )]

            if task not in selectedTasks:
                selectedTasks.append(task)
            if core not in selectedCores:
                selectedCores.append(core)

        unique_combinations = itertools.product(selectedTasks, selectedCores)

        newSolution = None
        for combination in unique_combinations:
            #combination[0] = selectedTask
            #combination[1] = selectedCore
            possibleSolution = copy.deepcopy(solution)

            core = None
            for c in possibleSolution.cores:
                for t in c.tasks:
                    if t.id == combination[0].id:
                        core = c
            
            remove_task = None
            for task in core.tasks:
                if task.id == combination[0].id:
                    remove_task = task

            core.tasks.remove(remove_task)
            
            core = next(filter(lambda x: x.id == combination[1].id and x.MCPId == combination[1].MCPId, possibleSolution.cores))
            core.tasks.append(combination[0])

            possibleSolution.calc_wcrt()
            laxity = possibleSolution.calc_laxity()

            if newSolution == None or newSolution.laxity < laxity:
                newSolution = possibleSolution

        return newSolution

    def calc_prob(self, c, c_next, temp):
        change = c.calc_laxity()-c_next.calc_laxity()
        return np.exp(change/temp)
