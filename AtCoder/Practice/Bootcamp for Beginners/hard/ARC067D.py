# ARC067D - Walk and Teleport
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/arc067/tasks/arc067_b
# Date: 2021/01/22

# ---------- Ideas ----------
# X[i] < X[i+1]になってるわけだが，左の街から1つずつ行かない理由はあるか？
# 西に向かって歩くことってあるの？
# A>Bなら，毎回テレポートした方がいい。

# ------------------- Answer --------------------
#code:python

# とりあえず貪欲に解いてみる。サンプルは当然通る。
n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if (x[i+1]-x[i])*a > b:
        ans += b
    else:
        ans += (x[i + 1] - x[i]) * a
print(ans)
# 通った笑
# min使ったほうがきれい
n, a, b = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    ans += min((x[i + 1] - x[i]) * a, b)
print(ans)


# ------------------ Sample Input -------------------
4 2 5
1 2 5 7

7 1 100
40 43 45 105 108 115 124

7 1 2
24 35 40 68 72 99 103


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/arc067/editorial.pdf
# ABC-Cレベルの問題だった。
# 学ぶことがなにもない

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#greedy
#貪欲