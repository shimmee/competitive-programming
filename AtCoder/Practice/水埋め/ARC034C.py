# ARC034C - 約数かつ倍数
# URL: https://atcoder.jp/contests/arc034/tasks/arc034_3
# Date: 2021/04/09

# ---------- Ideas ----------
# A-B <= 100がポイント！
# BとAの間にある数字達の約数は，どんな子たちでもB!にかけてあげればA!の約数になりうる
# B+1，B+2，..., A-1, Aを素因数分解して，約数の個数を数えるだけ


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

a, b = map(int, input().split())
mod = 10**9+7
factor = []
for n in range(b+1, a+1):
    factor += prime_factorize(n)

counter = Counter(factor) # 素因数の出現回数

ans = 1
# 約数の個数を数える
for key, value in counter.items():
    ans  = ans * (value+1) % mod

print(ans)
# ------------------ Sample Input -------------------
3 2

15 4


# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc034
# けんちょんさん: https://drken1215.hatenablog.com/entry/2018/09/09/230316
# 簡単だった！今なら茶か緑diffだと思う

# ----------------- Category ------------------
#AtCoder
#素因数分解
#約数の個数
#階乗
#水色diff
#整数問題