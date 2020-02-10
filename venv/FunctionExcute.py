def run_function(func_name,*arg,**kwargs):
    exec(open('Library/'+func_name+'.py').read())
    return