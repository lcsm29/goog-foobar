def solution(s):
    highest = 1
    for size in range(1, len(s)):
        pieces = s.count(s[:size])
        if pieces * size == len(s):
            highest = max(highest, pieces)
    return highest
