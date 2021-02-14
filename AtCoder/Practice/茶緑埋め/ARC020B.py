# ARC020B - 縞模様
# URL: https://atcoder.jp/contests/arc020/tasks/arc020_2
# Date: 2021/02/13

# ---------- Ideas ----------
# N<=100なので，2色の色を決め打ちして全探索が楽かな
# 同じ色がだめな点に注意

# ------------------- Answer --------------------
#code:python
n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]

ans = 10**20
for i in range(1, 11): # 偶数番目の色
    for j in range(1, 11): # 奇数番目の色
        if i == j: continue # 同じ色はダメ
        cnt = 0
        for k in range(n):
            if k % 2 == 0: # 偶数番目のマス
                if a[k] != i:
                    cnt += 1
            else: # 奇数番目のマス
                if a[k] != j:
                    cnt += 1
        ans = min(ans, cnt*c)
print(ans)

# ------------------ Sample Input -------------------
3 10
3
2
1

10 1000
1
2
3
4
5
6
7
8
9
10


# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc020
# 想定解法と同じだったけど，もう少し綺麗にかけそう

# ----------------- Category ------------------
#AtCoder
#全探索
#縞模様
#交互に色を変える