import NodeGroup as node_group
import Expresstion as exp
class WhileNode(object):
    def __init__(self,expresstion,if_group,else_group):
        self.expresstion = expresstion
        self.if_group = if_group
        self.else_group = else_group

    def run_node(self):
        while (exp.Expresstion.run_node(self.expresstion)):
            node_group.NodeGroup.run_node(self.if_group)
        else:
            node_group.NodeGroup.run_node(self.else_group)
