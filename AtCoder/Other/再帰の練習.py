######################################################
######################################################
######################################################
# 再帰関数 / DFSの勉強
# 2020/12/05
######################################################
######################################################
######################################################

import sys
sys.setrecursionlimit(1000000)

############################################################
# n以下の正の整数の総和 (1+2+⋯+n) を計算する関数sum
############################################################
def sum(n):
    if n == 0:
        return 0
    return sum(n-1) + n
sum(10)

############################################################
# n以下の正の整数の総和 (1+2+⋯+n) を計算するプログラム: コメントつき
############################################################

def fun(n):
    if n == 0:
        return 0
    ans = fun(n - 1) + n
    print(f'{n}までの和={ans}')
    return ans
fun(10)


############################################################
# 入力の底xと冪指数aからべき乗を計算する関数power: x**aを求める関数
############################################################
def power(x, a):
    if a == 0:
        return 1
    return power(x, a-1)*x
power(2,10)

############################################################
# nの階乗を求める関数factorial: n!
############################################################
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1)*n
factorial(5)


############################################################
# 長さnのリストに1を詰め込む関数
############################################################
def fill_one(n):
    if n == 0:
        return []

    l = fill_one(n-1)
    print(f'l is {l}')
    l += [1]
    return l
fill_one(10)

############################################################
# 整数a, bの最大公約数gcdを求める関数
############################################################
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
gcd(5, 10)


############################################################
# ツリー構造をもったリストの探索: ただの深さ優先
############################################################
l = ['1', '2', ['3a', '3b', ['3a1', '3a2']], ['4a', '4b', '4c', '4d'], '5']
def dfs_loop(l):

############################################################
# bitのパターンを出力する関数bit: n桁のbitのパターン全部
############################################################
# n=3なら[0,0,0], [0,0,1], ..., [1,1,1]まで
# ハローさんのブログより: https://qiita.com/ikngtty/items/a494ff83f12646dee88f
def make_bit_pattern(n):

    if n == 0:
        return [[]] # この空のリストにどんどん詰めていく
    rest_pattern = make_bit_pattern(n-1)

    pattern = []
    pattern += [[0] + p for p in rest_pattern]
    pattern += [[1] + p for p in rest_pattern]
    return pattern

make_bit_pattern(3)


############################################################
# ABC114C - 755
# https://atcoder.jp/contests/abc114/tasks/abc114_c
############################################################

# n桁の準753数を作る関数
def make_753(n):
     if n == 0:
         return ['']

     l = make_753(n-1)
     pattern = []
     pattern += ['7' + p for p in l]
     pattern += ['5' + p for p in l]
     pattern += ['3' + p for p in l]

     return pattern
make_753(3)


# n桁までの準753数を作る関数
def make_753(n):
    if n == 0:
        return ['']

    l = make_753(n - 1)
    pattern = []
    pattern += ['7' + p for p in l]
    pattern += ['5' + p for p in l]
    pattern += ['3' + p for p in l]

    return list(set(l+pattern))

n = int(input())
num753 = make_753(9)
ans = 0
for i in num753:
    if i == '': continue
    if (int(i) <= n) and ('7' in i) and ('5' in i) and ('3' in i):
        ans+=1
print(ans)



























import itertools
all_pattern = itertools.product([0, 1], repeat=n)
for pattern in all_pattern:
    for i in range(n):
        if pattern[i] == 1:






############################################################
# リストxの要素からk個選ぶ組み合わせ列挙する関数
############################################################
x = [1,2,3,4,5]
def make_combination(k, x, ans=[]):
    if k == len(x):
        ans.append(list(x))
        return

    make_combination(k + 1, x, ans)
    x[k] = 1
    make_combination(k + 1, x, ans)
    x[k] = 0

make_combination(2, x, ans=[])