#concept: decoratoris a python feature that
#lets you modify a function using @symbol
def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("hello")
say_hello()