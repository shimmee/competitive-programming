# ABC152E - Flatten
# URL: https://atcoder.jp/contests/abc152/tasks/abc152_e
# Date: 2021/04/09

# ---------- Ideas ----------
# A = (2,3,4), B = (b1, b2, b3)とすると
# 2*b1 = 3*b2 = 4*b3 になる必要がある。これをKとおくと
# 数列Aの最小公倍数がKになる
# AのLCMを求めて，LCM / AiとすればBiになる

# ------------------- Answer --------------------
#code:python
from math import gcd
from functools import reduce
def lcm_base(x, y):
    return (x * y) // gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

mod = 10**9+7
n = int(input())
a = list(map(int, input().split()))

lcm = lcm_list(a)
b = [lcm // i for i in a]
print(sum(b) % mod)



# ------------------ Sample Input -------------------

3
1000000 999999 999998

3
2 3 4


# ----------------- Length of time ------------------
# 4分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc152/editorial.pdf
# なぜ水diffなんだ？と思ったら最大公約数を求める部分が他の言語では不可能で，工夫が必要だったっぽい
# pythonだから解けた...
# 想定解法はAiを1つずつ素因数分解していって素因数の個数を数えていく感じの方法
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/01/22/071000

# ----------------- Category ------------------
#AtCoder
#最大公約数
#LCM
#素因数分解
#整数問題
#水色diff
#ABC-E