def solution(x, y):
    for a, b in zip(x, y):
        if a not in y: return a
        if b not in x: return b
