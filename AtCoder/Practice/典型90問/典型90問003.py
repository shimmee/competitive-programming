# 典型90問003 - Longest Circular Road
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_c
# Date: 2021/05/10

# ---------- Ideas ----------
# 木の直径+1が最大スコアになる
# 木の直径は2回BFSすれば出せるらしい
# 1回目: 適当な適当な頂点から他の全点までの距離
# 2回目: 1回目で一番遠かった頂点からスタートして他の全点までの距離
# 2回目でmaxの距離が木の直径になる

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

def bfs(G, s):
    dist = [-1]*n
    dist[s] = 0
    que = deque([s])

    while que:
        v = que.popleft()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)

    return dist

dist1 = bfs(G, 0)
start = dist1.index(max(dist1))
dist2 = bfs(G, start)
print(max(dist2) + 1)

# ------------------ Sample Input -------------------
3
1 2
2 3

5
1 2
2 3
3 4
3 5



# ----------------- Length of time ------------------
# 12分

# -------------- Editorial / my impression -------------
# bfsをスクラッチから書いたので時間かかった
# 木の直径が2回のBFSで出せることは知らなかったので大きな学び
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/003.jpg

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#木の直径
#BFS
#幅優先探索
#最短経路問題