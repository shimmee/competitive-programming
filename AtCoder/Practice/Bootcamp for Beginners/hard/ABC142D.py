# ABC142D - Disjoint Set of Common Divisors
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc142/tasks/abc142_d
# Date: 2021/01/12


# ------------------- Solution --------------------
# AとBをそれぞれ素因数分解して，setを取る
# 共通の素因数の個数+1が答え
# 使ってる関数が1を素因数として数えないため，+1をする

# ------------------- Answer --------------------
#code:python
def prime_factorize(n: int):
    # 試し割り法による素因数分解
    # https://en.wikipedia.org/wiki/Trial_division
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    f = 3 # 奇数でどんどん割っていって，素数を探す。
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            n //= f # nをfで割って減らす。
        else:
            f += 2 # 奇数なので+2ずつ足していく。
    if n != 1: factors.append(n)
    # Only odd number is possible
    return factors

a, b = map(int, input().split())
a_div = set(prime_factorize(a))
b_div = set(prime_factorize(b))

div = list(a_div & b_div)
print(len(div)+1)

# ------------------ Sample Input -------------------
12 18

420 660

1 2019

# ----------------- Length of time ------------------
# 9分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc142/editorial.pdf
# 解説どおりに解けた

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#最大公約数
#gcd
#素因数分解
#互いに素
#ABC-D
#整数問題
#試し割り法