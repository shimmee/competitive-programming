# ABC201 -
# URL:
# Date: 2021/05/15

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
st = []
for _ in range(n):
    s, t = input().split()
    st.append([int(t), s])

st = sorted(st, reverse=True)
print(st[1][1])

# ------------------ Sample Input -------------------
3
Everest 8849
K2 8611
Kangchenjunga 8586


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
