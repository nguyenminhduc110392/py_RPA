import VariableList as variablelist
import Variable as variable
variable_list = variablelist.VariableList()


greetdy = variable_list.get_init_value("message")
variable_list.get_item("message").set_cur_value("Hi World")
