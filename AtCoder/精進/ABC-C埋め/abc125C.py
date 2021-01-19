# ABC125C - GCD on Blackboard
# URL: https://atcoder.jp/contests/abc125/tasks/abc125_c
# 日付: 2020/11/28

# ---------- 思ったこと / 気づいたこと ----------
# 特定の整数を消すときめたら，それ以外の要素の最大公約数を求めればいい
# 各要素の約数を求めて，インデックスが約数を表すリストを作って，全部の約数について出現回数を数える
# 出現回数がn or n-1の約数のうち，最大のものを出力すればよさそう


# ------------------- 解答 --------------------
#code:python
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
A = list(map(int, input().split()))
l = [0]*(max(A)+1)

for a in A:
    divisors = make_divisors(a)
    for d in divisors:
        l[d] += 1

ans = 0
for i in range(len(l)):
    if l[i] == n or l[i] == n-1:
        ans = i
print(ans)


# 10億行のリストが作れなかったので，約数が出るたびにカウントすることに

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
A = list(map(int, input().split()))

l = [[] for i in range(2)]
for a in A:
    divisors = make_divisors(a)
    for d in divisors:
        if d in l[0]:
            idx = l[0].index(d)
            l[1][idx] += 1
        else:
            l[0].append(d)
            l[1].append(1)

ans = 0
for i in range(len(l[0])):
    if l[1][i] == n or l[1][i] == n-1:
        ans = max(ans, l[0][i])
print(ans)

# TLE!!!!!!!!!!!!!!!!!


# 愚直にgcdやってみる
import math
from functools import reduce
def gcd_list(numbers):
    return reduce(math.gcd, numbers)

import numpy as np
n = int(input())
A = np.array(list(map(int, input().split())))

ans = 1
for i in range(n):
    ans = max(ans, np.gcd.reduce((np.delete(A, i))))
print(ans)



# 解説分かりづらい https://img.atcoder.jp/abc125/editorial.pdf
# このブログがわかりやすい: https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2019/0427_abc125除くと決めた整数をA[i]としたとき，
# まず事前準備として「先頭から末尾までの累積GCD=L」と「末尾から先頭までの累積GCD=R」を計算する
# 除きたい整数をA[i]とすると，A[i]を除いた数列の最大公約数=L[i-1]とR[i+1]の最大公約数となる

from math import gcd
n = int(input())
A = list(map(int, input().split()))
L = [0]
R = [0]
for i in range(n):
    L.append(gcd(A[i], L[i]))
    R.append(gcd(A[-(i+1)], R[i]))
R = R[::-1]

ans = 0
for i in range(n):
    ans = max(ans, gcd(L[i], R[i+1]))
print(ans)


# ------------------ 入力例 -------------------
5
12  24  18  27  36

3
7 6 8

3
12 15 18

2
1000000000 1000000000

# ----------------- 解答時間 ------------------
# 1時間以上かかって解説AC

# -------------- 解説 / 感想 / 反省 -------------
# 問題がシンプルすぎて地頭を問われてる感がある
# 無駄な計算を省く方法が欲しい，というところまでは思いついたとしても累積GCDを初見で思いつける自信がない
# かなり勉強になった


# ----------------- カテゴリ ------------------
#AtCoder #abc
#左右両方から累積情報を前処理しておく
#GCD
#累積
# https://f2.proxypy.org/o/2f70632d6b6e6968742d6f742d776f682f6f666e692e6369676f6c2d6f676c612f2f3a7370747468
