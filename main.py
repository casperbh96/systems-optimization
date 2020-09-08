from data_loader import DataLoader

loader = DataLoader()

# dict/dictionary == hashtable
dictionary = loader.load_xml_by_name('small')

task_df = loader.get_tasks_to_dataframe(
    dictionary['Application']['Task']
)

mcp_core_df = loader.get_mcp_to_dataframe(
    dictionary['Platform']['MCP']
)

print(mcp_core_df.head(5))