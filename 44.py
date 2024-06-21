def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

divide(10, 0)