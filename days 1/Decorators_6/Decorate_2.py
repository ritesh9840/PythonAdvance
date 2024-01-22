def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat_n_times(3)
def say_hello():
    print("Hello!")


# Calling the decorated function
say_hello()
