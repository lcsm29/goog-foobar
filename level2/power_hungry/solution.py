def solution(xs):
    if len(xs) <= 1:
        return str(xs[0]) if len(xs) else '0'
    xs = [n for n in xs if n]
    pos, neg = [n for n in xs if n > 0], [n for n in xs if n < 0]
    if len(neg) == len(pos + neg) == 1:
        return '0'
    if len(neg) % 2 == 1:
        neg.remove(max(neg))
    prod = 1
    for n in pos + neg:
        prod *= n
    return str(prod)


if __name__ == '__main__':
    from time import perf_counter_ns
    basic_tests = (
        ([2, 0, 2, 2, 0], '8'),
        ([-2, -3, 4, -5], '60')
    )
    additional_tests = (
        ([-1], '-1'),
        ([0], '0'),
        ([1], '1'),
        ([-1, -3], '3'),
        ([-1, 0], '0'),
        ([-10, -10, -10, 20], '2000'),
        ([-10, -10, -11, 20], '2200')
    )
    results = {}
    num_iters = 1
    for func in [func for func in dir() if func.startswith('solution')]:
        results[func] = []
        print(f'\n{func}() (Number of Iterations {num_iters:,})')
        for test in basic_tests + additional_tests:
            string, expected = test
            start = perf_counter_ns()
            for i in range(num_iters):
                result = globals()[func](string)
            end = perf_counter_ns()
            results[func].append(end - start)
            print(f'{func}("{string}") returned {result} '
                  f'({"correct" if result == expected else f"expected: {expected}"})'
                  f' in {end - start:,} nanoseconds.')
