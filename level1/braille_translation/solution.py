def solution(s):
    return ''.join('000001' + braille[c.lower()] if c.isupper() else braille[c] for c in s)


braille = {
    'a': '100000', 'b': '110000', 'c': '100100', 'd': '100110',
    'e': '100010', 'f': '110100', 'g': '110110', 'h': '110010',
    'i': '010100', 'j': '010110', 'k': '101000', 'l': '111000',
    'm': '101100', 'n': '101110', 'o': '101010', 'p': '111100',
    'q': '111110', 'r': '111010', 's': '011100', 't': '011110',
    'u': '101001', 'v': '111001', 'w': '010111', 'x': '101101',
    'y': '101111', 'z': '101011', ' ': '000000'
}


def solution_dict(word):
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for c in word:
        if c in caps:
            answer += '000001'
            c = c.lower()
        answer += braille_dict[c]
    return answer


def solution_short_dict(word):
    return ''.join('000001' + braille_dict[c.lower()] if c.isupper() else braille_dict[c] for c in word)


def solution_tuple(word):
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for c in word:
        if c == ' ':
            answer += '000000'
            continue
        if c in caps:
            answer += '000001'
            c = c.lower()
        answer += braille_tuple[ord(c) - 97]
    return answer


def solution_index(word):
    answer = ''
    for c in word:
        if c == ' ':
            answer += '000000'
            continue
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            answer += '000001'
            c = c.lower()
        answer += braille_list_wo_space[ord(c) - 97]
    return answer


def solution_short_index(word):
    return ''.join('000001' + braille_list[ord(c) - 65] if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else braille_list[ord(c)] if c == ' ' else braille_list[ord(c) - 97] for c in word)


braille_dict = {
    'a': '100000', 'b': '110000', 'c': '100100', 'd': '100110',
    'e': '100010', 'f': '110100', 'g': '110110', 'h': '110010',
    'i': '010100', 'j': '010110', 'k': '101000', 'l': '111000',
    'm': '101100', 'n': '101110', 'o': '101010', 'p': '111100',
    'q': '111110', 'r': '111010', 's': '011100', 't': '011110',
    'u': '101001', 'v': '111001', 'w': '010111', 'x': '101101',
    'y': '101111', 'z': '101011', ' ': '000000'
}
braille_tuple = (
    '100000', '110000', '100100', '100110', '100010', '110100', '110110', 
    '110010', '010100', '010110', '101000', '111000', '101100', '101110', 
    '101010', '111100', '111110', '111010', '011100', '011110', '101001', 
    '111001', '010111', '101101', '101111', '101011'
)
braille_list_wo_space = '100000 110000 100100 100110 100010 110100 110110 110010 010100 010110 101000 111000 101100 101110 101010 111100 111110 111010 011100 011110 101001 111001 010111 101101 101111 101011'.split()
braille_list = '100000 110000 100100 100110 100010 110100 110110 110010 010100 010110 101000 111000 101100 101110 101010 111100 111110 111010 011100 011110 101001 111001 010111 101101 101111 101011 0 0 0 0 0 0 000000'.split()


if __name__ == '__main__':
    from time import perf_counter_ns
    basic_tests = (
        ('code', '100100101010100110100010'),
        ('Braille', '000001110000111010100000010100111000111000100010'),
        ('The quick brown fox jumps over the lazy dog', '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'),
    )
    additional_tests = (
    )
    results = {}
    num_iters = 10_000
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
