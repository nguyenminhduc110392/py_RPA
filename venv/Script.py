import NodeBase as nb
import NodeGroup as ng

class Script(object):
    type = "script"
    node_list = []
    def __init__(self):
        pass

    def __getnodelist__(self):
        return self.node_list

    def __additem__(self, element):
        return self.node_list.append(element)

    def __getitem__(self, index):
        return self.node_list.__getitem__(index)

    def __getleng__(self):
        return self.node_list.__len__()

    def __run__(self):
        for i in range(self.node_list.__len__()):
            self.node_list.__getitem__(i).run_node()
        return

