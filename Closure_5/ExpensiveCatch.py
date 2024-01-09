def expensive_operation(x):
    cache = {}
    if x in cache:
        # If result is already in the cache, return it
        return cache[x]
    else:
        # Perform the expensive computation
        result = x ** 2
        # Store the result in the cache for future use
        cache[x] = result
        return result


# Example usage
print(expensive_operation(3))  # This will compute and cache the result
print(expensive_operation(3))  # This will retrieve the result from the cache
