num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def linear_lookup(
    numbers: list[int],
    selected_num: int,
) -> tuple[int | None, int]:
    searches = 0
    for number in numbers:
        searches += 1
        if number == selected_num:
            return number, searches
    return None, searches


def binary_search(
    numbers: list[int],
    selected_num: int,
) -> tuple[int | None, int]:
    low = 0
    high = len(numbers) - 1
    searches = 0
    while low <= high:
        mid = (low + high) // 2
        searches += 1
        if numbers[mid] == selected_num:
            return selected_num, searches
        elif numbers[mid] > selected_num:
            high = mid - 1
        else:
            low = mid + 1
    return None, searches


def selection_sort_by_total(numbers: list[int]) -> tuple[list[int], int]:
    remaining = numbers
    result: list[int] = []
    pairings = 0
    while remaining:
        smallest = remaining[0]
        for i in range(1, len(remaining)):
            pairings += 1
            if remaining[i] < smallest:  # noqa: PLR1730
                smallest = remaining[i]
        result.append(smallest)
        remaining.remove(smallest)
    return result, pairings


mult_array = [1, 10, 100]


print(f"{'n':>10} | {'linear_lookup':>10} | {'binary_sort':>10} | {'selection':>15}")

for i in mult_array:
    _, func_one = linear_lookup(num_list * i, 10)
    _, func_two = binary_search(num_list * i, 10)
    a, func_three = selection_sort_by_total(num_list * i)
    print(f"{i * 10:>10} | {func_one:>10} | {func_two:>10} | {func_three:>15}")
