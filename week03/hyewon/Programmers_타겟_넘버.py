def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        nonlocal answer

        # 종료 조건
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return

        # 현재 숫자를 + 하는 경우
        dfs(index + 1, current_sum + numbers[index])

        # 현재 숫자를 - 하는 경우
        dfs(index + 1, current_sum - numbers[index])

    dfs(0, 0)

    return answer