def solution(i):
    def sieve_gen(composites={}, cand=2):
        while True:
            if cand not in composites:
                composites[cand * cand] = [cand]
                yield cand
            else:
                for prime in composites[cand]:
                    composites.setdefault(prime + cand, []).append(prime)
                del composites[cand]
            cand += 1

    concatenated = ''
    for prime in sieve_gen():
        concatenated += str(prime)
        if len(concatenated) > i + 5:
            break
    return concatenated[i:i + 5]


def solution_prime_generator_separated(i):
    concatenated = ''
    for prime in prime_gen():
        concatenated += str(prime)
        if len(concatenated) > i + 5:
            break
    return concatenated[i:i + 5]


def prime_gen(composites={}, cand=2):
    while True:
        if cand not in composites:
            composites[cand * cand] = [cand]
            yield cand
        else:
            for prime in composites[cand]:
                composites.setdefault(prime + cand, []).append(prime)
            del composites[cand]
        cand += 1


def solution_brute_accumulator(i):
    s = '235711'
    cand = 11
    while len(s) < i + 5:
        cand += 2
        div, limit = 3, int(cand**0.5) + 1
        while div < limit:
            if cand % div == 0:
                break
            div += 1
        if div == limit:
            s += str(cand)
    return s[i:i + 5]


def solution_brute_generator_separated(i):
    concatenated = ''
    for prime in brute_gen():
        concatenated += str(prime)
        if len(concatenated) > i + 5:
            break
    return concatenated[i:i + 5]


def brute_gen(cand=1):
    primes=[2]
    while True:
        cand += 2
        for p in primes:
            if cand % p == 0:
                break
        else:
            yield primes[-1]
            primes.append(cand)


if __name__ == '__main__':
    from time import perf_counter_ns
    basic_tests = (
        (0, '23571'),
        (3, '71113')
    )
    additional_tests = (
        (5000, '05131'),
        (9996, '20120'),
        (10000, '02192'),
    )
    results = {}
    for func in [func for func in dir() if func.startswith('solution')]:
        results[func] = []
        for test in basic_tests + additional_tests:
            index, expected = test
            start = perf_counter_ns()
            result = globals()[func](index)
            end = perf_counter_ns()
            results[func].append(end - start)
            print(f'{func}({index}) returned {result} '
                  f'({"correct" if result == expected else f"expected: {expected}"})'
                  f' in {end - start:,} nanoseconds.')
