


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def succ(n):
    return n + 1

succ(10)


def new_decorator(some_arg):
    def foo(x):
        print('before calling')
        res = some_arg(x)
        print(res)
        print('after')
    return foo


@new_decorator
def func_to_decor(n):
    return n + 1

func_to_decor(2)


def new_dec(func):
    def foo(x):
        print('hello')
        res = func(x)
        print(res)
    return foo


@new_dec
def aget_dec(n):
    return 1 + n

aget_dec(4)