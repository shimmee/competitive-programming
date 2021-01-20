# ABC149-C: Next Prime
# URL: https://atcoder.jp/contests/abc149/tasks/abc149_c
# 日付: 2020/11/19

# ---------- 思ったこと / 気づいたこと ----------
# X＜10＊＊5なので，エラトステネスで全列挙すればいい。
# X=99992だとX以上の素数が10＊＊5を超えることもあるので注意


# ------------------- 方針 --------------------
# エラトステネスで10**5*2以下の素数を全て全列挙する
# Xの次に大きいものを探す。

# ------------------- 解答 --------------------
#code:python

def prime_sieve(n):
    # エラトステネスの篩
    # 参考: https://oku.edu.mie-u.ac.jp/~okumura/python/sieve.html
    sq = int(n ** 0.5)
    prime = [False] * 2 + [True] * (n-1) # 素数のboolリストを作る。最初の2マス(0と1)は素数でないのでFalse。

    for i in range(sq):
        if prime[i]:
            for j in range(i*2, n+1, i): # 素数の倍数倍は素数ではないので，Falseにする
                prime[j] = False

    return [i for i in range(n+1) if prime[i]]

prime = prime_sieve(10**5*2)
X = int(input())
for i in prime:
    if i >= X:
        print(i)
        exit()


# ------------------ 入力例 -------------------
20

2

99992

# ----------------- 解答時間 ------------------
# 4分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc149/editorial.pdf
# 10000を超える点に注意してWAを避けた。サンプルのおかげ

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#素数
#エラトステネスの篩