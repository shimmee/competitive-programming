# 典型90問024 - Select +／- One
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_x
# Date: 2021/05/09

# ---------- Ideas ----------
# 各iごとの差の総和がK以下でかつ，差の総和とKの偶奇が一致すればいける

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

gap_sum = sum([abs(A[i]-B[i]) for i in range(n)])
if gap_sum <= k and gap_sum % 2 == k % 2:
    print('Yes')
else:
    print('No')

# ------------------ Sample Input -------------------
2 5
1 3
2 1


# ----------------- Length of time ------------------
# 3分

# -------------- Editorial / my impression -------------
# さすがにパリティにはなれてきたね
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/024.jpg

# ----------------- Category ------------------
#AtCoder
#偶奇に注目
#パリティ
#典型90問