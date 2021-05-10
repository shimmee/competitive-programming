# ZONeエナジー プログラミングコンテスト D
# URL:
# Date:

# ---------- Ideas ----------
#

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
S = input()

back = 1 # 末尾につけるか頭か
T = deque([])
for s in S:

    if s == 'R':
        back = 1 - back
    else:
        if back == 1:
            if T and T[-1] == s:
                T.pop()
            else:
                T.append(s)
        else:
            if T and T[0] == s:
                T.popleft()
            else:
                T.appendleft(s)

print(''.join(T) if back == 1 else ''.join(list(T)[::-1]))


# ------------------ Sample Input -------------------
ozRnonnoe

hellospaceRhellospace


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
