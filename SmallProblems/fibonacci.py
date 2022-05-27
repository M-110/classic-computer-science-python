from typing import Dict, Callable, List, Tuple
from timeit import timeit
from functools import lru_cache
import matplotlib.pyplot as plt


# A simple recursive fibonacci sequence. Not very efficient.
def fib(n: int) -> int:
    """Calculate the nth fibonacci number."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# A more efficient function using a cache.

cache: Dict[int, int] = dict()


def cached_fib(n: int) -> int:
    """Calculate the nth fibonacci number.
    
    Store previous results in a cache.
    """
    if n not in cache:
        if n < 2:
            cache[n] = n
        else:
            cache[n] = cached_fib(n - 1) + cached_fib(n - 2)
    return cache[n]


# Using the functools decorator lru_cache:

@lru_cache(maxsize=None)
def lru_cached_fib(n: int) -> int:
    """Calculate the nth fibonacci number."""
    if n < 2:
        return n
    return lru_cached_fib(n - 1) + lru_cached_fib(n - 2)


# Using an iterative approach.


def iterative_fib(n: int) -> int:
    """Calculate the nth fibonacci number.
    
    Uses iteration to continually add to the fibonacci number"""
    if n == 0:
        return 0

    fib_0: int = 0
    fib_1: int = 1

    for _ in range(1, n):
        (fib_0), (fib_1) = fib_1, (fib_0 + fib_1)
    return fib_1


def fib_generator():
    """Generates next number in the fibonacci sequence"""
    yield 0
    yield 1
    a, b = yield 1
    while True:
        a, b = yield a + b


def fib_from_generator(n):
    """Convoluted way of using a generator to iteratively calculate the fibonacci sequence."""
    gen = fib_generator()
    a, b = 0, next(gen)
    for i in range(n):
        a, b = b, gen.send((a, b))
    return b


MOD = 1000000007


def fast_doubling_fib(n: int, result: Tuple[int, int] or None = None) -> Tuple[int, int]:
    """Fast doubling method for the fib sequence.
    
    Based on method from https://www.geeksforgeeks.org/fast-doubling-method-to-find-the-nth-fibonacci-number/
    """
    if result is None:
        result = 0, 0
    if n == 0:
        return 0, 1
    result: Tuple[int, int] = fast_doubling_fib((n // 2), result)

    a, b = result

    c: int = 2 * b - a

    if c < 0:
        c += MOD

    c = (a * c) % MOD

    d: int = (a * a + b * b) % MOD

    if n % 2 == 0:
        return c, d
    else:
        return d, c + d


def test_times(n: int, fib_func: Callable) -> List[int]:
    """Creates an array of times it takes to run the function from 0 to n"""
    times: List[int] = []
    for i in range(n):
        times.append(timeit(f'globals()["cache"] = dict(); lru_cached_fib.cache_clear(); {fib_func.__name__}({i});',
                            number=10, globals=globals()) / 10)
    return times


# The graph shows the times for each of the 3 approaches.
# Iterative is clearly the fastest.
# But if you were going to repeatedly calculate various fibonacci numbers
# then the cached versions would certainly be faster.
#
# The fast doubling method I found online is the fastest.


if __name__ == "__main__":
    x_range = 300
    cached_results: List[int] = test_times(x_range, cached_fib)
    lru_cached_results: List[int] = test_times(x_range, lru_cached_fib)
    iterative_results: List[int] = test_times(x_range, iterative_fib)
    generator_results: List[int] = test_times(x_range, fib_from_generator)
    fast_doubling_results: List[int] = test_times(x_range, fast_doubling_fib)

    plt.plot(cached_results, label='cached')
    plt.plot(lru_cached_results, label='lru_cached')
    plt.plot(iterative_results, label='iterative')
    plt.plot(generator_results, label='generator')
    plt.plot(fast_doubling_results, label='fast doubling')
    plt.legend()
    plt.title('Speed of various fibonacci algorithms')
    plt.xlabel(xlabel='n')
    plt.ylabel(ylabel='seconds')
