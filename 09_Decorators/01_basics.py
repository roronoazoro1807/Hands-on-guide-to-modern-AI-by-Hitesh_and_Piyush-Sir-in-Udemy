from functools import wraps


def my_decorator(func):
    @wraps(func)  # preserves original function info
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper


@my_decorator
def greet():
    print("Siuuuuuuu from Krishna Ronaldo")


greet()
print(greet.__name__)
