# ARC113B - A^B^C
# URL: https://atcoder.jp/contests/arc113/tasks/arc113_b
# Date: 2021/02/21

# ---------- Ideas ----------
# これを貼り付けた: https://stackoverflow.com/questions/33765667/last-digit-of-abc

# ------------------- Answer --------------------
#code:python
mod2mod5_to_mod10 = [[0 for i in range(5)] for j in range(2)]
for i in range(10):
    mod2mod5_to_mod10[i % 2][i % 5] = i

[a,b,c] = map(int, input().split())

if a % 5 == 0:
    abcmod5 = 0
else:
    bmod4 = b % 4
    if bmod4  == 0 or bmod4 == 1:
        bcmod4 = bmod4
    elif bmod4 == 2:
        if c == 1:
            bcmod4 = 2
        else:
            bcmod4 = 0
    else:
        if c % 2 == 0:
            bcmod4 = 1
        else:
            bcmod4 = 3

    abcmod5 = ((a % 5)**bcmod4) % 5

abcmod2 = a % 2

abcmod10 = mod2mod5_to_mod10[abcmod2][abcmod5]

print(abcmod10)

# ------------------ Sample Input -------------------
2 2 2

1 2 3
4 3 2

3141592 6535897 9323846


# ----------------- Length of time ------------------
# 30分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc113/editorial
# 調べて見つけるまでに時間が結構かかった
# 周期4だから，modで上手いこと解けるらしい

# ----------------- Category ------------------
#AtCoder
#ARC-B
#周期性
#mod
#整数問題
#茶diff
#