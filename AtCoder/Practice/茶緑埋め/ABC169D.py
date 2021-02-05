# ABC169D - Div Game
# URL: https://atcoder.jp/contests/abc169/tasks/abc169_d
# Date: 2021/02/04

# ---------- Ideas ---------- 
# 約数列挙してp^eと表せるものを候補として，小さい方から貪欲にnを割っていって1になるまで頑張る
# 2つの素数の組み合わせはダメ!!!
# 10**12なので約数列挙

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
if n == 1: print(0); exit()
prime = prime_factorize(n)
divisor = [prime[0]]
for i in range(1, len(prime)):
    if prime[i-1] == prime[i]:
        divisor.append(divisor[i-1]*prime[i])
    else:
        divisor.append(prime[i])
divisor.sort()

m = len(divisor)
ans = 0
for i in range(m):
    if n % divisor[i] == 0:
        n //= divisor[i]
        ans += 1
print(ans)
# ------------------ Sample Input -------------------
1000000000000

24

64

997764507000


# ----------------- Length of time ------------------
# 19分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc169/editorial.pdf
# 最初，nの全ての約数が候補になるのかと勘違いしていた。このせいでWA出して10分ロス
# 実際は，約数のうちp^eで表せるもの，つまり何かの素数の累乗で表せる約数のみ
# なので約数列挙ではなく素因数分解を用いて候補を列挙した。

# ----------------- Category ------------------
#AtCoder  
#ABC-D
#素因数分解
#操作:操作を最大何回行えるか
#Greedy
#貪欲
#整数問題
#操作:整数をreplaceしていく
#茶diff
