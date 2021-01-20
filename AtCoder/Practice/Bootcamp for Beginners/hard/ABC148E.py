# ABC148E - Double Factorial
# Bootcamp For Beginners - Hard
# URL:  https://atcoder.jp/contests/abc148/tasks/abc148_e
# Date: 2021/01/13

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# 5**i*2ごとに，10の増え方が繰り上がるので，このリストlをつくる
# iが大きい順に5**i*2でnを割ってみて，商aが1以上なら，lのi番目をansに加える
# nを5**i*2で割った余りで更新する


# ------------------- Answer --------------------
#code:python
n = int(input())
if n % 2 == 1 or n < 10:
    print(0); exit()
else:
    ans = 0
    l = [0]*30
    l[0] = 0
    l[1] = 0
    l[2] = 6
    for i in range(3, 30):
        l[i] = (l[i-1])*5+1

    for i in reversed(range(30)):
        a = n // (5**i*2)
        if a > 0:
            ans += l[i]*a
            n %= (5**i*2)
        if n < 50:
            break
    print(ans + n//10)


# 解説: https://img.atcoder.jp/abc148/editorial.pdf
# nが10(=5**1*2)で割れる回数，50(=5**2*2)で割れる回数，250(=5**3*2)で割れる回数をどんどん足していけばいい
n = int(input())
if n % 2 == 1 or n < 10:
    print(0)
else:
    ans = 0
    for i in range(1, 30):
        ans += n // (5**i*2)
    print(ans)

# ------------------ Sample Input -------------------
12

5

1000000000000000000

100
130

# ----------------- Length of time ------------------
# 67分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc148/editorial.pdf
# とても大変だった
# 簡単に考えることができなかったため，複雑なコードになっちゃった
# 解説とやってることは同じ
# 復習してもよさそう。

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#wanna_review #hard復習 #復習したい
#ABC-E
#pで何回割れるか
#緑diff
#整数問題



# 実験

#
# def prime_factorize(n: int):
#     # 試し割り法による素因数分解
#     # https://en.wikipedia.org/wiki/Trial_division
#     factors = []
#     while n % 2 == 0:
#         factors.append(2)
#         n //= 2
#     f = 3 # 奇数でどんどん割っていって，素数を探す。
#     while f * f <= n:
#         if n % f == 0:
#             factors.append(f)
#             n //= f # nをfで割って減らす。
#         else:
#             f += 2 # 奇数なので+2ずつ足していく。
#     if n != 1: factors.append(n)
#     # Only odd number is possible
#     return factors
#
# def give_ans(n):
#     ans = 0
#     for i in range(2, n+1, 2):
#         p = prime_factorize(i)
#         ans += p.count(5)
#     return ans
# give_ans(250)
# give_ans(1250)
# give_ans(5**1)
# give_ans(5**2)
# give_ans(5**3)
# give_ans(5**4)
# give_ans(5**5)
# give_ans(5**6)
# give_ans(5**7)
# give_ans(5**8)
