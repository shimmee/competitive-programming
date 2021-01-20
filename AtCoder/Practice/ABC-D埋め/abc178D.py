# ABC178D-Redistribution
# URL: https://atcoder.jp/contests/abc178/tasks/abc178_d
# 日付: 2020/11/20

# ---------- 思ったこと / 気づいたこと ----------
# s=10くらいまで書いてみたら，a[i] = a[i-1]+a[i-3]となってた
# フィボナッチ数列みたい
# S<= 2000なので，再帰関数で回る

# ------------------- 方針 --------------------
# フィボナッチ数列を改造する
# メモ化再帰で書く

# ------------------- 解答 --------------------
#code:python

import sys
sys.setrecursionlimit(1000000)
mod = 1000000007

n = int(input())
dp = [-1]*(n+1)
def fib(n):
    if n == 0 or n == 1 or n == 2:
        return 0
    if n == 3 or n == 4 or n == 5:
        return 1
    if dp[n] != -1:
        return dp[n] % mod
    dp[n] = fib(n-1) + fib(n-3)
    return dp[n] % mod

print(fib(n))

# ------------------ 入力例 -------------------
7
1729

# ----------------- 解答時間 ------------------
# 13分くらいAC

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/abc178/editorial/101
# 解説はDPで解いてる。やってることは再帰関数とおなじ

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#再帰関数
#メモ化再帰
#動的最適化
