# ARC113A - A*B*C
# URL: https://atcoder.jp/contests/arc113/tasks/arc113_a
# Date: 2021/02/21

# ---------- Ideas ----------
# 1からKを全て素因数分解: O(KlogK)でK<=10**5なので1億回ループ
# 例: 素因数分解の結果が[2,3]でこれをA,B,Cに振り分けたい:
# 区別のある3つの箱に区別のないボールを振り分けるのと同じ: https://methodology.site/n-balls-and-3boxes/2/#2
# (n+2)C2 で計算できる


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

def n2C2(n):
    return (n+2)*(n+1)//2

from collections import deque, Counter
K = int(input())
ans = 0
for i in range(1, K+1):
    prime = prime_factorize(i)
    m = len(prime)
    counter = Counter(prime)
    cnt = 1
    for key, value in counter.items():
        cnt *= n2C2(value)
    ans += cnt
print(ans)

###################################
# 25分でACしたけど全探索できるらしい

K = int(input())
ans = 0
for a in range(1, K+1):
    bc = K // a
    for b in range(1, bc+1):
        c = bc // b
        ans += c
print(ans)

# ------------------ Sample Input -------------------
2

31415

10


# ----------------- Length of time ------------------
# 25分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc113/editorial
# 全探索だと調和級数で間に合うっぽい

# ----------------- Category ------------------
#AtCoder
#ARC-A
#全探索
#素因数分解
#調和級数