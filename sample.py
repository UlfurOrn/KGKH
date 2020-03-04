def fizzbuzz(num):
    is_div_5 = num % 5 == 0
    is_div_3 = num % 3 == 0

    if is_div_5 and is_div_3:
        return "FizzBuzz"
    
    elif is_div_5:
        return "Buzz"

    elif is_div_3:
        return "Fizz"
    
    return num