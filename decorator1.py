def fib(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


fib_cache = {0: 0, 1: 1}


def fib_with_cache(n):
    if n in fib_cache:
        return fib_cache[n]
    elif n < 0:
        rslt = -1
    else:
        rslt = fib_with_cache(n - 1) + fib_with_cache(n - 2)
    fib_cache[n] = rslt
    return rslt


def fib_with_cache_and_debug(n):
    print(f"Calling fib({n})")
    if n in fib_cache:
        rslt = fib_cache[n]
    elif n < 0:
        rslt = -1
    else:
        rslt = fib_with_cache_and_debug(n - 1) + fib_with_cache_and_debug(n - 2)
    fib_cache[n] = rslt
    print(f"'fib({n})' returned {rslt}")
    return rslt


if __name__ == "__main__":
    print(fib_with_cache_and_debug(5))