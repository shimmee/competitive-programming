# CODE FESTIVAL 2015 予選B: B - 採点
# URL: https://atcoder.jp/contests/code-festival-2015-qualb/tasks/codefestival_2015_qualB_b
# Date: 2021/02/08

# ---------- Ideas ----------
# Counterのmost_commonで出現回数の最大のものを得る

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
d = Counter(a)
common = d.most_common()
if common[0][1] > n//2:
    print(common[0][0])
else:
    print('?')

# ------------------ Sample Input -------------------
3 2
2 1 2

4 2
2 1 2 1

10 5
0 1 2 3 4 5 5 5 5 5

# ----------------- Length of time ------------------
# 4分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/code-festival-2015-qualb
# よいです。

# ----------------- Category ------------------
#AtCoder
#Counter