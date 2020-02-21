import VariableList as variablelist
import Variable as variable


class AssignNode(object):
    type = "assign_node"

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def run_node(self):
        variablelist.VariableList().get_item(self.name).set_cur_value(self.value)

    def load_properties_list(self):
        return {"name":self.name, "value":self.value}
