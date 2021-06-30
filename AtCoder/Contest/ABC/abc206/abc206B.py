# ABC206
# URL:
# Date: 2021/06/19

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
cnt = 0
i = 1
while True:
    cnt += i
    if cnt >= n:
        print(i)
        exit()
        break
    i += 1


# ------------------ Sample Input -------------------
12

100128

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
