# ABC096D - Five, Five Everywhere
# URL: https://atcoder.jp/contests/abc096/tasks/abc096_d
# Date: 2021/04/17

# ---------- Ideas ----------
# 全部末尾が3の素数選べば任意の5つの合計が3の倍数になったりしない?
# 違う，5の倍数になる

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

prime = prime_sieve(55555)
prime3 = []
for p in prime:
    if str(p)[-1] == '3':
        prime3.append(p)

n = int(input())
print(*prime3[:n])

# ------------------ Sample Input -------------------
5
8


# ----------------- Length of time ------------------
# 8分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc096/editorial.pdf
# 想定解法は，5で割って1余る素数を寄せ集める，でした
# 末尾が3とか1だと5の倍数に必ずなるからそれでもよかった

# ----------------- Category ------------------
#AtCoder
#エラトステネス
#素数列挙
#数字の末尾に注目