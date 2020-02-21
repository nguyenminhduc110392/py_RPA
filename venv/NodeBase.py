#import FunctionExcute as functionexcute
from FunctionExcute import run_function

class NodeBase(object):
    type = "node_base"
    def __init__(self,node_name,function_name):
        self.name = node_name
        self.function = function_name

    def __getname__(self):
        return self.name

    def __getfunction__(self):
        return self.function

    def __gettype__(self):
        return self.type

    def __setname__(self,name):
        self.name = name
        return

    def __setfunction__(self,function):
        self.function = function
        return

    def __settype__(self,type):
        self.type = type
        return

    def run_node(self):
        run_function(self.function)

    def load_properties_list(self):
        return {'Name': self.name,'Function': self.function}