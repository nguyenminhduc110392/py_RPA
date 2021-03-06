import NodeBase as nb
import NodeGroup as ng
import json

class Script(object):
    # type = "script"
    # node_list = []
    def __init__(self):
        self.node_list = []
        self.type = "script"
        pass

    def __getnodelist__(self):
        return self.node_list

    def __additem__(self, element):
        return self.node_list.append(element)

    def __getitem__(self, index):
        return self.node_list.__getitem__(index)

    def __getleng__(self):
        return self.node_list.__len__()

    def __del__(self):
        return

    def __run__(self):
        for i in range(self.node_list.__len__()):
            self.node_list.__getitem__(i).run_node()
        return

    def toJSON(self):
        print(self.__dict__)
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

