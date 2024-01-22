def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            result = func(*args)
            cache[args] = result
        return cache[args]
    return wrapper

# Usage


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)

