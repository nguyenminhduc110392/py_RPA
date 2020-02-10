#import FunctionExcute as functionexcute
from FunctionExcute import run_function

class NodeBase(object):
    def __init__(self,node_name,function_name,node_type = "node_base"):
        self.name = node_name
        self.function = function_name
        self.type = node_type

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
        done_code = False
        done_code = run_function(self.function)
        while (done_code):
            break