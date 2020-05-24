import pytest
from src import temp


def test_fizzbuzz():
    assert temp.fizzbuzz(1) == '1'
    assert temp.fizzbuzz(2) == '2'
    assert temp.fizzbuzz(3) == 'Fizz'
    assert temp.fizzbuzz(4) == '4'
    assert temp.fizzbuzz(5) == 'Buzz'
    assert temp.fizzbuzz(6) == 'Fizz'
    assert temp.fizzbuzz(7) == '7'
    assert temp.fizzbuzz(8) == '8'
    assert temp.fizzbuzz(9) == 'Fizz'
    assert temp.fizzbuzz(10) == 'Buzz'
    assert temp.fizzbuzz(15) == 'FizzBuzz'
    assert temp.fizzbuzz(30) == 'FizzBuzz'


if __name__ == '__main__':
    pytest.main(['-v', __file__])
