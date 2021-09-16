def solution(data, n):  # the one that I submitted on Invitation #A3
    freq = {num: data.count(num) for num in data}
    return [num for num in data if freq[num] <= n]


def solution(data, n):  # the one that I submitted on Invitation #A4
    return [i for i in data if data.count(i) <= n]
