# ARC011C - ダブレット
# URL: https://atcoder.jp/contests/arc011/tasks/arc011_3
# Date: 2021/04/10

# ---------- Ideas ----------
# 単語をグラフの頂点と見なして，1文字違いの単語同士を辺でつなげる
# グラフにおけるfirstからlastまでの最短距離が聞かれているので，BFSで求める
# BFSの経路復元をして，何の単語を使用したかを出力する

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
def count_gap(si, sj):
    cnt = 0
    for k in range(m):
        if si[k] != sj[k]:
            cnt += 1
    return cnt

first, last = input().split()
m = len(first)
n = int(input())
S = [input() for _ in range(n)]

n += 2
S = [first] + S + [last]

G = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if count_gap(S[i], S[j]) <= 1:
            G[i].append(j)
            G[j].append(i)

# BFS from here
dist = [-1] * n
dist[0] = 0
route = [-1]*n # 1つ前の頂点を格納: 経路復元用
route[0] = 0

que = deque([0])
while que:
    v = que.popleft()
    for u in G[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            route[u] = v
            que.append(u)

if dist[-1] == -1:
    print(-1)
    exit()
else:
    print(dist[-1]-1)

# 経路復元
cur = n-1
passed = [S[cur]]
while cur != 0:
    cur = route[cur]
    passed.append(S[cur])
for s in passed[::-1]:
    print(s)




# ------------------ Sample Input -------------------
eye lid
4
lie
die
did
dye

eye eye
4
lie
die
did
dye

# ----------------- Length of time ------------------
# 27分

# -------------- Editorial / my impression -------------
# 単語をグラフとみなすのを思いついて嬉しかった
# 結構面倒だったけど面白かった
# マジカルバナナやん
# 辺の重さがすべて1なのでダイクストラの必要はない

# ----------------- Category ------------------
#AtCoder
#BFS
#幅優先探索
#経路復元
#最短経路問題
#マジカルバナナ
#最短路問題
#水diff
#グラフ問題