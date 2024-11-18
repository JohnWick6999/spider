def decorative(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@decorative
def add_func(a, b):
    return a+b

print(add_func(1,2))