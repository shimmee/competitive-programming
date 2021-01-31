# ABC190E - Magical Ornament
# URL: https://atcoder.jp/contests/abc189/tasks/abc189_e
# Date: 2021/01/30

# ---------- Ideas ----------
# BFSのパートとTSPのパートに分けられる
# 本番でTSPに気づかなくて，終わった後に解説AC

# ------------------- Solution --------------------
# Cに含まれる各頂点から始まる他の頂点への距離をBFSで求める: K<=17なので最大17回BFS
# その後TSP
# 普通のTSPは各頂点を1回しか通らず，全ての頂点を回るようになっている


# ------------------- Answer --------------------
#code:python
from collections import deque
n, m = map(int, input().split())

G = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

k = int(input())
c = list(map(int, input().split()))
c = [i-1 for i in c]

inf = float('INF')
table = [[inf]*k for _ in range(k)] #table[i][j]: 頂点i (c[i])からjに行く時の最短距離
for i in range(k): # c[i]からスタート

    # dist(始点から各頂点までの距離)とque(回るべき頂点のリスト)を用意
    dist = [-1]*n
    que = deque([])

    # distとqueを初期化
    dist[c[i]] = 0
    que.append(c[i])

    while que:
        v = que.popleft()
        for w in G[v]:
            if dist[w] != -1:
                continue
            dist[w] = dist[v] + 1
            que.append(w)

    for j in range(k):
        table[i][j] = dist[c[j]]

# どこかに-1があるとだめ
min_d = min([min(i) for i in table])
if min_d == -1:
    print(-1)
    exit()


# 上で計算したtableをつかって巡回セールスマン
inf = float('INF')
ans = inf
dp = [[inf] * k for _ in range(2 ** k)]
for i in range(k):
    dp[1 << i][i] = 1

for S in range(1 << k):  # range(2**n)と同じ書き方。Sは0から2**n -1までの整数
    for v in range(k):
        if (S & (1 << v)) == 0: continue  # vは必ずSに含まれてる必要がある

        # Sからvを除いた集合:推移式の{S-{v}}の部分
        sub = S ^ (1 << v)
        for j in range(k):  # 頂点tから頂点v，重さはw
            dp[S][v] = min(dp[S][v], dp[sub][j] + table[v][j])
ans = min(dp[-1])
print(ans)

# ------------------ Sample Input -------------------
4 3
1 4
2 4
3 4
3
1 2 3

10 10
3 9
3 8
8 10
2 10
5 8
6 8
5 7
6 7
1 6
2 4
4
1 2 7 9

4 3
1 4
2 4
1 2
3
1 2 3

# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc190/editorial
# BFSの部分は本番で解けてたけど，残りのTSPの部分が思いつけなかった
# 今までで一番悔しかった
# 最近bitDPの巡回セールスマンやったばっかりだったのに，全然気づけなかった

# ----------------- Category ------------------
#AtCoder
#ABC-E
#TSP
#巡回セールスマン問題
#bitDP
#動的計画法
#復習したい
#解説AC