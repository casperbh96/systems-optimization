import xml.etree.ElementTree as ET

class XMLFormatter():
    def __init__(self):
        pass

    def write_schedule_xml(self, schedule, filename):
        solution = self.__newElement(tag='Solution', text='\n\t')
        for core in schedule.cores:
            for task in core.tasks:
                taskElem =  self.__newSubElement(parent=solution, tag='Task', tail='\n\t', attribs={'Id':task.id, 'MCP':core.MCPId, 'Core':core.id, 'WCRT':str(task.wcrt)})
        count = 0
        for elem in solution:
            count +=1
        solution[count-1].tail = '\n'
        ET.ElementTree(solution).write(filename)
        comment = '\n<!-- Total Laxity: ' + str(schedule.laxity) + ' -->'
        file = open(filename, 'a')
        file.write(comment)
        file.close()

    def __newElement(self, tag, text='', tail='', attribs={}):
        elem = ET.Element(tag, attribs)
        elem.text = text
        elem.tail = tail
        return elem

    def __newSubElement(self, parent, tag, text='', tail='', attribs={}):
        subElem = ET.SubElement(parent, tag, attribs)
        subElem.text = text
        subElem.tail = tail
        return subElem
