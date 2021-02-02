# ABC070D - Transit Tree Path
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc070/tasks/abc070_d
# Date: 2021/01/31

# ---------- Ideas ----------
# 頂点Kから他の頂点への最短経路をBFSで事前計算しておく
# 頂点Kを経由してxからyに行くのは，xからKの距離とyからKの距離の和である
# 各クエリに対して，Kからxの距離 + Kからyの距離 を出力すればよい

# ------------------- Answer --------------------
#code:python
n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a - 1].append([b - 1, c])
    tree[b - 1].append([a - 1, c])

q, k = map(int, input().split())
k -= 1
from collections import deque
que = deque([])
dist = [-1]*n # 頂点Kから各頂点までの距離

que.append(k)
dist[k] = 0

# BFS
while que:
    v = que.popleft()
    for u, w in tree[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + w
            que.append(u)

# クエリごとの処理
for _ in range(q):
    x, y = map(int, input().split())
    print(dist[x-1] + dist[y-1])

# ------------------ Sample Input -------------------
5
1 2 1
1 3 1
2 4 1
3 5 1
3 1
2 4
2 3
4 5

7
1 2 1
1 3 3
1 4 5
1 5 7
1 6 9
1 7 11
3 2
1 3
4 5
6 7

# ----------------- Length of time ------------------
# 14分！AC!

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc070/editorial.pdf
# 解説やけんちょんさんはDFSで解いてる
# BFSのテンプレのコピペなしで1発でAC!
# この人と全く同じ解き方してる: https://hiro-kato.hatenablog.jp/entry/2019/06/15/233136

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#幅優先探索
#BFS
#深さ優先探索
#DFS
#緑diff
#クエリ処理問題
#事前計算
#前処理
#木問題
#グラフ問題
