# ARC034B - 方程式
# URL: https://atcoder.jp/contests/arc034/tasks/arc034_2
# Date: 2021/02/08

# ---------- Ideas ----------
# 全て求めよだが，最大で2つしかなさそう
# n<=10のときはnが偶数の時OK
# n > 10のとき，最大の桁が奇数なら行ける
# 桁の和は最大でも9*18
# f(x)は0から9＊18までとりうるので，x=n-f(x)はnからn-9*18まで調べればOK
# xをnからn-9*18の範囲で全探索する!

# ------------------- Answer --------------------
#code:python
n = int(input())

ans = []
flag = False
for i in range(max(0, n-9*18), n+1):
    s = i + sum(list(map(int, str(i))))
    if s == n:
        ans.append(i)
        flag = True
if flag:
    print(len(ans))
    for i in ans:
        print(i)
else: print(0)

# ------------------ Sample Input -------------------
8


# ----------------- Length of time ------------------
# 32分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc034
# 気づくまでにとても時間がかかった。
# ABC166D - I hate factorizationに似てる！
# 方程式を満たす整数を求める問題で，探索するべき整数の範囲が広い場合，探索する範囲を絞れる可能性が高い

# ----------------- Category ------------------
#AtCoder
#範囲を絞る
#全探索の範囲を絞る
#整数問題
