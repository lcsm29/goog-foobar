'''
Commander Lambda is all about efficiency, including using her bunny prisoners for manual labor. 
But no one's been properly monitoring the labor shifts for a while, and they've gotten quite mixed up.
You've been given the task of fixing them, but after you wrote up new shifts, 
you realized that some prisoners had been transferred to a different block 
and aren't available for their assigned shifts. And manually sorting through each shift list 
to compare against prisoner block lists will take forever - remember, Commander Lambda loves efficiency!

Given two almost identical lists of prisoner IDs x and y where one of the lists contains an additional ID, 
write a function solution(x, y) that compares the lists and returns the additional ID.

For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], the function solution(x, y) 
would return 6 because the list x contains the integer 6 and the list y doesn't. 
Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], 
the function solution(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.

In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 
but never more than 99, and one of the lists will contain an additional unique integer which should be 
returned by the function.  The same n non-unique integers will be present on both lists, 
but they might appear in a different order, like in the examples above. 
Commander Lambda likes to keep her numbers short, so every prisoner ID will be between -1000 and 1000.
'''
def solution(x, y):
    x, y = set(x), set(y)
    for n in x:
        if n not in y:
            return n
    for n in y:
        if n not in x:
            return n

if __name__ == '__main__':
    from time import perf_counter_ns
    basic_tests = (
        ([13, 5, 6, 2, 5], [5, 2, 5, 13], 6),
        ([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50], -4)
    )
    additional_tests = (
    )
    results = {}
    for func in [func for func in dir() if func.startswith('solution')]:
        results[func] = []
        for test in basic_tests + additional_tests:
            x, y, expected = test
            start = perf_counter_ns()
            result = globals()[func](x, y)
            end = perf_counter_ns()
            results[func].append(end - start)
            print(f'{func}({x, y}) returned {result} '
                  f'({"correct" if result == expected else f"expected: {expected}"})'
                  f' in {end - start:,} nanoseconds.')
