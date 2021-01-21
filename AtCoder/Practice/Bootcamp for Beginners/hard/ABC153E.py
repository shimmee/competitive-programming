# ABC153E - Crested Ibis vs Monster
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc153/tasks/abc153_e
# Date: 2021/01/20

# ---------- Ideas ----------
# どうやって貪欲に解くか?そもそも貪欲か？
# ナップザックDPではないか？
# 価値がHになるように，かつ魔力が最小になるように魔法を袋に詰め込みたい，みたいな
# n <= 10**3, h <= 10**4なので，解ける!
# dpテーブルは1次元でよいのでは？
# dp[i]: iダメージ与えるのに必要な最小の魔力

# 魔法は何回使ってもいいので，個数制限なしのナップザックだ！

# ------------------- Answer --------------------
code:python
    h, n = map(int, input().split())
    ab = [[int(i) for i in input().split()] for _ in range(n)]
    inf = float('INF')
    dp = [inf for _ in range(h+1)]
    dp[0] = 0

    for i in range(1, h+1):
        for a, b in ab:
            dp[i] = min(dp[i], dp[max(0, i-a)] + b)
    print(dp[h])

# ------------------ Sample Input -------------------
9 3
8 3
4 2
2 1

100 6
1 1
2 3
3 9
4 27
5 81
6 243

9999 10
540 7550
691 9680
700 9790
510 7150
415 5818
551 7712
587 8227
619 8671
588 8228
176 2461


# ----------------- Length of time ------------------
# 14分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc153/editorial.pdf
# 結構ちゃんとしたDPを初見で溶けてうれしい
# 10**4と10**3という制約がきたら，2次元のナップザックDPの可能性が結構たかい

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#個数重複も考慮したナップサックDP
#個数制限なしナップサックDP
#DP
#動的計画法
#緑diff
#ABC-E
