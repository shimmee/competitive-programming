# ABC207
# URL:
# Date: 2021/06/26

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
tlr = [[int(i) for i in input().split()] for _ in range(n)]
ans = 0
for i in range(n):
    t1, l1, r1 = tlr[i]
    for j in range(i+1, n):
        t2, l2, r2 = tlr[j]

        if t1 == t2 == 1: # ともに閉区間の時
            if (l1 <= l2 and r1 <= r2) or (l2 <= l1 and r2 <= r1) or (l1 <= l2 and r2 <= r1) or (l2 <= l1 and r1 <= r2):
                ans += 1
        if t1 == t2 == 2: #



# ------------------ Sample Input -------------------
3
1 1 2
2 2 3
3 2 4


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
