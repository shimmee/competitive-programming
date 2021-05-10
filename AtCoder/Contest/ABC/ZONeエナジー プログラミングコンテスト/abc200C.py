# ZONeエナジー プログラミングコンテスト C
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
score = [[int(i) for i in input().split()] for _ in range(n)]

score

for i in range(n):
    for j in range(i+1, n):
        a = max([score[i][0], score[j][0]])
        b = max([score[i][1], score[j][1]])
        c = max([score[i][2], score[j][2]])
        d = max([score[i][3], score[j][3]])
        e = max([score[i][4], score[j][4]])

        a,b,c,d,e




# ------------------ Sample Input -------------------
3
3 9 6 4 6
6 9 3 1 1
8 8 9 3 7


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
