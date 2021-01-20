# ABC052C - Factors of Factorial
# URL: https://atcoder.jp/contests/arc067/tasks/arc067_a
# 日付: 2020/12/10

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 1からnまでの整数を素因数分解して，各素因数の出現回数のリストを作る: prime
# 素因数の個数から約数の数を計算: https://mathtrain.jp/numberofd

# ------------------- 解答 --------------------
#code:python
mod = 10**9+7
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

prime = [0]*n
for i in range(1, n+1):
    l = prime_factorize(i)
    if l != []:
        for p in l:
            prime[p-1] += 1
ans = 1
for p in prime:
    ans = ans * (p+1)
    ans = ans % mod
print(ans)




# ------------------ 入力例 -------------------
1000

# ----------------- 解答時間 ------------------
# 1時間くらい

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc067/editorial.pdf
# 素因数を求めるアイデアまではすぐ辿り着いたものの，素因数から約数の個数を計算する方法がわからず，自力で考えてしまった
# 約数の個数の計算方法を忘れがちなので，また復習してもいい: https://mathtrain.jp/numberofd

# ----------------- カテゴリ ------------------
#AtCoder #abc
#約数
#約数の個数
#素因数分解
#試し割り
#復習したい
