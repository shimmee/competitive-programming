# ABC070C - Multiple Clocks
# URL: https://atcoder.jp/contests/abc070/tasks/abc070_c
# 日付: 2020/12/17

# ---------- 思ったこと / 気づいたこと ----------
# LCMやん

# ------------------- 解答 --------------------
#code:python
from math import gcd
n = int(input())
T = [int(input()) for _ in range(n)]

lcm = T[0]
for i in T[1:]:
  lcm = lcm*i//gcd(lcm, i)
print(lcm)

# コードがダサいので新しく作ったスニペットで

from math import gcd
from functools import reduce
def lcm_base(x, y):
    return (x * y) // gcd(x, y)
def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
n = int(input())
T = [int(input()) for _ in range(n)]

print(lcm_list(T))


# ------------------ 入力例 -------------------
2
2
3

5
2
5
10
1000000000000000000
1000000000000000000


# ----------------- 解答時間 ------------------
# 3分でAC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc070/editorial.pdf
# 解説通りだった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#LCM #最小公倍数
