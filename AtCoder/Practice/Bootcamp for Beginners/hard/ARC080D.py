# ARC080D - Grid Coloring
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/arc080/tasks/arc080_b
# Date:2021/01/19


# ---------- Ideas ----------
# ジグザグにすればいい

# ------------------- Solution --------------------
# aを展開する: [1,2,3]なら[1,2,2,3,3,3]みたいに
# 1次元のaを二次元に変換する: h*w
# 奇数番目をreverseする

# ------------------- Answer --------------------
#code:python
h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b += [i+1 for _ in range(a[i])]

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

b = convert_1d_to_2d(b, w)
for i in range(h):
    if i % 2:
        b[i] = b[i][::-1]

for i in b:
    print(*i)
    
# ------------------ Sample Input -------------------
2 2
3
2 1 1

3 5
5
1 2 3 4 5

1 1
1
1


# ----------------- Length of time ------------------
# 12分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/arc080/editorial.pdf

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#ジグザグ
#グリッド
#grid
