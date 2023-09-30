def solution(name, yearning, photo):
    result = []
    dic = dict(zip(name, yearning)) 
    
    for i in range(len(photo)):
        s = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dic:  
                s += dic[photo[i][j]]
            else:
                continue
        result.append(s)

    return result


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))
