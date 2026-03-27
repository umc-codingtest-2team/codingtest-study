n = int(input())
arr = list(map(int, input().split()))

print(*arr[::-1]) 
# *를 안 빼면 리스트 형태로 출력됨