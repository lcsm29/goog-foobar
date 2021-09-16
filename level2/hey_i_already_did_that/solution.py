def solution(n, b):  # submitted A5
    k = len(n)
    past_nums = []
    num = n
    while 1:
        x = ''.join(str(i) for i in sorted(int(i) for i in num))
        y = x[::-1]
        z = ''
        pos = True if int(x[0]) - int(y[0]) >= 0 else False
        for i, j, l in zip(x, y, range(k)):
            tmp = int(i) - int(j) + (0 if (pos and l) or not l else -1)
            pos = True if tmp >=0 else False
            if not pos:
                tmp += b
            z += str(tmp)
        num = z[::-1]
        if num in past_nums:
            break
        past_nums.append(num)
    ans = 1
    for i in past_nums[::-1]:
        if i == num:
            break
        ans += 1
    return ans
