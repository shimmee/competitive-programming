# ABC185
# URL: https://atcoder.jp/contests/abc185/tasks/abc185_c
# 日付: 2020/12/13

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
#

# ------------------- 解答 --------------------
#code:python

n = int(input())
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = combinations_count(n-1, 11)
print(ans)


# ------------------ 入力例 -------------------


# ----------------- 解答時間 ------------------
#

# -------------- 解説 / 感想 / 反省 -------------
#

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい