#coding=utf-8;
g = False;
def print_func( par ):
    globals()['g'] = True;
    print 'Hello: ', par;
    return;

def sum_func( arg1, arg2 ):
    if globals()['g'] == False:
        return 0;
    else:
        return arg1 + arg2;