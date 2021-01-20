# パナソニックプログラミングコンテスト2020C - Sqrt Inequality
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_c
# Date: 2021/01/04

# ---------- Ideas ----------
# 桁の大きい浮動点小数の問題
# Topic of this problem is "floating-point number"

# ------------------- Solution --------------------
# 桁の大きい浮動点小数の問題

# ------------------- Answer --------------------
#code:python
a,b,c = map(int, input().split())
if 4*a*b < (c-a-b)**2:
    print('Yes')
else:
    print('No')
# 1ケースWA


a,b,c = map(int, input().split())
if (c-a-b) >= 0 and 4*a*b < (c-a-b)**2:
    print('Yes')
else:
    print('No')
# AC!!!!


a,b,c = map(int, input().split())
if 4*a*b < (a**2 + b**2 + c**2)+2*(a*b-b*c-c*a):
    print('Yes')
else:
    print('No')
# 1ケースWA



a,b,c = map(int, input().split())
from math import sqrt
if 2*sqrt(a*b) < c-a-b:
    print('Yes')
else:
    print('No')
# 5ケースWA

a,b,c = map(int, input().split())
from math import sqrt
if sqrt(a) + sqrt(b) < sqrt(c):
    print('Yes')
else:
    print('No')
# 4ケースWA

# ------------------ Sample Input -------------------
2 3 9

2 3 10

# ----------------- Length of time ------------------
# 17min

# -------------- Editorial / my impression -------------
#  https://img.atcoder.jp/panasonic2020/editorial.pdf
# could solve along with the editorial

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#浮動点小数 #float