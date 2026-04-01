from collections import deque

computer = int(input())
couple = int(input())

n = 0 # 최종 개수
visited = [False] * (computer+1) # 0~computer까지 있음


# BFS
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)


graph = [[] for _ in range(computer+1)]

for _ in range(couple):
    a, b = map(int, input().split())
    # 서로 연결
    graph[a].append(b)
    graph[b].append(a) 

bfs(1)

for i in range(len(visited)):
    if i!= 1 and visited[i]:
        n += 1

print(n)