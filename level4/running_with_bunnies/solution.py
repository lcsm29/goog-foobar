from itertools import permutations


def solution(times, time_limit):
    time = [list(t) for t in times[:]]
    paths = lambda x: [(x[i - 1], x[i]) for i in range(1, len(x))]
    w = len(time)
    for k in range(w):
        for i in range(w):
            for j in range(w):
                if time[i][j] > time[i][k] + time[k][j]:
                    time[i][j] = time[i][k] + time[k][j]
    if any([1 for i in range(w) if time[i][i] < 0]):
        return [i for i in range(w - 2)]
    for i in range(w - 2, -1, -1):
        for p in permutations(range(1, w - 1), i):
            t = 0
            for s, e in paths([0] + list(p) + [-1]):
                t += time[s][e]
            if t <= time_limit:
                return sorted([i - 1 for i in p])


if __name__ == '__main__':
    from time import perf_counter_ns
    basic_tests = (
        (((  0,  1,  1,  1,  1), (  1,  0,  1,  1,  1), (  1,  1,  0,  1,  1), (  1,  1,  1,  0,  1), (  1,  1,  1,  1,  0)), 3, [0, 1]),
        (((  0,  2,  2,  2, -1), (  9,  0,  2,  2, -1), (  9,  3,  0,  2, -1), (  9,  3,  2,  0, -1), (  9,  3,  2,  2,  0)), 1, [1, 2])
    )
    additional_tests = (
    )
    results = {}
    num_iters = 1
    for func in [func for func in dir() if func.startswith('solution')]:
        results[func] = []
        print(f'\n{func}() (Number of Iterations {num_iters:,})')
        for test in basic_tests + additional_tests:
            times, limit, expected = test
            times = [list(time) for time in times[:]]
            start = perf_counter_ns()
            for i in range(num_iters):
                result = globals()[func](times, limit)
            end = perf_counter_ns()
            results[func].append(end - start)
            print(f'{func}({times if len(times) < 6 else "truncated due to length: " + str(len(times))}) returned {result} '
                  f'({"correct" if result == expected else f"expected: {expected}"})'
                  f' in {end - start:,} nanoseconds.')
