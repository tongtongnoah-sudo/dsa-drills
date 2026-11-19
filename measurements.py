import timeit
from collections.abc import Callable

import matplotlib.pyplot as plt  # type: ignore

arr_list_one = [10, 100, 1000, 10000]
arr_list_two = [10, 50, 100]
arr_list_three = [10**6, 10**9, 10**10]


def get_first(arr: list[int]) -> int:
    """The complexity is O(1), and it runs at the same pace no matter
    what number is put in."""
    return arr[0]


def sum_list(arr: list[int]) -> int:
    """The complexity is O(n), meaning the function's execution
    time grows linearly, so it's much more efficient than a quadratic
    Big-O function."""
    return sum(arr)


def count_pairs(arr: list[int]) -> int:
    """The complexity is O(n^2), so the execution time will grow according to the
    square of the input, and this is much less efficient than a linear Big-O."""
    pairs = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                pairs += 1
    return pairs


def halve_number(n: int) -> int:
    """The complexity is O(log n), hence the function's
    execution time grows much slower than even linear Big-O functions."""
    while n != 0:
        n = n // 2
    return n


def best_time(func: Callable[[], object], number: int) -> float:
    """Seconds per call, taking the fastest of 5 runs to filter out noise."""
    runs = timeit.repeat(func, number=number, repeat=5)
    return min(runs) / number


time_func_one = []
time_func_two = []
time_func_three = []
time_func_four = []

for n in arr_list_one:
    range_arr = list(range(n))
    t = best_time(lambda: get_first(range_arr), number=1000000)  # noqa: B023
    time_func_one.append(t)

for n in arr_list_one:
    range_arr = list(range(n))
    t = best_time(lambda: sum_list(range_arr), number=10000)  # noqa: B023
    time_func_two.append(t)

for n in arr_list_two:
    range_arr = list(range(n))
    t = best_time(lambda: count_pairs(range_arr), number=1000)  # noqa: B023
    time_func_three.append(t)

for n in arr_list_three:
    t = best_time(lambda: halve_number(n), number=50000)  # noqa: B023
    time_func_four.append(t)

plt.plot(arr_list_one, time_func_one)
plt.plot(arr_list_one, time_func_two)
plt.plot(arr_list_two, time_func_three)
plt.plot(arr_list_three, time_func_four)
plt.xscale("log")
plt.yscale("log")
plt.title("Best runtime graph")
plt.xlabel("Input size")
plt.ylabel("Optimized time")
plt.savefig("growth_plot.png")
