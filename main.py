from modules import DataLoader, DeadlineMonotic, SimulatedAnnealing
import random


loader = DataLoader()

# dict/dictionary == hashtable
dictionary = loader.load_xml_by_name('large')

task_df = loader.get_tasks_to_dataframe(
    dictionary['Application']['Task']
)

mcp_core_df = loader.get_mcp_to_dataframe(
    dictionary['Platform']['MCP']
)

print(mcp_core_df.head(5))

annealing = SimulatedAnnealing()
dm = DeadlineMonotic()

temp = 10000
temp_decrease = 0.003
c = annealing.initial_candidate(task_df, mcp_core_df) # worst case executing time
list_of_schedules = [] # ordered by average laxity

while temp > 1:
    c_next = annealing.generate_neighbor()
    WCRT = None # https://academic.oup.com/comjnl/article/29/5/390/486162

    if annealing.calc_prob() > random.uniform(0, 1):
        c = c_next

        if dm.is_solution():
            if len(list_of_schedules) == 0: 
                list_of_schedules.append(c)

            for i, schedule in enumerate(list_of_schedules):
                if schedule > c:
                    list_of_schedules.insert(i, c)
                    break

    temp = temp * (1 - temp_decrease)