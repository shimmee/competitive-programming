# ABC172D - Sum of Divisors
# URL: https://atcoder.jp/contests/abc172/tasks/abc172_d
# Date: 2021/02/06


# ---------- Ideas ----------
# 実行制限時間3秒だ
# エラトステネスの要領で，各整数の約数の個数をカウンターでカウントしていくのはどうか
# そもそも試し割りで素因数分解している時間がない

# ------------------- Answer --------------------
#code:python
# エラトステネス風に解いてみる
n = int(input())
if n == 1:
    print(1); exit()
count = [1]*n
for i in range(2, n+1):
    j = 1
    while i*j <= n:
        count[i*j-1] += 1
        j += 1
ans = 0
for i in range(1, n+1):
    ans += i*count[i-1]
print(ans)

# TLEです。厳密にはO(NlogN)だけど，間に合いそうだけど，間に合わない。
# C++はこれが一応1つの想定解法らしい。pythonでこれで通してる人はいないっぽい。
# 今回はTLEだけど悪くない方法だと思う。
# この人もこの方法で説いてる: https://torus711.hatenablog.com/entry/2020/06/28/124202


# 新しい学び
# osa_k法: 1以上N以下の全ての整数を素因数分解 (or約数列挙)する際に，NlogNでできる方法 (普通にやるとN√N)
# 参考1: https://blog.manuel1024.com/archives/79
# 参考2: http://tutuz.hateblo.jp/entry/2018/10/03/074039
# N以下の各整数kに対し，kの最小の素因数のリスト(minFactor)を作りたい: エラトステネスの要領で作れる
# minFactor = [-1,-1,2,3,2,5,3,7,2,3,5,11,3,13,7,5,2,17,3]
# 18  → 18 / minFactor[18] = 9 → 9 / minFactor[9] = 3 → 3 / minFactor[3] → 1

from collections import defaultdict
n = int(input())
sq = int(n ** 0.5)
min_factor = [-1]*(n+1) # kの最小の素因数のリスト: -1で初期化

# エラトステネス
for i in range(2, sq+1):
    if min_factor[i] == -1:
        for j in range(i, n+1, i): # 素数の倍数倍は素数ではないので，Falseにする
            min_factor[j] = i

# sq以上の素数の場所は-1になったままなので，自分自身を入れてあげる
for i in range(2, n+1):
    if min_factor[i] == -1:
        min_factor[i] = i

# n以下の各整数kについて，min_factorで割っていって，1になるまで進める。同時に各素因数で割った回数を数えておく
ans = 1
for k in range(2, n+1):
    now = k
    d = defaultdict(int) # 各素因数で割った回数
    while now != 1:
        prime = min_factor[now]
        d[prime] += 1
        now //= prime
    cnt = 1
    for val in d.values(): # 約数の個数は各素因数の出現回数+1のprod
        cnt *= val + 1
    ans += k * cnt
print(ans)


# ------------------ Sample Input -------------------
100

4

10

20

10000000


# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# 解説: https://img.atcoder.jp/abc172/editorial.pdf
# 公式の解法はO(√N)だった。しかしこんなアドホックな解き方は学びにならないので，osa_k法で解けてよかった。
# 素晴らしい解説: https://crieit.net/posts/koya-abc172-d

# 最初に思いついたエラトステネス風の約数個数カウント方法 O(NlogN)は，よくある方法らしい。
# 今回はC++なら通るけどpythonだと無理だった。
# とてもいい勉強になった。

# ----------------- Category ------------------
#AtCoder
#約数の個数
#エラトステネス
#素因数分解
#osa_k法
#O(NlogN)



# まずエラトステネスで素数列挙する: O(NloglogN)
# 素数リストを用いて，N以下の各整数kごとに試し割りして約数の個数を数える (NlogN)
# 結局試し割りの部分が上手くかけませんでした
#
# def prime_sieve(n):
#     # エラトステネスの篩
#     # 参考: https://oku.edu.mie-u.ac.jp/~okumura/python/sieve.html
#     sq = int(n ** 0.5)
#     prime = [False] * 2 + [True] * (n-1) # 素数のboolリストを作る。最初の2マス(0と1)は素数でないのでFalse。
#
#     for i in range(sq):
#         if prime[i]:
#             for j in range(i*2, n+1, i): # 素数の倍数倍は素数ではないので，Falseにする
#                 prime[j] = False
#
#     return [i for i in range(n+1) if prime[i]]
#
# n = int(input())
# prime = prime_sieve(int(n**0.5)+1)
# # k**0.5以下の最大の素数
# l = [0]*n
# now = 0
# for k in range(4, n+1):
#     while prime[now] <= k ** 0.5:
#         now += 1
#     l[k-1] = now
#
#
# ans = 1
# for k in range(2, n+1):
#     idx = l[k-1]
#     factor = prime[0:idx]
#     div_cnt = 1
#     now = k
#     for i in range(len(factor)):
#         if now == 1: break
#         prime_cnt = 0
#         while now % factor[i] == 0:
#             prime_cnt += 1
#             now //= factor[i]
#         div_cnt *= (prime_cnt + 1)
#     ans += k*div_cnt
# print(ans)
