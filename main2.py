from modules import calculations as calc

filename = 'small.xml'
tasks, mcps = calc.load_file_as_object(filename)

temp = 10000
tempCooling = 0.003

currentSol = calc.initial_candidate2(tasks, mcps)
listOfSchedules = []

print(calc.calc_laxity(currentSol, tasks, mcps))