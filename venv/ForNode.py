import NodeGroup as node_group
class ForNode(object):
    def __init__(self,start,stop,step,for_group):
        self.start = start
        self.stop = stop
        self.step = step
        self.for_group = for_group

    def run_node(self):
        done_code = False
        for i in range(int(self.start),int(self.stop),int(self.step)):
            done_code = node_group.NodeGroup.run_node(self.for_group)
        while (done_code):
             break