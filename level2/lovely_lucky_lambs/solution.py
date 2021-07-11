def fib(x, a=1, b=1, counter=1):
    while x > 0:
        a, b = b, a + b
        counter += 1
        x -= a
    return counter
    

def log(x, base=2, exp=1):
    while base**exp - 1 <= x:
        exp += 1
    return exp


def solution(x):
    return fib(x) - log(x) if 0 < x < 1e9 else 0
