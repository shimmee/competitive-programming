# ABC115C - Christmas Eve
# URL: https://atcoder.jp/contests/abc115/tasks/abc115_c
# 日付: 2020/11/28


# ------------------- 方針 --------------------
# ソートしてK本ずつをループで取っていく

# ------------------- 解答 --------------------
#code:python
n,k=map(int, input().split())
h=[int(input()) for _ in range(n)]
h.sort()
ans = 10**20
for i in range(n-k+1):
    ans = min(ans, abs(h[i]-h[i+k-1]))
print(ans)
# ------------------ 入力例 -------------------
5 3
10
15
11
14
12

5 3
5
7
5
7
7

# ----------------- 解答時間 ------------------
# 7分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc115/editorial.pdf

# ----------------- カテゴリ ------------------
#AtCoder #abc
#ソートして貪欲
