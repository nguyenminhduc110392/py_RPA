import VariableList as variablelist
import Variable as variable
import Script as script
import NodeBase as nodebase
import NodeGroup as nodegroup

if __name__ == '__main__':
    variable_list = variablelist.VariableList()
    ui_variable = [
        ["url","","google.com"],
        ["url2","","facebook.com"],
        ["xpath","","//*[@id=\"identifierId\"]"],
        ["gmail","","wingchaos2012@gmail.com"]
    ]
    ui_action = [
        []
    ]
    for var in ui_variable:
        variable_list.__adduniqueitem__(variable.Variable(var[0], var[1], var[2]))
    #print(variable_list[1].__getattribute__("name"))
    #print(variable_list.get_init_value("xpath"))
    #variable_list.get_cur_value("url")
    objScript = script.Script()
    objNodeGroup = nodegroup.NodeGroup("group1")
    objNodeGroup2 = nodegroup.NodeGroup("group2")
    objectNodeBase1 = nodebase.NodeBase("nodebase1","test_func1")
    objectNodeBase2 = nodebase.NodeBase("nodebase2","test_func2")
    objectNodeBase3 = nodebase.NodeBase("nodebase2", "test_func1")
    objectNodeBase4 = nodebase.NodeBase("nodebase2", "test_func2")
    objectNodeBase5 = nodebase.NodeBase("nodebase2", "test_func1")

    objNodeGroup.__additem__(objectNodeBase1)
    objNodeGroup.__additem__(objectNodeBase2)
    objNodeGroup.__additem__(objectNodeBase5)
    objNodeGroup.__additem__(objectNodeBase3)
    objNodeGroup.__additem__(objectNodeBase4)
    objScript.__additem__(objNodeGroup)
    # objScript.__additem__(objectNodeBase1)
    # objScript.__additem__(objNodeGroup2)
    # objScript.__additem__(objectNodeBase2)
    # objScript.__additem__(objNodeGroup)
    # objScript.__additem__(objectNodeBase2)
    # objScript.__additem__(objectNodeBase2)
    # objScript.__additem__(objectNodeBase2)
    # objScript.__additem__(objectNodeBase2)
    # objScript.__additem__(objectNodeBase2)
    # objScript.__additem__(objectNodeBase2)

    objScript.__run__()
    #print()





