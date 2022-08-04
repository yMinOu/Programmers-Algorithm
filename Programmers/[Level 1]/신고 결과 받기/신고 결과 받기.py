def solution(id_list, report, k):
    answer = []
    # 딕셔너리로 변환
    id2_list = {string:[] for string in id_list}

    # id별 각 신고 결과
    for i in report:
        id2_list[i.split(" ")[0]].append(i.split(" ")[1])

    id3_list = {string :[] for string in id2_list}
    
    # 신고 결과 정리(곂치는 것)
    for key, values in id2_list.items():
        sort_values = sorted(values)
        for j in sort_values:
            if not id3_list[key]:
                id3_list[key].append(j)
            elif(id3_list[key][-1] == j):
                continue
            else:
                id3_list[key].append(j)
    
    # 자기가 받은 신고 수
    id2_list = {string:0 for string in id_list}

    for values in id3_list.values():
        for j in values: 
            id2_list[j] += 1

    # 결과 메일
    for key, values in id3_list.items():
        count = 0
        for i in values:
            if(id2_list[i] >= k):
                count += 1
        answer.append(count)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
