def solution(M, F):
    bombs = [int(M), int(F)]
    g = 0
    while bombs[0] - bombs[1]:
        bombs.sort()
        diff = bombs[1] - bombs[0]
        q, r = divmod(diff, bombs[0])
        g += q + (r > 0)
        bombs[1] -= (q + (r > 0)) * bombs[0]
    return str(g) if bombs == [1, 1] else 'impossible'

'''removed due to slow speed
def solution_brute(M, F):
    bombs = [int(M), int(F)]
    g = 0
    while bombs[0] - bombs[1]:
        bombs.sort()
        bombs[1] = bombs[1] - bombs[0]
        g += 1
    return str(g) if bombs == [1, 1] else 'impossible'
'''

if __name__ == '__main__':
    from time import perf_counter_ns
    basic_tests = (
        ('2', '1', '1'),
        ('4', '7', '4')
    )
    additional_tests = (
        ('498454011879264', '308061521170129', '70'),
        ('9366947731425726508977331996039353971111632790877', '5789092068864820527338372482892113982249794889765', '234'),
        ('1', str(10**50), str(10**50 - 1))
    )
    results = {}
    num_iters = 1
    for func in [func for func in dir() if func.startswith('solution')]:
        results[func] = []
        print(f'\n{func}() (Number of Iterations {num_iters:,})')
        for test in basic_tests + additional_tests:
            M, F, expected = test
            start = perf_counter_ns()
            for i in range(num_iters):
                result = globals()[func](M, F)
            end = perf_counter_ns()
            results[func].append(end - start)
            print(f'{func}("{M}", "{F}") returned {result} '
                  f'({"correct" if result == expected else f"expected: {expected}"})'
                  f' in {end - start:,} nanoseconds.')
