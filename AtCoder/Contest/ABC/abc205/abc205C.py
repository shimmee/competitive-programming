#
# URL:
# Date: 2021/06/13

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
a, b, c = map(int, input().split())
if c % 2 == 0:
    if abs(a) == abs(b): print('=')
    elif abs(a) > abs(b): print('>')
    else: print('<')
else:
    if a == b: print('=')
    elif a > b: print('>')
    else: print('<')



a, b, c = map(int, input().split())
if a**c > b**c:
    print('>')
elif a**c < b**c:
    print('<')
else:
    print('=')


# ------------------ Sample Input -------------------
5
3 1 2 4 5

6
3 1 4 1 5 2


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
