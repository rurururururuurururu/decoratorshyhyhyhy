class TwoDef:

    def twodef(func):
        def wrapper(*args, **kwargs):

            func(*args, **kwargs)

            return func(*args, **kwargs)

        return wrapper

    @twodef
    def greet(name):
        print(f"Привет, {name}!")

    greet("Алексей")