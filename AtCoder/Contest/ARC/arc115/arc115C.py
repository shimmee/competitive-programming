#
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# 素因数の個数が答え

# ------------------- Answer --------------------
#code:python

n = int(input())
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

ans = [1]
for i in range(2, n+1):
    prime = prime_factorize(i)
    ans.append(len(prime)+1)
print(*ans)



# ------------------ Sample Input -------------------
9

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
