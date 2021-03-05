# ABC160D - Line++
# URL: https://atcoder.jp/contests/abc160/tasks/abc160_d
# Date: 2021/03/04

# ---------- Ideas ----------
# BFSで無理やり解く
# 各頂点から他の全頂点への最短経路をBFSで求める。
# 各最短距離をインクリメントして，重複してるから最後に2で割る。

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n, x, y = map(int, input().split())

G = [[] for _ in range(n)]
for i in range(n-1):
    G[i].append(i + 1)
    G[i + 1].append(i)
G[x - 1].append(y - 1)
G[y - 1].append(x - 1)

dist_all = [0]*n
for s in range(n):
    dist = [-1]*n
    dist[s] = 0
    que = deque([s])

    while que:
        v = que.popleft()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                que.append(u)
    for d in dist:
        dist_all[d] += 1

for i in range(1, n):
    print(dist_all[i]//2)


# AC！！したけど，きれいな解き方があるっぽい
# 各頂点iからjへの行き方を，x or yを経由しない方法と経由する方法の小さい方とすればOK
# 経由しない: j-i
# i->x->y->j と経由する:abs(i-x) + abs(y-j)

n, x, y = map(int, input().split())
x -= 1
y -= 1

dist = [0]*n
for i in range(n):
    for j in range(i+1, n):
        d = min([j-i, abs(i-x)+abs(j-y)+1])
        dist[d] += 1
for i in range(1, n):
    print(dist[i])


# ------------------ Sample Input -------------------
5 2 4

3 1 3

# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# 想定解法がとても賢かった。
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/04/22/002100
# いろいろな解き方があるっぽい

# ----------------- Category ------------------
#AtCoder
#ABC-D
#各kに対して
#BFS
#グラフ問題
#最短路問題
#無向グラフ
#緑diff