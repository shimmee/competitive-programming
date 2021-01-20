# AGC028A - Two Abbreviations
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc028/tasks/agc028_a
# Date: 2021/01/04

# ---------- Ideas ----------
# Use LCM: length of shortest X is LCM if it exists
# I need condition for violation of the condition
# L = LCM, let's say L = 12, n = 3, m = 4
# X's index at (1, 4, 7, 10) should be S
# X's index at (1, 5, 9) should be T
# So, if some letters are fixed from S at (1,4,7,10) then, letters in these index should be not covered or be consistent with T

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from math import gcd
def lcm_base(x, y):
    return (x * y) // gcd(x, y)

n, m = map(int, input().split())
S = input()
T = input()

lcm = lcm_base(n, m)

n_ = lcm//n
m_ = lcm//m

X = [None]*lcm # X it self
j = 0
for i in range(0, lcm, n_): # Insert each letter in S into X
    X[i] = S[j]
    j += 1
    if j == n:
        break

j = 0
for i in range(0, lcm, m_):
    # If letters in T is not included in X, or consistent with S, then fine.
    if (X[i] is None) or X[i] == T[j]:
        j += 1
    else:
        print('-1')
        exit()

    if j == m:
        break

print(lcm)

# 5つのREが一生取れない
# 多分LCMがでかすぎて(最大で50000**2くらい)，配列Xがメモリオーバーになってる!!!!!!
# He uses completely same method as me: https://atcoder.jp/contests/agc028/submissions/15269652
# He changed from list to dictionary to reduce the memory

from math import gcd
def lcm_base(x, y):
    return (x * y) // gcd(x, y)

n, m = map(int, input().split())
S = input()
T = input()

lcm = lcm_base(n, m)

n_ = lcm//n
m_ = lcm//m

X = {}
j = 0
for i in range(0, lcm, n_):
    X[i] = S[j]
    j += 1

j = 0
for i in range(0, lcm, m_):
    if not i in X or X[i] == T[j]:
        j += 1
    else:
        print('-1')
        exit()
print(lcm)



# ------------------ Sample Input -------------------
1 7
o
abcdefg

1 5
a
fjkrp

2 40
ab
abcdedfbalufgujsbjkvdbjshbvjsbhfjdsbvjfs

4 2
abcd
ab

2 4
ab
abcd

3 2
acp
ae


6 3
abcdef
abc

15 9
dnsusrayukuaiia
dujrunuma


# ----------------- Length of time ------------------
# 1.5 hourrrrrrrrr

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc028/editorial.pdf
# I learned that making huge list (10**10) results in RE error in AtCoder


# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#RE
#復習したい
#medium復習
#wanna_review
