# ABC118C - Monsters Battle Royale
# URL: https://atcoder.jp/contests/abc118/tasks/abc118_c
# 日付: 2020/12/01

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# わからん。全くわからん。

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

# 1日考えてわからなかった
# けんちょんブログから最大公約数というヒントを得た
import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

print(gcd_list(a))

# ------------------ 入力例 -------------------
4
2 10 8 40

4
5 13 8 1000000000

3
1000000000 1000000000 1000000000

# ----------------- 解答時間 ------------------
# わからずけんちょんブログみた

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc118/editorial.pdf
# 全く気づかなかった，悔しい

# ----------------- カテゴリ ------------------
#AtCoder #abc
#最大公約数
#GCD
