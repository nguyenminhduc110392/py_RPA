import NodeBase
class NodeGroup(object):
    def __init__(self, node_name, node_type = "node_group"):
        self.name = node_name
        self.node_list = []
        self.type = node_type
        self.accessible = True

    def __getnodelist__(self):
        return self.node_list

    def __additem__(self,element):
        return self.node_list.append(element)

    def __getleng__(self):
        return super(NodeGroup, self).__len__()

    def __getitem__(self, index):
        return super(NodeGroup, self).__getitem__(index)

    def __setitem__(self, index):
        return super(NodeGroup, self).__setitem__(index)

    def __delitem__(self, index):
        return super(NodeGroup, self).__delitem__(index)

    def insert(self, index, value):
        self._inner_list.insert(index - 1, value)

    def run_node(self):
        for i in range(self.node_list.__len__()):
            self.node_list.__getitem__(i).run_node()
        return

    def load_properties_list(self):
        return {'Name': self.name}

