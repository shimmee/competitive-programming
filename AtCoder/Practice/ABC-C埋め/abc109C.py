# ABC109C - Skip
# URL: https://atcoder.jp/contests/abc109/tasks/abc109_c
# 日付: 2020/12/03

# ------------------- 方針 --------------------
# Xと各座標xとの距離のgcdが答え

# ------------------- 解答 --------------------
#code:python
n, X = map(int, input().split())
x = list(map(int, input().split()))

dist = [abs(X-i) for i in x]
import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

print(gcd_list(dist))

# ------------------ 入力例 -------------------
3 81
33 105 57

1 1
1000000000

# ----------------- 解答時間 ------------------
# 3分! 早い！

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc109/editorial.pdf
# 想像どおりの解法が解説に書いてた

# ----------------- カテゴリ ------------------
#AtCoder #abc
#GCD
#最大公約数
