import xmltodict

class DataLoader():
    def __init__(self):
        pass

    def load_xml_by_name(self, case_name: str) -> dict:
        file_path = f'./test_cases/{case_name}.xml'

        with open(file_path, 'r') as file:
            data = file.read()
            dictionary = xmltodict.parse(data)
            return dotdict(dictionary)

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__