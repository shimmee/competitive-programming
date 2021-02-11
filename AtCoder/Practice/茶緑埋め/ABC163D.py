# ABC163D - Sum of Large Numbers
# URL: https://atcoder.jp/contests/abc163/tasks/abc163_d
# Date: 2021/02/09

# ---------- Ideas ----------
# 連続する数は全部作れる
# n=10のとき，2つの整数で作れる最小値は0+1=1, 最大値は9+10=19。この間の数は全部作れる！
# i個の整数を使ったときの総和の最小値はa=0+1+...+i
# 最大値はb=(n-i)+(n-i+1)+...+n
# aからbの値は全て作れるので，このiに対応する総和の個数はb-a+1

# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n, k = map(int, input().split())
def get_sum(a, b):
    return (a + b) * (a - b + 1) // 2

ans = 0
for i in range(k, n+1):
    a = get_sum(i-1, 0)
    b = get_sum(n, n-i+1)
    ans += b-a+1
print(ans%mod + 1)

# ------------------ Sample Input -------------------
3 2

200000 200001

141421 35623


# ----------------- Length of time ------------------
# 27分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc163/editorial
# 「整数の総和の通り数」# はAGC015Aでやった。
# これも同じように「連続する数は全部作れる」というアイデアで解けた。


# ----------------- Category ------------------
#AtCoder
#全部
#数え上げ問題
#ABC-D
#O(N^2)個のものを考える問題
#ダブルカウントを防ぐ場合分けのテクニック
#等差数列
#緑diff
#全部作れる
#規則性のある整数列の総和の通り数