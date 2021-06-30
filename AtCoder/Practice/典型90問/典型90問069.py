# 典型90問069 - Colorful Blocks 2（★3）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bq
# Date: 2021/06/17

# ---------- Ideas ----------
# Colorful Subsequencesに似てる
# https://scrapbox.io/shinmeikeita-67718894/%23_AGC031A_-_Colorful_Subsequence
# 最初はk, 次はk-1，その次から毎回k-2個の選択肢がある
# n=1のときだけ注意


# ------------------- Answer --------------------
#code:python
# 綺麗にかく
mod=10**9+7
n, k = map(int, input().split())
if n == 1: print(k)
else: print(k*(k-1)*pow(k-2, n-2, mod) % mod)

# 短く書く
n,k=map(int,input().split())
print(k if n==1 else k*(k-1)*pow(k-2,n-2,10**9+7)%(10**9+7))

# ------------------ Sample Input -------------------
1 10
2 3
2 2
3 2
10 2
2021 617

# ----------------- Length of time ------------------
# 5分?

# -------------- Editorial / my impression -------------
# Nowhere P と100％同じ問題でした
# https://atcoder.jp/contests/jsc2021/tasks/jsc2021_d

# ----------------- Category ------------------
#AtCoder
#数え上げ
#典型90問
#pow
#繰り返し二乗法