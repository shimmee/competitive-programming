# ABC187C - 1-SAT
# URL: https://atcoder.jp/contests/abc187/tasks/abc187_c
# Date: 2021/01/02

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
S = [input() for _ in range(n)]

l1 = set([]) # !なし
l2 = set([])

for i in range(n):
    s = S[i]
    if s[0] != '!':
        l1.add(s)
    if s[0] == '!':
        s = s[1:]
        l2.add(s)

for word in l1:
    if word in l2:
        print(word)
        exit()
print('satisfiable')

# ------------------ Sample Input -------------------
6
a
!a
b
!c
d
!d

10
red
red
red
!orange
yellow
!blue
cyan
!green
brown
!gray

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#ABC187
#ABC-C
#AC_with_editorial #解説AC
