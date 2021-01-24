# ABC189D -
# URL: https://atcoder.jp/contests/abc189/tasks/abc189_d
# Date: 2021/01/23

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
# andが続くなら
# 各(... and ... and ...)がTrueとfalseになりうる回数

# ------------------- Answer --------------------
#code:python
n = int(input())
p = ''
for _ in range(n):
    s = input()
    if s == 'AND':
        p += '0'
    else:
        p += '1'

p = '1' + p
print(int(p[::-1], 2))



# ------------------ Sample Input -------------------
2
AND
OR

5
OR
OR
OR
OR
OR


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#ABC-D