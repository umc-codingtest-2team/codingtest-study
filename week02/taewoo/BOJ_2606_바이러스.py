from collections import deque


def main():
    n = int(input())
    m = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (n + 1)
    q = deque([1])
    visited[1] = True
    while q:
        x = q.popleft()
        for y in adj[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)

    # 1번을 제외한 감염 대수
    print(sum(visited) - 1)


