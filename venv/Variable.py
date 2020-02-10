class Variable(object):
    def __init__(self, var_name, cur_value, init_value):
        self.name = var_name
        self.cur_value = cur_value
        self.init_value = init_value

    def get_name(self):
        return self.name

    def get_cur_value(self):
        return self.cur_value

    def get_init_value(self):
        return self.init_value

    def set_name(self,name):
        self.name = name

    def set_cur_value(self,cur_value):
        self.cur_value = cur_value

    def set_init_value(self,init_value):
        self.init_value = init_value