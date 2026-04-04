import sys
from collections import deque


def main():
    sys.setrecursionlimit(3000)
    n, m, v = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    for i in range(1, n + 1):
        adj[i].sort()

    visited = [False] * (n + 1)
    dfs_order = []

    def dfs(x):
        visited[x] = True
        dfs_order.append(str(x))
        for y in adj[x]:
            if not visited[y]:
                dfs(y)

    dfs(v)
    print(" ".join(dfs_order))

    visited = [False] * (n + 1)
    bfs_order = []
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        bfs_order.append(str(x))
        for y in adj[x]:
            if not visited[y]:
                visited[y] = True
                q.append(y)

    print(" ".join(bfs_order))

