def solution(s, skip, index):
    answer = ''
    a = "abcdefghijklmnopqrstuvwxyz"
    a = sorted(set(a) - set(skip))
    print(a)

    for i in s :
        answer += a[(a.index(i) + index) % len(a)]

    return answer

print(solution("aukks", "wbqd", 5))
