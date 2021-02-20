# ARC008B - 謎のたこ焼きおじさん
# URL: https://atcoder.jp/contests/arc008/submissions/me
# Date: 2021/02/18

# ---------- Ideas ----------
# nameとkitを両方カウントする
# nameにある文字がkitになければ作れないので-1出力
# nameに”A”が11個必要でkitに"A"が2個あるとき，kitは6個必要，つまりceil(nameの個数/kitの個数)が必要
# この最大値を出力

# ------------------- Answer --------------------
#code:python
import math
n, m = map(int, input().split())
S = input()
T = input()

from collections import Counter

S_count = Counter(S)
T_count = Counter(T)

ans = 0
for s_key, s_value in S_count.items():
    if s_key in T_count:
        ans = max(ans, math.ceil(s_value / T_count[s_key]))
    else:
        print(-1); exit()
print(ans)
# ------------------ Sample Input -------------------
7 26
NAOHIRO
ABCDEFGHIJKLMNOPQRSTUVWXYZ

8 8
TAKOYAKI
TAKOYAKI

8 4
CHOKUDAI
MYON

6 6
MONAKA
NAMAKO

# ----------------- Length of time ------------------
# 4分

# -------------- Editorial / my impression -------------
# 解説ないけど合ってる完璧

# ----------------- Category ------------------
#AtCoder
#Counter
#ceil

