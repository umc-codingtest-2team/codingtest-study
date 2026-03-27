def solution(arr):
    answer = []

    for i in range(len(arr)):

        # answer 배열이 비어있을 때
        if len(answer) == 0:
            answer.append(arr[i])
            continue # 다음 턴으로 (i=1)
        
        # 중복되면 빼기
        if answer[-1] == arr[i]:
            continue
        
        # 안 중복되면 넣기
        answer.append(arr[i])

    return answer