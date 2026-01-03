def join_numbers_from_range(num_1: int, num_2: int) -> str:
    i = num_1
    line = ''
    while i <= num_2:
        line = line + str(i)
        i = i + 1
    return line 
