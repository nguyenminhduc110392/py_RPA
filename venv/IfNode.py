import NodeGroup as node_group
class IfNode(object):
    def __init__(self,expresstion,if_group,else_group):
        self.else_group = else_group
        self.if_group = if_group
        self.expresstion = expresstion

    def test_expresstion(self):
        return eval(self.expresstion)

    def set_if_group(self,if_group):
        self.if_group = if_group

    def set_expresstion(self,expresstion):
        self.expresstion = expresstion

    def set_else_group(self,else_group):
        self.else_group = else_group

    def run_node(self):
        done_code = False
        done_code = node_group.NodeGroup.run_node(self.if_group) if eval(self.expresstion) == True else node_group.NodeGroup.run_node(self.else_group)
        while (done_code):
            break
