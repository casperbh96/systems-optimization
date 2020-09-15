import xmltodict
import pandas as pd

class DataLoader():
    def __init__(self):
        pass

    def load_xml_by_name(self, case_name: str) -> dict:
        file_path = f'./test_cases/{case_name}.xml'

        # Read XML file, parse to dict, return dict
        with open(file_path, 'r') as file:
            data = file.read()
            dictionary = xmltodict.parse(data)

            return dictionary['Model']

    def get_mcp_to_dataframe(self, mcps: dict) -> pd.DataFrame:
        core_ids = []
        core_mcp_ids = []
        core_wcet_factors = []

        for mcp in mcps:
            for core in mcp['Core']:
                core_ids.append(core['@Id'])
                core_mcp_ids.append(mcp['@Id'])
                core_wcet_factors.append(core['@WCETFactor'])

        return pd.DataFrame({
            'CoreId':core_ids,
            'CoreMcpId':core_mcp_ids,
            'CoreWcetFactor':core_wcet_factors
        })

    def get_tasks_to_dataframe(self, tasks: dict) -> pd.DataFrame:
        ids = []
        deadlines = []
        periods = []
        wcets = []

        for task in tasks:
            ids.append(task['@Id'])
            deadlines.append(task['@Deadline'])
            periods.append(task['@Period'])
            wcets.append(task['@WCET'])

        return pd.DataFrame({
            'Id':ids,
            'Deadline':deadlines,
            'Period':periods,
            'WCET':wcets
        })