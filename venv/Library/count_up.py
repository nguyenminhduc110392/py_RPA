import VariableList as variablelist
import Variable as variable
variable_list = variablelist.VariableList()

count = variable_list.get_cur_value("counter")
count = int(count)+1
variable_list.get_item("counter").set_cur_value(str(count))