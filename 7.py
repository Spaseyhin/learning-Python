def is_leap_year(year: float) -> bool:
    return (year % 4) == 0 and (year % 100) != 0

print(is_leap_year(2016))  # => True