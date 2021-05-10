# 典型90問033 - Not Too Bright
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ag
# Date: 2021/05/09

# ---------- Ideas ----------
# 隅っこから1つ飛ばしで置いていく
# 2*3のときは行に1つ，列に2つおける
# ceil(h/2)とceil(w/2)の和
# 1列のときはコーナーケース: 連続で並んでてOK

# ------------------- Answer --------------------
#code:python
from math import ceil
h, w = map(int, input().split())
if h == 1 or w == 1:
    print(h*w)
else:
    print(ceil(h/2) * ceil(w/2))

# ------------------ Sample Input -------------------
2 3

3 4

1 3
# ----------------- Length of time ------------------
# 4分

# -------------- Editorial / my impression -------------
# みんなWA出したらしい
# 問題が分かりづらい
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/033.jpg

# ----------------- Category ------------------
#AtCoder
#コーナーケース
#ceil