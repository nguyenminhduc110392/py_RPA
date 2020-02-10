class VariableList(object):
    def __init__(self,var_list=[]):
        self.var_list = var_list
        pass

    def __additem__(self,element):
        return self.var_list.append(element)

    def __adduniqueitem__(self,element):
        self.var_list.append(element)
        var_list = []
        for i in range(self.var_list.__len__()):
            var_list.append(self.var_list.__getitem__(i))
        var_list = list(set(var_list))
        new_var_list = VariableList()
        for i in range(len(var_list)):
            new_var_list.__additem__(var_list.__getitem__(i))
        return new_var_list

    def __getleng__(self):
        return self.var_list.__len__()

    def __getitem__(self, key):
        return self.var_list.__getitem__(key)

    def __setitem__(self, key):
        return self.var_list.__setitem__(key)

    def __delitem__(self, name):
        var_list = []
        for i in range(self.var_list.__len__()):
            var_list.append(self.var_list.__getitem__(i))
        var_name = [var_list[i].get_name() for i in range(var_list.__len__())]
        return self.var_list.__delitem__(var_name.index(name))

    def get_init_value(self, name):
        var_list = []
        for i in range(self.var_list.__len__()):
            var_list.append(self.var_list.__getitem__(i))
        var_name = [var_list[i].get_name() for i in range(var_list.__len__())]
        return self.var_list.__getitem__(var_name.index(name)).get_init_value()

    def get_cur_value(self, name):
        var_list = []
        for i in range(self.var_list.__len__()):
            var_list.append(self.var_list.__getitem__(i))
        var_name = [var_list[i].get_name() for i in range(var_list.__len__())]
        return self.var_list.__getitem__(var_name.index(name)).get_cur_value()

    def get_item(self, name):
        var_list = []
        for i in range(self.var_list.__len__()):
            var_list.append(self.var_list.__getitem__(i))
        var_name = [var_list[i].get_name() for i in range(var_list.__len__())]
        return self.var_list.__getitem__(var_name.index(name))
