# AGC036A - Triangle
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc036/tasks/agc036_a
# Date: 2021/01/26
1146
# ---------- Ideas ----------
# 頂点の1つは原点でよさそう? -> そうとも限らない
# 辺が有理数のときS = x*y: Sの約数でともに10**9より小さいa,bがあればOK
# 整数の頂点から無理数の辺を引くことも可能

# 311114770564041497 = 19 * 6301 * 2598708396863
# x = √2598708396863, y = 19*6301*√2598708396863 みたいにできたら行ける。
# 無理数の辺xを作るには，整数の辺a,bからできる直角三角形の斜辺がxになる必要がある
# a^2+b^2=x^2となるようなaとbの長さがわかれば，適当に座標を設定すればいい
#

# ------------------- Solution --------------------
#

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

S = int(input())
prime_factorize(S)



l = []
for a in range(1, 10):
    for b in range(1, 10):
        l.append(a**2+b**2)
set(l)


x1=314159265
y1=358979323
x2=846264338
y2=327950288

import math
math.sqrt((x1-x2)**2 + (y1-y2)**2)

# ------------------ Sample Input -------------------
3
100
311114770564041497


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
