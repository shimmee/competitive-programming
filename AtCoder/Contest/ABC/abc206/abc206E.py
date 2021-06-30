# ABC206
# URL:
# Date: 2021/06/19

# ---------- Ideas ----------
# x,y はgcd以外の約数を持つ
# x,yは互いに素ではなく(つまりgcd != 1)，gcdとは異なる約数

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
def prime_sieve(n):
    # エラトステネスの篩
    # 参考: https://oku.edu.mie-u.ac.jp/~okumura/python/sieve.html
    sq = int(n ** 0.5)
    prime = [False] * 2 + [True] * (n-1) # 素数のboolリストを作る。最初の2マス(0と1)は素数でないのでFalse。

    for i in range(sq+1):
        if prime[i]:
            for j in range(i*2, n+1, i): # 素数の倍数倍は素数ではないので，Falseにする
                prime[j] = False

    return [i for i in range(n+1) if prime[i]]

len(prime_sieve(10**6))

# ------------------ Sample Input -------------------


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
