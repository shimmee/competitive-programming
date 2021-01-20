# CODE FESTIVAL 2017 qual B: B - Problem Set
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/code-festival-2017-qualb/tasks/code_festival_2017_qualb_b
# 日付: 2020/12/29

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# counterつかう

# ------------------- 解答 --------------------
#code:python
from collections import Counter
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

dist_d = Counter(d)
dist_t = Counter(t)

flag = True
for key, value in dist_t.items():
    if dist_d[key] >= value: continue
    else: flag = False
if flag: print('YES')
else: print('NO')

# ------------------ 入力例 -------------------
5
3 1 4 1 5
3
5 4 3

7
100 200 500 700 1200 1600 2000
6
100 200 500 700 1600 1600

1
800
5
100 100 100 100 100


15
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
9
5 4 3 2 1 2 3 4 5

# ----------------- 解答時間 ------------------
# 4分

# -------------- 解説 / 感想 / 反省 -------------
#

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
