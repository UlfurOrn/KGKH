from sample import fizzbuzz

def test_return_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"


def test_return_buzz():
    assert fizzbuzz(5) == "Buzz"