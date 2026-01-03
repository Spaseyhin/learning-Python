def multiply_numbers_from_range(num_1: int, num_2: int) -> int:
    i = num_1
    result = 1
    while i <= num_2:
        result = result * i

        i = i + 1
    return result


print(multiply_numbers_from_range(2, 5))