# ARC030B - ツリーグラフ
# URL: https://atcoder.jp/contests/arc030/tasks/arc030_2
# Date: 2021/04/14

# ---------- Ideas ----------
# xを根とする根付き木と考える
# 辺に注目
# 宝石を取るために通る必要のある最低限の辺の個数 * 2が答えになりそう
# xからすべての宝石への最短経路を考えて，その最短経路で通るすべての辺が最低限必要な辺になりそう?
# BFSでやr
# xから各宝石への経路復元を行い，通った辺を保存していき，最後に辺の数を数える

# ------------------- Answer --------------------
#code:python
n, x = map(int, input().split())
h = list(map(int, input().split()))
h = [i for i in range(n) if h[i]]
G = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

if len(h) == 0 or len(h) == 1:
    print(0)
    exit()

from collections import deque, Counter

# bfs
s = x-1 # スタート地点
pre = [-1]*n
pre[s] = 0 # 親の頂点
que = deque([s])

while que:
    v = que.popleft()
    for u in G[v]:
        if pre[u] == -1:
            pre[u] = v
            que.append(u)

# 経路復元
passed = []
for g in h:
    cur = g
    while cur != s:
        passed.append([min(cur+1, pre[cur]+1), max(cur+1, pre[cur]+1)])
        cur = pre[cur]

# 重複を削除
passed = [list(tupl) for tupl in {tuple(item) for item in passed }]
print(len(passed)*2)

# ------------------ Sample Input -------------------
8 4
1 0 1 0 1 0 1 0
1 2
2 3
2 4
1 5
5 6
5 7
7 8

5 1
1 0 1 0 1
1 2
2 3
2 4
1 5


# ----------------- Length of time ------------------
# 30分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc030
# DFSでオイラーツアー的に全部回るのが想定解法だったらしい
# 今回のBFSの解き方だと，経路復元にO(N^2)かかってるので，Nが大きいときは通用しない
#

# ----------------- Category ------------------
#AtCoder
#BFS
#DFS
#幅優先探索
#深さ優先探索
#オイラーツアー
#euler_tour
#経路復元
#最短経路
#行きがけ帰りがけ