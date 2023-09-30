def solution(s):
    a, b = 0 ,0

    while s != '1':
        a += 1
        n = s.count('1')
        b += len(s) - n
        s = bin(n)[2:]
        
    return [a, b]

print(solution("01110"))
