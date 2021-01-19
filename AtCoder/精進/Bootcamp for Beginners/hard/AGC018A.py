# AGC018A - Getting Difference
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc018/tasks/agc018_a
# Date: 2021/01/15

# ---------- Ideas ----------
# Kがmax(A)より大きかったら無理
# KがAに入ってたらOK
# 1さえ作れれば，必ずKは作れる
# どれだけ操作を繰り返しても，max(A)以下の数字ができる

# Kとa[i]の差をaから作れるのでもOK。
# K=7, a=[9,3,4]だったら[2,10,11]がaから作れればOK
#

# 同じ数字のボールが箱に入っている意味はないから，setで管理してよさそう

# ------------------- Solution --------------------
# ソートする
# (1) Kがmax(A)より大きかったらダメ
# (2) KがAに入ってたらOK
# (3) 前後の差が1のものがあればOK
# (4) 2倍+1したものがAに入ってればOK: 2回で1を作れるから
# (5) Kとa[i]の差をaから作れるのでもOK。

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
A_set = set(A)

if max(A) < k:
    print('IMPOSSIBLE')
    exit()
elif k in A_set:
    print('POSSIBLE')
    exit()

for i in range(n-1):
    if A[i+1]-A[i] == 1:
        print('POSSIBLE')
        exit()

for a in A:
    if 2*a+1 in A_set:
        print('POSSIBLE')
        exit()

for a in A:
    if a > k: b = k-a
    else: b = k+a
    if b in A_set:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')


# 嘘解法っぽいのでACできた！
# 解説: https://img.atcoder.jp/agc018/editorial.pdf
# Kが全要素のgcdで割り切れたらOK
n, k = map(int, input().split())
A = list(map(int, input().split()))

if max(A) < k:
    print('IMPOSSIBLE')
else:
    from math import gcd
    from functools import reduce

    def gcd_list(numbers):
        return reduce(gcd, numbers)

    G = gcd_list(A)
    if k % G == 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

# ------------------ Sample Input -------------------
3 7
9 3 4

3 5
6 9 3

4 11
11 3 7 15

5 12
10 2 8 6 4


# ----------------- Length of time ------------------
# 30分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc018/editorial.pdf
# けんちょんタグが役立つ: https://drken1215.hatenablog.com/entry/2020/03/22/205100
# ユークリッド互除法と全く同じような操作であることに気づかなかった

# ----------------- Category ------------------
#AtCoder #AGC-A
#BootcampForBeginners-hard
#wanna_review #hard復習 #復習したい
#操作がEuclidの互除法に対応
#操作:2つのものを1つにマージ
#最大公約数
#GCD
#整数問題
#操作を好きな回数だけ行える