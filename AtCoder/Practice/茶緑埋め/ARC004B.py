# ARC004B - 2点間距離の最大と最小 ( Maximum and Minimum )
# URL: https://atcoder.jp/contests/arc004/tasks/arc004_2
# Date: 2021/02/13

# ---------- Ideas ----------
# 最大は全ての和
# 最小は以下
# n=1 (2点)の場合，入力そのまま
# n >= 2の場合 (3点以上): 最大の辺が他の辺の和より大きいか小さいかで場合分け
# 小さい時: 原点に帰れるので0
# 大きい時: 原点まで届かないので，(最大の辺 - 他の辺の和)を出力

# ------------------- Answer --------------------
#code:python
n = int(input())
a = [int(input()) for _ in range(n)]
max_a = max(a)
sum_a = sum(a)
rest_a = sum_a - max_a

# 最大値
print(sum_a)

# 最小値
print(0 if rest_a >= max_a else max_a - rest_a)


# ------------------ Sample Input -------------------
3
4
8
1


10
1
2
3
4
5
6
7
8
9
10


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# 非公式解説: https://kyopro.hateblo.jp/entry/2019/05/23/214835
# こういう類の問題をロボットアーム問題と名付けたい
# ロボットアームは初めて解いた

# ----------------- Category ------------------
#AtCoder
#ロボットアーム
#最大値との差