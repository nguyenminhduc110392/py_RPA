import Operator as op
class Expresstion(object):
    type = "expresstion"
    def __init__(self,left,right,operator):
        self.left = left
        self.right = right
        self.operator = operator

    def run_node(self):
        objOperator = op.Operator(self.left,self.right,self.operator)
        return objOperator.expresstion_result()

