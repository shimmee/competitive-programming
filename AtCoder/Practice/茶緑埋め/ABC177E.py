# ABC177E - Coprime
# URL: https://atcoder.jp/contests/abc177/tasks/abc177_e
# Date: 2021/02/15

# ---------- Ideas ----------
# pairwiseじゃないときは全体をgcdすればいい
# A <= 10**6なので，前処理で1からmax(A)までの全ての整数を素因数分解できそう
# 10**6個全ての整数について素因数分解したい: osa_k法
# osa_k法: 1以上N以下の全ての整数を素因数分解 (or約数列挙)する際に，NlogNでできる
# 18  → 18 / minFactor[18] = 9 → 9 / minFactor[9] = 3 → 3 / minFactor[3] → 1

# ------------------- Solution --------------------
# ステップ0: 数列から1を除く: 元の数列は適当に保存
# ステップ1: 1からmax(A)までの各整数kの最小素因数(minFactor)を求める (エラトステネスの要領で)
# ステップ2: minFactorを用いて数列の各要素を素因数分解してlist(set, set, ...)で管理する
# ステップ3: 素因数が1つも重複して出現していなければpairwise coprime
# GCDしてみて1ならsetwise

# ------------------- Answer --------------------
#code:python
from math import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)
n = int(input())
A_raw = list(map(int, input().split()))
A = [a for a in A_raw if a != 1] # 1を除いて考える

# もし全要素が1ならAは空になってる: pairwise coprime'
if not A:
    print('pairwise coprime'); exit()

# エラトステネスでminFactorを作成
max_a = max(A)
minFactor = [0, 1] + [-1]*(max_a-1)
for i in range(2, max_a+1):
    for j in range(i, max_a+1, i):
        if minFactor[j] == -1:
            minFactor[j] = i

# 数列の各要素の全ての素因数を列挙: list内のsetで管理
factors = [] # 各aの全ての素因数
for a in A:
    now = a
    factor = set([])
    while now != 1:
        prime = minFactor[now]
        factor.add(prime)
        now //= prime
    factors.append(factor)

# pairwise coprime: 全ての素因数の集合が異なる
flag = [False]*(max(map(max, factors))+1) # 各素因数が出現したかどうか
judge = False # 一度でも同じ素因数が出現したらjudge = Trueとする
for factor in factors:
    for i in list(factor):
        if flag[i]:
            judge = True
            break
        else:
            flag[i] = True

if not judge:
    print('pairwise coprime')
elif gcd_list(A_raw) == 1:
    print('setwise coprime')
else:
    print('not coprime')


# ACした!!!
####################################
# けど終盤の2つのfor文を合体できそう!!
####################################

from math import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)
n = int(input())
A_raw = list(map(int, input().split()))
A = [a for a in A_raw if a != 1] # 1を除いて考える

# もし全要素が1ならAは空になってる: pairwise coprime'
if not A:
    print('pairwise coprime'); exit()

# エラトステネスでminFactorを作成
max_a = max(A)
minFactor = [0, 1] + [-1]*(max_a-1)
for i in range(2, max_a+1):
    for j in range(i, max_a+1, i):
        if minFactor[j] == -1:
            minFactor[j] = i

# 数列の各要素の全ての素因数を列挙しながらpairwise coprimeの判定
prime_flag = [False]*(10**6+1) # 各素因数が出現したかどうか
break_flag = False
judge = False # 一度でも同じ素因数が出現したらjudge = Trueとする
for a in A:
    now = a
    factor = set([]) # 要素aの素因数の集合
    while now != 1:
        prime = minFactor[now]
        factor.add(prime)
        now //= prime

    # 素因数が1度でも出現していればpairwiseではなくなるので，break
    for i in list(factor):
        if prime_flag[i]:
            judge = True
            break_flag = True
            break
        else:
            prime_flag[i] = True
    if break_flag:
        break


if not judge:
    print('pairwise coprime')
elif gcd_list(A_raw) == 1:
    print('setwise coprime')
else:
    print('not coprime')


# ------------------ Sample Input -------------------
5
1 1 1 1 1

3
5 22 33

3
6 10 15


3
3 4 5


# ----------------- Length of time ------------------
# 70分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc177/editorial
# 今まで解いた整数問題で一番楽しかった (解けたから)
# エラトステネスが大好き。
# けんちょんさんの解説が詳しい: https://drken1215.hatenablog.com/entry/2020/10/31/203300

# ----------------- Category ------------------
#AtCoder
#osa_k法
#緑diff
#ABC-E
#エラトステネスの篩
#高速素因数分解
#調和級数
#バケット
#制約:数値が10^6以下
#整数問題
#最大公約数
#GCD
#数列
#最大公約数の値を固定して考える
#O(N^2)個のものを考える問題
#ある量を固定して考える