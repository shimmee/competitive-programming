# ABC190A -
# URL: https://atcoder.jp/contests/abc189/tasks/abc189_a
# Date: 2021/01/30

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
a, b, c = map(int, input().split())
if c == 0:
    if a > b:
        print('Takahashi')
    else:
        print('Aoki')
else:
    if a < b:
        print('Aoki')
    else:
        print('Takahashi')

# ------------------ Sample Input -------------------


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#ABC-A