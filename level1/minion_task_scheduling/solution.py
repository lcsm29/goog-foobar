def solution(data, n): 
    freq = {num: data.count(num) for num in data}
    return [num for num in data if freq[num] <= n]
