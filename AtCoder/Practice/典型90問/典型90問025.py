# 典型90問025 - Digit Product Equation
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_y
# Date: 2021/04/27

# ---------- Ideas ----------
# 解説ACです
# mは桁の中身を入れ替えても同じなので，桁数を固定して，0~9までの数字を順番に入れて全探索する
# 重複組合せになる.
# itertools.combinations_with_replacementでできる
# many requirementsと同じ問題になる

# ------------------- Answer --------------------
#code:python
from functools import reduce  # Required in Python 3
import operator
def prod(iterable):
    return reduce(operator.mul, iterable, 1)

from itertools import combinations_with_replacement
from math import prod

n, b = map(int, input().split())

cnt = 0
for p in range(1, len(str(n))+1): # 桁の長さ
    all_pattern = list(combinations_with_replacement(range(10), p))
    for pattern in all_pattern:
        m = b + prod(pattern)
        if tuple(sorted([int(i) for i in str(m)])) == pattern:
            if m <= n:
                cnt += 1
print(cnt)



# ------------------ Sample Input -------------------
999 434

255 15

# ----------------- Length of time ------------------
# 解説AC15分

# -------------- Editorial / my impression -------------
# 考察の部分が思いつかなかった
# 再帰関数書かなくていいからcombinations_with_replacement大好き

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#combinations_with_replacement
#重複組合せ
#組み合わせ全探索
#再帰関数