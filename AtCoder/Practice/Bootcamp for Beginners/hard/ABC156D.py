# ABC156D - Bouquet
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc156/tasks/abc156_d
# Date: 2021/01/19

# ---------- Ideas ----------
# 逆元だ！

# ------------------- Solution --------------------
# (2**n) - 1 - nCa - nCb
# のmod!

# ------------------- Answer --------------------
#code:python
# この記事を参考！: https://nagiss.hateblo.jp/entry/2019/07/01/185421
n, p, q = map(int, input().split())

mod = 10**9+7
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def combination(n, r, mod=mod):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

print((pow(2, n, mod)-1 - combination(n, p, mod) - combination(n, q, mod))%mod)
# これでAC


# powを使った方がきれいに書ける!
# こちらから: https://atcoder.jp/contests/abc156/submissions/19271013
n, a, b = map(int, input().split())
mod = 10**9+7

def combination(n, r, mod=10**9+7):
    # n<=10**9, r<=10**6 で使用可能
    p, q = 1, 1
    for i in range(r):
        p = p*(n-i)%mod
        q = q*(i+1)%mod
    return p * pow(q,mod-2,mod) % mod

print((pow(2, n, mod)-1 - combination(n, a, mod) - combination(n, b, mod))%mod)


# これだとO(N)になった間に合わない
n, p, q = map(int, input().split())
mod = 10**9+7
def comb_mod(n, r, mod):
    # n <= 10**5で使用可能

    """powを用いて(nCr) mod p を求める"""
    ans = 1
    for i in range(1, n+1):
        ans = ans * i % mod
    for i in range(1, r+1):
        ans = (ans * pow(i, mod - 2, mod)) % mod
    for i in range(1, n-r+1):
        ans = (ans * pow(i, mod - 2, mod)) % mod
    return ans


print((pow(2, n, mod)-1 - comb_mod(n, p, mod) - comb_mod(n, q, mod))%mod)

# ------------------ Sample Input -------------------
4 1 3

100000 12432 34321

1000000000 141421 173205


# ----------------- Length of time ------------------
# 13分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc156/editorial.pdf
# 今回の問題はn <= 10**9なので，用意していた二項係数modのO(N)スニペットが使えなかった
# 繰り返し二乗法の関数を拾って乗り切った

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#数え上げ問題
#ABC-D
#補集合を考える
#緑diff
#逆元
#pow
#二項係数
#組み合わせ計算