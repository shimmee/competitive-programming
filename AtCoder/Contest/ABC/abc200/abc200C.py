# ABC200C - Ringo's Favorite Numbers 2
# URL: https://atcoder.jp/contests/abc200/tasks/abc200_c
# Date: 2021/05/08

# ---------- Ideas ----------
# Zero-sum rangesやcandi distributionと同じ
# 余りを出して同じあまりなら組み合わせられるやつ
# 超典型

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

from collections import deque, Counter

per = [i%200 for i in a]
counter = Counter(per)
ans = 0
for key, value in counter.items():
    if value >= 2:
        ans += value*(value-1)//2
print(ans)



# ------------------ Sample Input -------------------
6
123 223 123 523 200 2000

8
199 100 200 400 300 500 600 200

# ----------------- Length of time ------------------
# 2分

# -------------- Editorial / my impression -------------
# 本番でここまで8分で通せたので1100パフォ出せた

# ----------------- Category ------------------
#AtCoder
#Zero-sum-ranges
#Counter