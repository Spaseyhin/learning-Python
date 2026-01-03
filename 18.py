def fizzbuzz(n: int) -> str:
    result = ''
    for num in range(1, n+1):
        
        if num % 3 == 0 and num % 5 == 0:
            result += "FizzBuzz"
        elif num % 3 == 0:
            result += "Fizz"
        elif num % 5 == 0:
            result += "Buzz"
        else:
             result += str(num)

        if num != n:
            result += ' '
    return result
        
print(fizzbuzz(1))
print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))