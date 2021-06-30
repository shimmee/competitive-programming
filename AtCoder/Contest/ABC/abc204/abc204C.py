# ABC204C- - Tour
# URL: https://atcoder.jp/contests/abc204/tasks/abc204_c
# Date: 2021/06/06

# ---------- Ideas ----------
# 全頂点からBFSやる

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)

ans = 0
for s in range(n):
    dist = [-1]*n
    dist[s] = 0
    que = deque([])
    que.append(s)

    while que:
        v = que.popleft()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)

    for i in range(n):
        if dist[i] != -1:
            ans += 1
print(ans)

# ------------------ Sample Input -------------------
3 3
1 2
2 3
3 2


# ----------------- Length of time ------------------
# やるだけ6分

# -------------- Editorial / my impression -------------
# こういうやるだけ問題出して欲しい

# ----------------- Category ------------------
#AtCoder
#BFS