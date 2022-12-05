import random 
import math

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Dzielisz przed 0"

def factorial(a):
    result = 1
    for i in range(1, a+1):
        result = result * i
    return result


def test_add():
    '''Test dodawania'''
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert mul(a,b) == a*b

def test_div():
    '''Test dzielenia'''
    a = random.randint(1,100)
    b = random.randint(1,100)
    assert div(a,b) == a/b

def test_div2():
    '''Test dzielenia przez 0'''
    a = random.randint(1,100)
    b = 0
    assert div(a,b) == "Dzielisz przed 0"

def test_factorial():
    '''Test liczenia silni'''
    a = random.randint(1,100)
    assert factorial(a) == math.factorial(a)

def test_factorial2():
    '''Test liczenia silni z 0'''
    a = 0
    assert factorial(a) == math.factorial(a)


if __name__ == '__main__':
    test_add()
    test_div()
    test_div2()
    test_factorial()
    test_factorial2()