# ABC198C - Compass Walking
# URL: https://atcoder.jp/contests/abc198/tasks/abc198_c
# Date: 2021/04/11

# ---------- Ideas ----------
# 長さが届けばできるやつ: 長さ調整してどうにかできる
#
# 誤差問題か？
# ルートつけないように整数のまま計算するやつか？

# ------------------- Answer --------------------
#code:python
# sqrt(x^2+y^2) < k*r とはじめてなるようなkを線形時間で探す
r ,x ,y = map(int, input().split())
a = (x**2 + y**2)**0.5

if a < r:
    print(2)
    exit()

ans = 0
while ans * r < a:
    ans += 1
print(ans)

# WA出しまくったけど結局AC: forをwhileにした
# こんなことしなくてもceilで解けた...

import math
r ,x ,y = map(int, input().split())
a = (x**2 + y**2)**0.5

if a < r:
    print(2)
elif a == r:
    print(1)
else:
    print(math.ceil(a/r))

# ------------------ Sample Input -------------------
2 2 0
100 1 1

5 15 0

3 4 4

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
# WA出しまくった...
# これが早く解けなくてDとか解き始めたせいでレートが30くらい下がった...

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#長さが届きさえすれば調整できてOKな問題
#ロボットアーム問題
#座標問題
#ユークリッド距離