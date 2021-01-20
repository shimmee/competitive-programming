# AGC011B - Colorful Creatures
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc011/tasks/agc011_b
# Date: 2021/01/15

# ---------- Ideas ---------- 
# 一番大きい数字は必ず生き残れる
# どの数字も，とりあえず自分より小さい数字を全部吸収してから，大きい数字を吸収していけばいい

# ソートしてからAの累積和とAのを比べる
# 累積和の項*2がAより大きかったら，そのiは生き残れる。小さかったら，そのiより小さいものは無理

# ------------------- Solution -------------------- 
# 

# ------------------- Answer --------------------
#code:python
from itertools import accumulate
n = int(input())
A = list(map(int, input().split()))
A.sort()
cum = list(accumulate(A))

A = A[1:] # 最初は使わない
cum = cum[:-1] # 最後は使わない

ans = 1
for i in reversed(range(n-1)):
    if 2*cum[i] >= A[i]:
        ans += 1
    else:
        break
print(ans)

# ------------------ Sample Input -------------------
3
3 1 4

5
1 1 1 1 1

6
40 1 30 2 7 20


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc011/editorial.pdf
# 最後の部分は線形探索で間に合うので楽

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#累積和
#貪欲
#greedy
#cumsum
