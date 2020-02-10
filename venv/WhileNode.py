import NodeGroup as node_group
class WhileNode(object):
    def __init__(self,expresstion,if_group,else_group):
        self.expresstion = expresstion
        self.if_group = if_group
        self.else_group = else_group

    def run_node(self):
        done_code = False
        while (eval(self.expresstion)):
            done_code = node_group.NodeGroup.run_node(self.if_group)
        else:
            done_code= node_group.NodeGroup.run_node(self.else_group)

        #while (done_code):
        #    break