# ARC114A - Not coprime
# URL: https://atcoder.jp/contests/arc114/tasks/arc114_a
# Date: 2021/03/14

# ---------- Ideas ----------
# 使用済み素因数のリストとans=1を用意
# 各要素を素因数分解して，全素因数について走査: どれかがスキップ，どれも使用されてなかったらans*=pして使用済みにする


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
X = sorted(list(map(int, input().split())))

# 素因数が1つでも使用済みだったらOK
# 何も使用されてなければ最小のprimeをかける
used = []
ans = 1
for x in X:
    prime = set(prime_factorize(x))
    flag= False
    for p in prime:
        if p in used:
            flag = True
            break
    if not flag:
        used.append(min(prime))
        ans *= min(prime)
print(ans)


# これは嘘解法でした。2ケースWAになります
# 2 5 15と15 5 2で答えが異なってしまうから，ダメでした。
# ------------------------------------------------------
# bit全探索が解法です。
# 50以下の素因数は15個なので，全部試します

from math import gcd
import itertools
n = int(input())
x = sorted(list(map(int, input().split())))

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
m = len(primes)

ans = float('INF')
all_pattern = itertools.product([0, 1], repeat=m)
for pattern in all_pattern:
    y = 1
    for i in range(m):
        if pattern[i] == 1:
            y *= primes[i]

    flag = True # yと全てのxが互いに素でなければTrue
    for j in range(n):
        if gcd(x[j], y) == 1:
            flag = False
    if flag:
        ans = min(ans, y)
print(ans)


# ------------------ Sample Input -------------------
3
47 2 15

3
2 5 15

3
15 5 2

4
2 3 6 12 7

3
3 6

3
7 13 35

4
4 4 4 5

3
3 5 7

2
4 3

2
47 49

7
3 4 6 7 8 9 10

8
3 4 5 6 7 8 9 10



# ----------------- Length of time ------------------
# 本番1時間かけてWAで解説AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc114/editorial
# bit全探索に気づかなかった。N<=50なので，気付きづらかった


# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#bit全探索
#GCD