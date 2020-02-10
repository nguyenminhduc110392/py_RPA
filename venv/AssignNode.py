import VariableList as variablelist
import Variable as variable
class AssignNode():
    def __init__(self,name,value):
        self.name = name
        self.value = value

    def run_node(self):
        variablelist.VariableList().get_item(self.name).set_cur_value(self.value)
