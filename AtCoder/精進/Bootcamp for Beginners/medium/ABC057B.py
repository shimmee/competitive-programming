# ABC057B - Checkpoints
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc057/tasks/abc057_b
# 日付: 2020/12/29

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 50なので二重る−う

# ------------------- 解答 --------------------
#code:python

n, m = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(n)]
cd = [[int(i) for i in input().split()] for _ in range(m)]

for i in range(n):
    a, b = ab[i]
    dist = 10**10
    for j in range(m):
        c, d = cd[j]

        d = abs(a-c) + abs(b-d)
        if d < dist:
            dist = d
            idx = j+1
    print(idx)

# ------------------ 入力例 -------------------
2 2
2 0
0 0
-1 0
1 0

3 4
10 10
-10 -10
3 3
1 2
2 3
3 5
3 5

5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000

# ----------------- 解答時間 ------------------
#  4分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc057/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
