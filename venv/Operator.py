class Operator(object):
    operator_dict = {
        "=": "number_equal",
        ">": "number_higher",
        "<": "number_lower",
        ">=": "number_not_lower",
        "<=": "number_not_higher",
        "equal": "string_equal",
        "not equal": "string_not_equal",
    }
    def __init__(self,left,right,operator):
        self.left = left
        self.right = right
        self.operator = operator

    def expresstion_result(self):
        method = getattr(self, self.operator_dict.get(self.operator), lambda: "Invalid")
        return method(self.left,self.right)

    def get(self,argument):
        self.operator_dict.get(argument)

    def number_equal(self,left,right):
        return True if int(left) == int(right) else False

    def number_higher(self,left,right):
        return True if int(left) > int(right) else False

