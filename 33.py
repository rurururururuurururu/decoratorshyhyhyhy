def hs(func):
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs))
    return wrapper

@hs
def add(a, b):
    return a + b

result = add(3, 3)
print(result)