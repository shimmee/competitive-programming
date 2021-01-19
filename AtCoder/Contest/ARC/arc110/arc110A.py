# ARC110A - Redundant Redundancy
# URL: https://atcoder.jp/contests/arc110/tasks/arc110_a
# 日付: 2020-12-05

# ---------- 思ったこと / 気づいたこと ----------
# 最大公約数

# ------------------- 方針 --------------------
# LCM+1が答えになりそう

# ------------------- 解答 --------------------
#code:python

from math import gcd   #will work for an int array of any length
n = int(input())
l = [i for i in range(2, n+1)]

lcm = l[0]
for i in l[1:]:
  lcm = lcm*i//gcd(lcm, i)
print(lcm+1)

# ------------------ 入力例 -------------------
3
10

# ----------------- 解答時間 ------------------
# 10分くらい

# -------------- 解説 / 感想 / 反省 -------------
# https://atcoder.jp/contests/arc110/editorial/382
# 簡単だった！
# 灰色問題

# ----------------- カテゴリ ------------------
#AtCoder #arc
#LCM
#最小公倍数