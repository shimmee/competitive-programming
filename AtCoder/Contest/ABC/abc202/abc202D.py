# ABC202
# URL:
# Date: 2021/05/22

# ---------- Ideas ----------


# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from math import factorial
fact = []
for i in range(61):
    fact.append(factorial(i))

A, B, k = map(int, input().split())
ans = ''

cnt = 0
while cnt < k:
    for i in range(A+1): # bのポジション: 何個aが右側に含まれるか
        cnt_next = fact[i+B-1]//(fact[i]*fact[B-1])
        if cnt + cnt_next >= k: # 一番左のbの位置がi+Bに確定
            ans += 'a'*(A-i) + 'b'

            A -= (A-i)
            B -= 1
            break
        else:
            cnt += cnt_next
    if A == 0 or B == 0:
        break
ans += 'a'*A
ans += 'b'*B

print(ans)



# ------------------ Sample Input -------------------
2 2 4

3 3 6

10 10 40

30 30 118264581564861424



# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
