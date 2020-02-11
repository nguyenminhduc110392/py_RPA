class BreakNode(object):
    type = "break_node"
    def __init__(self):
        pass

    def run_node(self):
        exec('break')