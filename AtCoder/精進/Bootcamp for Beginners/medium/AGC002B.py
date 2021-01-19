# AGC002B - Box and Ball
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc002/tasks/agc002_b
# Date: 2021/01/09


# ------------------- Solution -------------------- 
# 可能性のある箱のflagのリスト
# ボールの数のリスト
# 箱xにボールが1つの場合には，箱xに赤玉が入っている可能性がなくなり，yの可能性ができる
# 2つ以上の場合には，単純にyの可能性が増えるだけ

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())
flag = [False]*(n+1) # 赤玉の可能性のフラッグ
flag[1] = True
ball = [1]*(n+1)

now = 1 # 必ず赤玉が1つ入っている場所がわかっていれば，このインデックスの箱

for _ in range(m):
    x, y = map(int, input().split())

    # xに赤玉がある可能性があって
    if flag[x]:
        if ball[x] == 1: # かつボールが1つなら
            flag[y] = True # yに可能せいが生まれて
            flag[x] = False # xに赤玉がある可能性がなくなる
        else: # かつボールが2つ以上なら
            if flag[x]:
                flag[y] = True

    ball[x] -= 1
    ball[y] += 1
print(sum(flag))

# ------------------ Sample Input -------------------
3 2
1 2
2 3

3 3
1 2
2 3
2 3


4 4
1 2
2 3
4 1
3 4

# ----------------- Length of time ------------------
# 21分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/agc/002/editorial.pdf
# completely same answer with the editorial

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-medium
