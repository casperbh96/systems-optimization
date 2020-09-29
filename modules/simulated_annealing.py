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
        sortedCores.sort(key=lambda x: float(x[2]))

        # Create core objects and append to core object list
        for dfCore in sortedCores:
            core = Core(dfCore[0], dfCore[1], float(dfCore[2]), 0, [])
            cores.append(core)

        # Sort list of tast heaviest tast first from dataframe
        sortedTasks = tasks.values.tolist()
        sortedTasks.sort(key=lambda x: int(x[3]) / int(x[2]), reverse=True)

        # For each task assign to core with least load and create TaskSolution obj
        for task in sortedTasks:
            #find least loaded core
            core = min(cores, key=attrgetter('utilizationPct'))
            util = (float(task[3])/float(task[2]))*float(core.WCETFactor)
            taskObj = TaskSolution(task[0], core, util, int(task[1]), int(task[3]), int(task[2]))
            core.utilizationPct += util
            taskAssignments.append(taskObj)
            core.tasks.append(taskObj)

        # Create solution object from assigned
        solution = Solution(taskAssignments,cores)

        return solution

    def generate_neighbor(self, solution):
        #Get random links in solution
        link1 = randrange(0, len(solution.tasks) - 1)
        link2 = randrange(0, len(solution.tasks) - 1)
        link3 = randrange(0, len(solution.tasks) - 1)
        link4 = randrange(0, len(solution.tasks) - 1)
        selectedLinks = [link1, link2, link3, link4]
        selectedCores = [solution.tasks[link1].core_obj.id, solution.tasks[link2].core_obj.id, solution.tasks[link3].core_obj.id, solution.tasks[link4].core_obj.id]


        # Get all combinations of cores and tasks
        unique_combinations = []
        permut = itertools.permutations(selectedLinks, len(selectedCores))
        for comb in permut:
            zipped = zip(comb, selectedCores)
            unique_combinations.append(list(zipped))

        newSolution = None
        # Assign new cores for all combinations and get best solution
        for combination in unique_combinations:
            possibleSolution = copy.deepcopy(solution)
            #assign new cores foreach index-core combination
            for ic in combination:
                possibleSolution.tasks[ic[0]].core = ic[1]

            newSolution = copy.deepcopy(possibleSolution)

        return newSolution

    def calc_prob(self, c, c_next, temp):
        change = c.calc_laxity()-c_next.calc_laxity()
        return np.exp(change/temp)
