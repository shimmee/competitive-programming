# 典型90問075 - Magic For Balls（★3）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bw
# Date: 2021/06/26

# ---------- Ideas ----------
# 素因数分解して素因数の個数を数えてm個とすると
# 2^kが初めてmを超えるようなkが答え

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

n = int(input())
factors = prime_factorize(n)
m = len(factors) - 1
print(m.bit_length())


# 短く書く

print((len(prime_factorize(int(input())))-1).bit_length())


# ------------------ Sample Input -------------------
42
48
53
120
12000000000

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
# すぐに思いついた
#

# ----------------- Category ------------------
#AtCoder
#典型90問
#試し割り法
#素因数分解
