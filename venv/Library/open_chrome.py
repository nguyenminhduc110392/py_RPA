from selenium import webdriver
import VariableList as variablelist
import Variable as variable
variable_list = variablelist.VariableList()

driver = webdriver.Chrome()
variable_list.get_item("driver").set_cur_value(driver)
