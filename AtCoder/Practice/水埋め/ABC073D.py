# ABC073D - joisino's travel
# URL: https://atcoder.jp/contests/abc073/tasks/abc073_d
# Date: 2021/04/07

# ---------- Ideas ----------
# 無向グラフ
# r1 からrRは好きな順番で回っていい: つまり巡回セールスマン問題 (TSP)
# R <= 8なので順列全探索で最短ルートを探せばOK
# r1からrRの距離は全点対間最短経路でワーシャルフロイド法で求められる

# ------------------- Answer --------------------
#code:python
import itertools
n, m, R = map(int, input().split())
r = list(map(int, input().split()))
r = [i-1 for i in r]

inf = float('INF')
dp = [[inf for _ in range(n)] for _ in range(n)]

# dpの各要素がaからbへの重みを表すので，入力の無効グラフを初期状態としてdpテーブルに埋め込む
for _ in range(m):
    a,b,c = map(int, input().split())
    dp[a - 1][b - 1] = c
    dp[b - 1][a - 1] = c

# スタートとゴールが同じ場合(i=jのとき)は距離がゼロ
for i in range(n):
    dp[i][i] = 0

# ワーシャルフロイド
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# r1からrRまでのルートを順列全探索して最短ルートを探す
ans = 10**20
all_pattern = list(itertools.permutations(r))
for pattern in all_pattern:
    dist = 0
    for i in range(R-1):
        v_from = pattern[i]
        v_to = pattern[i+1]

        dist += dp[v_from][v_to]
    ans = min(ans, dist)
print(ans)


# ------------------ Sample Input -------------------
3 3 3
1 2 3
1 2 1
2 3 1
3 1 4

# ----------------- Length of time ------------------
# 16分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc073/editorial.pdf
# ワーシャルフロイドと順列全探索という典型アルゴリズムだった
# グラフ問題で頂点数が200から300くらいだとワーシャルフロイドの感じがある
# 楽しかった


# ----------------- Category ------------------
#AtCoder
#ワーシャルフロイド
#順列全探索
#巡回セールスマン問題
#TSP
#全点対間最短経路
#水色diff
#最短路問題
#前処理:Floyd-Warshall法
#グラフ問題
#Floyd-Warshall法
#ABC-D