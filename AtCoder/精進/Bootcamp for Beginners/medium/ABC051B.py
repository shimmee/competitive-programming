# ABC051B - Sum of Three Integers
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc051/tasks/abc051_b
# Date: 2021/01/09

# ---------- Ideas ---------- 
# O(K^2)でとく, K< 2500

# ------------------- Solution -------------------- 
# xとyで全探索
# z = s-x-yが0以上，k以下ならインクリメント

# ------------------- Answer --------------------
#code:python
k, s = map(int, input().split())
ans = 0
for x in range(k+1):
    for y in range(k+1):
        z = s-x-y
        if 0 <= z <= k:
            ans += 1
print(ans)

# ------------------ Sample Input -------------------
2 2

5 15


# ----------------- Length of time ------------------
# 4分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc051/editorial.pdf
# 一番面白くない全探索！

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-medium
#全探索