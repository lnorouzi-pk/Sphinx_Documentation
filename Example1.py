def func1(arg1,arg2):
    '''
    This function takes 2 arguments , sets the first equal to the second and returns the first argument. Pointless

    :param arg1: Some value
    :param arg2: Another Value

    :return: Return the first value
    '''
    arg1 = arg2
    return arg1

def func2():
    '''

    Function with no arguments return
    prints hello

    :return: None

    '''
    print('hellooo')
    pass
x=0
y=1
print(func1(x,y))