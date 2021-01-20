# CADDi 2018 C - Product and GCD
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/caddi2018/tasks/caddi2018_a
# Date: 2021/01/08


# ------------------- Solution -------------------- 
# 素因数分解する
# 素因数の出現回数を数える
# 各素因数の出現回数がp以上なら，その素因数を最大公約数の一部にできる

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

n, p = map(int, input().split())

factor = prime_factorize(p)
from collections import Counter
ans = 1
for key, value in Counter(factor).items():
    if value >= n:
        ans *= key**(value//n)
print(ans)

# **を*にしててn=1のケースがWAになっちゃった



# ------------------ Sample Input -------------------
1 24

3 24

5 1

1 111

4 972439611840


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/caddi2018/editorial.pdf

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-medium
#試し割り
#素因数分解