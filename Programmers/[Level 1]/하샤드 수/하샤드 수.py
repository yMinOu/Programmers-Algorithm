def solution(num):
    answer = True
    num = str(num)
    num_list = list(num)
    
    s = 0
    for i in num_list: 
        s += int(i)
    
    if(int(num) % s == 0) :  answer = True
    else :  answer = False

    return answer


print(solution(13))
