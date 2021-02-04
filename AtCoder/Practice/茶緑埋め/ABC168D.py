# ABC168D - .. (Double Dots)
# URL: https://atcoder.jp/contests/abc168/tasks/abc168_d
# Date: 2021/02/03

# ---------- Ideas ---------- 
# 連結グラフではない限り，どの部屋からも1にたどり着くというのは無理
# 経路復元の問題
# BFSで最短経路を探索しながら，来た道を配列に記録していく

# ------------------- Answer --------------------
#code:python
from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

route = [-1]*n # 1つ前の部屋番号を格納する配列
que = deque([])

route[0] = 0
que.append(0)

while que:
    v = que.popleft()
    for u in G[v]:
        if route[u] == -1:
            route[u] = v
            que.append(u)

if min(route) == -1:
    print('No')
else:
    print('Yes')
    for i in range(1, n):
        print(route[i]+1)

# ------------------ Sample Input -------------------
6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6


4 4
1 2
2 3
3 4
4 2


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc168/editorial.pdf
# 10分でスクラッチでBFSを書けるというのは大きな成長

# ----------------- Category ------------------
#AtCoder  
#ABC-D
#グラフ問題
#最短路問題
#構築問題
#BFS
#幅優先探索
#経路復元
#緑diff

