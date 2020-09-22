from modules import DataLoader, DeadlineMonotic, SimulatedAnnealing
import random


loader = DataLoader()

# dict/dictionary == hashtable
dictionary = loader.load_xml_by_name('small')

task_df = loader.get_tasks_to_dataframe(
    dictionary['Application']['Task']
)

mcp_core_df = loader.get_mcp_to_dataframe(
    dictionary['Platform']['MCP']
)

annealing = SimulatedAnnealing()
dm = DeadlineMonotic()

temp = 10000
temp_decrease = 0.003
c = annealing.initial_candidate(task_df, mcp_core_df)
list_of_schedules = [] # ordered by laxity

while temp > 1:
    c_next = annealing.generate_neighbor(c)
    c_next.calc_wcrt()

    if annealing.calc_prob(c, c_next, temp) > random.uniform(0, 1):
        c = c_next

        if dm.is_solution(c):
            if len(list_of_schedules) == 0: 
                list_of_schedules.append(c)

            for i, schedule in enumerate(list_of_schedules):
                if schedule.laxity > c.laxity:
                    list_of_schedules.insert(i, c)
                    break

    temp = temp * (1 - temp_decrease)
    print(temp)

print(list_of_schedules[0].laxity)