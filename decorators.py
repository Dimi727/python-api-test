import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("im here")
        func()
        print("now there")
    return function_that_runs_func


@my_decorator
def my_function():
    print("im the function now!")

print(my_function())

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func2():
            print("Dies")
            if number == 4:
                print("bestanden")
            else:
                func()
            print("vorbei")
        return function_that_runs_func2
    return my_decorator

@decorator_with_arguments(20)
def my_function_too():
    return 1+1

print(my_function_too)


def decorator_with_arguments(number):
    def my_decorator2(func):
        @functools.wraps(func)
        def functions_that_runs_func(*args, **kwargs):
            print("in the decorator!")
            if number == 100:
                print("permission")    
            else:
                func(*args, **kwargs)
            print("after decorator")
        return functions_that_runs_func
    return my_decorator2

@decorator_with_arguments(57)
def my_function_too(x,y):
    print(x+y)

my_function_too(100,100) 