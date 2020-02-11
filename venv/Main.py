import VariableList as variablelist
import Variable as variable
import Script as script
import NodeBase as nodebase
import NodeGroup as nodegroup
import IfNode as ifnode
import ForNode as fornode
import AssignNode as assnode
import BreakNode as breaknode
import Expresstion as exp

if __name__ == '__main__':
    variable_list = variablelist.VariableList()
    ui_variable = [
        ["url","","http://gmail.com"],
        ["url2","","facebook.com"],
        ["xpath","","//*[@id=\"identifierId\"]"],
        ["gmail","","wingchaos2012@gmail.com"],
        ["counter","","1"],
        ["message","","Hello world"],
        ["driver","",""]
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
    objExp = exp.Expresstion("3","2",'>')
    #print(objScript.type)
    # objAssignNode = assnode.AssignNode("counter","8")
    objNodeGroup = nodegroup.NodeGroup("group1")
    objNodeGroup2 = nodegroup.NodeGroup("group2")
    # objBreakNode = breaknode.BreakNode()

    objNodeBase = nodebase.NodeBase("nodebase1","test_func1")
    objNodeBase2 = nodebase.NodeBase("nodebase2", "test_func2")
    #objNodeBase2 = nodebase.NodeBase("nodebase2","count_up")

    # objNodeBase2 = nodebase.NodeBase("nodebase1", "test_func2")
    objNodeGroup.__additem__(objNodeBase)
    #objNodeGroup.__additem__(objNodeBase2)
    objNodeGroup2.__additem__(objNodeBase2)
    # objNodeGroup2.__additem__(objNodeBase)
    objIfNode = ifnode.IfNode(objExp,objNodeGroup,objNodeGroup2)
    #objForNode = fornode.ForNode(variable_list.get_init_value("counter"),"4","1",objNodeGroup)

    #print objIfNode.test_expresstion()
    # objScript.__additem__(objNodeBase)
    # objScript.__additem__(objNodeBase2)
    objScript.__additem__(objIfNode)
    objScript.__run__()
    #print()





