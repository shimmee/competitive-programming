# ABC094D - Binomial Coefficients
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc094/tasks/arc095_b
# Date: 2021/01/16

# ---------- Ideas ----------
# comb(a,b)のaは半分より右だけが選択肢になる
# aは大きい方が良い。同じbならできるだけaは大きい方が良い
# できるだけbはaの半分くらいがいい

# ------------------- Solution --------------------
# ソートする
# 最大のaを選ぶ，bはリストからa/2に一番近い数を選ぶ

# ------------------- Answer --------------------
#code:python
from scipy.special import comb

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
max_a = max(a)
now = 0
for j in range(1, n):
    c = comb(max_a, a[j], exact=True)
    if c >= now:
        now = c
        ans = [max_a, a[j]]

print(ans[0], ans[1])

# TLE!!!
# 組み合わせ計算が時間かかってる

# a[i]の半分に一番近い数字を探す
import math
def getNearestValue(list, num):
    import numpy as np
    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]
n = int(input())
a = list(map(int, input().split()))
max_a = max(a)
a = sorted(a, reverse=True)[1:]
b1 = getNearestValue(a, math.ceil(max_a/2))
b2 = getNearestValue(a, math.floor(max_a/2))

if abs(b1-max_a/2) <= abs(b2-max_a/2): # b1の方がmax_a/2に近い場合
    print(max_a, b1)
else:
    print(max_a, b2)


# きれいに書きたい

def getNearestValue(list, num): # https://qiita.com/icchi_h/items/fc0df3abb02b51f81657
    import numpy as np
    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = getNearestValue(a[1:], max(a)//2)
print(max(a), b)

# こんな関数なくても，なくても，a/2に一番近い数字をループで探せばいい
n = int(input())
a = sorted(list(map(int, input().split())))
max_a = max(a)
b = a[0]
for i in range(n-1):
    if abs(b-max_a/2) > abs(a[i]-max_a/2):
        b = a[i]
print(max_a, b)


# ------------------ Sample Input -------------------
5
6 9 4 2 11

4
15 30 90 100

2
100 0

# ----------------- Length of time ------------------
# 21分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/arc095/editorial.pdf
# パスカルの三角形らしい
# 実際にcombを計算しなくても良いというのがミソ

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#パスカルの三角形
#combination
#組み合わせ計算
