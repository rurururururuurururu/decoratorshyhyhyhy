class Decorator:

    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Выполняется функция по выводу имени, подождите")

            return func(*args, **kwargs)

        return wrapper


    @decorator
    def greet(name):
        print(f"Привет, {name}!")


    greet("Алексей")
