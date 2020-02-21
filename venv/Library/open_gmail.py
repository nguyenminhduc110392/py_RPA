from selenium import webdriver
import VariableList as variablelist
import Variable as variable
variable_list = variablelist.VariableList()

driver = variable_list.get_cur_value("driver")
driver.get(variable_list.get_init_value("url"))