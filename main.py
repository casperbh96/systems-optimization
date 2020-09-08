from data_loader import DataLoader

loader = DataLoader()

data = loader.load_xml_by_name('small')
print(data['Model'])
