# ABC199C -
# URL:
# Date: 2021/04/24

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

n = int(input())
n = 2*n
m = n//2
S = input()
q = int(input())

S = [s for s in S]
S1 = S[:m]
S2 = S[m:]

flag = True # 前半と後半の順番

for _ in range(q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if flag:  # S1 -> S2のとき
            if b <= m-1: # aとbが前半S1側
                S1[a], S1[b] = S1[b], S1[a]
            elif m <= a: # aとbが後半S2側
                S2[a-m], S2[b-m] = S2[b-m], S2[a-m]
            else: # aとbがS1, S2にまたがるとき
                S1[a], S2[b-m] = S2[b-m], S1[a]
        else: # S2 -> S1のとき
            if b <= m-1: # aとbが前半S2側
                S2[a], S2[b] = S2[b], S2[a]
            elif m <= a: # aとbが後半S1側
                S1[a-m], S1[b-m] = S1[b-m], S1[a-m]
            else: # aとbがS2, S1にまたがるとき
                S2[a], S1[b-m] = S1[b-m], S2[a]
    else:
        flag = not flag

if flag:
    print(''.join(S1+S2))
else:
    print(''.join(S2+S1))






# ------------------ Sample Input -------------------
2
FLIP
2
2 0 0
1 1 4

2
FLIP
6
1 1 3
2 0 0
1 1 2
1 2 3
2 0 0
1 1 4

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
