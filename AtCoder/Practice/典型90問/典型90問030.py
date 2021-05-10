# 典型90問030 - K Factors
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ad
# Date: 2021/05/06

# ---------- Ideas ----------
# n以下の素数を列挙して，その素数を使ってまたエラトステネスの要領でカウントしていけばいい

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


n, k = map(int, input().split())
prime_list = prime_sieve(n)

prime_count = [0] *(n+1)
for p in prime_list:
    now = p
    while now <= n:
        prime_count[now] += 1
        now += p

ans = sum([1 for p in prime_count if p >= k])
print(ans)


# ------------------ Sample Input -------------------
15 2
30 2
200 4
869120 1
10000000 3


# ----------------- Length of time ------------------
# 10分くらい

# -------------- Editorial / my impression -------------
# 水diffだけど簡単だった
# 茶diffでもおかしくない

# ----------------- Category ------------------
#AtCoder
#整数問題
#素数列挙
#エラトステネスの篩