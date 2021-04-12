# ABC114D - 756
# URL: https://atcoder.jp/contests/abc114/tasks/abc114_d
# Date: 2021/04/07

# ---------- Ideas ----------
# 1からnまで素因数分解する
# 約数が75になるのは4パターンなので，全部数え上げる: 75 = 75 or 3*25 or 5*15 or 3*5*5
# ある整数Mが七五数のとき, a,b,c異なる素因数を用いて
# (1) M = a**74
# (2) M = a**2 * b**24
# (3) M = a**14 * b**4
# (4) M = a**2 * b**4 * c**4


# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
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
if n == 1: print(0); exit()

factor = []
for i in range(2, n+1):
    factor += prime_factorize(i)

num75 = [] # 七五数はかぶる可能性があるので，とりあえず作ったやつをここにいれる
counter = Counter(factor)

# M = a**74の形
for key, value in counter.items():
    if value >= 74:
        num75.append(key**74)


# M = a**2 * b**24の形
A, B = [], []
for key, value in counter.items():
    if value >= 2:
        A.append(key)
    if value >= 24:
        B.append(key)

for a in A:
    for b in B:
        if a != b:
            num75.append(a**2 * b**24)


# M = a**14 * b**4の形
A, B = [], []
for key, value in counter.items():
    if value >= 14:
        A.append(key)
    if value >= 4:
        B.append(key)

for a in A:
    for b in B:
        if a != b:
            num75.append(a**14 * b**4)

# M = a**2 * b**4 * c**4の形
A, B, C = [], [], []
for key, value in counter.items():
    if value >= 2:
        A.append(key)
    if value >= 4:
        B.append(key)
        C.append(key)


for a in A:
    for b in B:
        for c in C:
            if a != b and b != c and c != a:
                num75.append(a**2 * b**4 * c**4)

print(len(set(num75)))


# ------------------ Sample Input -------------------
10

100


# ----------------- Length of time ------------------
# 20分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc114/editorial.pdf
# 水diffにしては簡単でびっくりした
# 何の工夫も必要なかった

# ----------------- Category ------------------
#AtCoder
#水色diff
#素因数分解
#約数
#整数問題
#ABC-D
#全探索
#試し割り
#約数の個数