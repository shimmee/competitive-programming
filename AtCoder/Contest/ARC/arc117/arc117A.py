# ARC117A -
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
A, B = map(int, input().split())

if A >= B:
    a = [i for i in range(2, A*2+1, 2)]
    b = [-i for i in range(1, B*2-1, 2)]
    b.append(-(sum(a)+sum(b)))
    ans = sorted(a+b)
    print(*ans)
else:
    b = [-i for i in range(2, B*2+1, 2)]
    a = [i for i in range(1, A*2-1, 2)]
    a.append(-(sum(a)+sum(b)))
    ans = sorted(a+b)
    print(*ans)


# ------------------ Sample Input -------------------
5 5

1 20

7 5

5 7


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
