from lxml import objectify
from objects.AppTask import AppTask
from objects.MCP import MCP
from objects.MCPCore import MCPCore
from objects.SolTask import SolTask


def load_file_as_object(filename):
    with open('test_cases/' + filename, 'r') as file:
        xmlStr = file.read()
    model = objectify.fromstring(xmlStr)

    application = []
    for task in model.Application.Task:
        deadline = int(task.attrib['Deadline'])
        id = int(task.attrib['Id'])
        period = int(task.attrib['Period'])
        wcet = int(task.attrib['WCET'])
        appTask = AppTask(deadline, id, period, wcet)
        application.append(appTask)

    platform = []
    for mcp in model.Platform.MCP:
        id = int(mcp.attrib['Id'])
        cores = []
        for core in mcp.Core:
            coreId = int(core.attrib['Id'])
            wcetFactor = float(core.attrib['WCETFactor'])
            cores.append(MCPCore(coreId, wcetFactor))
        platform.append(MCP(id, cores))

    return application, platform


def initial_candidate2(tasks, mcps):
    solution = []
    solution.append(SolTask(tasks[0].Id, mcps[0].Id, mcps[0].Cores[0].Id, None))
    solution.append(SolTask(tasks[1].Id, mcps[0].Id, mcps[0].Cores[1].Id, None))
    solution.append(SolTask(tasks[2].Id, mcps[0].Id, mcps[0].Cores[2].Id, None))
    solution.append(SolTask(tasks[3].Id, mcps[0].Id, mcps[0].Cores[3].Id, None))
    solution.append(SolTask(tasks[4].Id, mcps[1].Id, mcps[1].Cores[0].Id, None))
    solution.append(SolTask(tasks[5].Id, mcps[1].Id, mcps[1].Cores[1].Id, None))
    solution.append(SolTask(tasks[6].Id, mcps[1].Id, mcps[1].Cores[2].Id, None))
    solution.append(SolTask(tasks[7].Id, mcps[1].Id, mcps[1].Cores[3].Id, None))
    solution.append(SolTask(tasks[8].Id, mcps[1].Id, mcps[1].Cores[2].Id, None))
    solution = calc_wcrt(solution, tasks, mcps)
    return solution


def calc_wcrt(solution, tasks, mcps):
    for solTask in solution:
        task = next((x for x in tasks if x.Id == solTask.Id), None)
        mcp = next((x for x in mcps if x.Id == solTask.MCP), None)
        core = next((x for x in mcp.Cores if x.Id == solTask.Core), None)
        interference = 0
        responseTime = interference + (task.WCET * core.WCETFactor)
        tasksOnCore = [x for x in solution if x.MCP == mcp.Id and x.Core == core.Id and not x.Id == task.Id]
        for coreTask in tasksOnCore:
            taskDetails = next((x for x in tasks if x.Id == coreTask.Id), None)
            interference += (responseTime / taskDetails.Period) * (taskDetails.WCET * core.WCETFactor)
        solTask.WCRT = interference + task.WCET
    return solution


def calc_laxity(solution, tasks, mcps):
    res = 0
    for mcp in mcps:
        for core in mcp.Cores:
            n = 0
            laxity = 0
            for task in [x for x in solution if x.MCP == mcp.Id and x.Core == core.Id]:
                taskDetails = next((x for x in tasks if x.Id == task.Id), None)
                n += 1
                laxity += taskDetails.Deadline - task.WCRT
            if n != 0:
                res += int(laxity / n)
    return laxity
