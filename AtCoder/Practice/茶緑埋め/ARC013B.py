# ARC013B - 引越しできるかな？
# URL: https://atcoder.jp/contests/arc013/tasks/arc013_2
# Date: 2021/02/15

# ---------- Ideas ----------
# 全荷物の最大の辺は，ダンボールの1辺として必要
# 他の2辺は，各ダンボールの3辺をソートして，1番目に短いもの，2番目に短いもの，のうち最大のものが必要になるので更新していく

# ------------------- Answer --------------------
#code:python
C = int(input())
boxes = [[int(i) for i in input().split()] for _ in range(C)]

max_len = max(map(max, boxes))
len1 = 0
len2 = 0
for box in boxes:
    box.sort()
    len1 = max(len1, box[0])
    len2 = max(len2, box[1])
print(max_len*len1*len2)

# ------------------ Sample Input -------------------
2
10 20 30
20 20 20

3
10 20 30
20 20 20
30 20 10


# ----------------- Length of time ------------------
# 9分

# -------------- Editorial / my impression -------------
# https://kmjp.hatenablog.jp/entry/2013/03/23/0900
# 3辺ソートして，それぞれ一番長いのを取ってくればいいだけだった

# ----------------- Category ------------------
#AtCoder
#ソート
