from collections import deque

# 입력
N, M, V = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향

# 작은 번호부터 방문하기 위해 정렬
for i in range(1, N + 1):
    graph[i].sort()


# DFS
def dfs(node):
    visited[node] = True
    print(node, end=' ')

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)


# BFS
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)


# DFS 실행
visited = [False] * (N + 1)
dfs(V)

print()

# BFS 실행 (visited 초기화)
visited = [False] * (N + 1)
bfs(V)