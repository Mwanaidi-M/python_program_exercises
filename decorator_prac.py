def my_decorator(func):
    """This is a decorator function i.e. a function that adds new functionality to a function that is paased as an arg.
       it's  like adding chocolate sprinkles to an ice cream.
    Args:
        a function: func
    """
    # the decorator has a nested function 'inner_func' and it calls the function 'func' inside it then add new functionality.
    # you can also add new functionality then call the function.
    # if the function has any params, then the inner function as well MUST have the same number and type of params.
    # but when returning the nested function in the decorator you dont have to add the params, just call the function name as is.
    def inner_func(name):
        func(name)
        print(f'{name} just got some sprinkles')

    return inner_func

    # nested function without params
    ''' 
    def inner_func():
        func()
        print(f'This function just got some sprinkles')

    return inner_func
    '''

# calling the decorator; @decorator_name 
# have this decorator above the function you want the decorator to apply to. 
@my_decorator
def my_function(name):
    print(f'{name} is just an old function')

# function without params
'''
@my_decorator
def my_function():
    print(f'I\'m is just an old function')
'''

# calling the function without params.
# sam = my_function()

sam = my_function('James')

sam