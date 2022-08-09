# 처음 풀이 (효율성X)
'''
def solution(n):
    answer = 0

    for i in range(2, n+1):
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            answer += 1        
    return answer

print(solution(5))
'''

# 구글 참고 (에라토스테네스의 체 공식!)

def solution(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num: 
            num -= set(range(2*i, n+1, i))
                    
    return len(num)

print(solution(5))
