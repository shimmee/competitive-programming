# ABC201 -
# URL:
# Date: 2021/05/15

# ---------- Ideas ----------
# itertoolsで全組み合わせ作って殴る

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from itertools import combinations_with_replacement, permutations
s = input()
maru = [i for i in range(10) if s[i] == 'o']
hate = [i for i in range(10) if s[i] == '?']

if len(maru) > 4:
    print(0)
    exit()
elif s == 'x'*10:
    print(0)
    exit()

m_maru = len(maru)
m_hate = 4 - len(maru)
ans = 0

all_hate = list(combinations_with_replacement(maru+hate, m_hate))
all_pattern = []
for comb_hate in all_hate:
    comb = list(comb_hate) + maru
    all_pattern += list(permutations(comb))
print(len(set(all_pattern)))

# ACしたけど10000まで全探索すればいいだけだった

s = input()
ans = 0
for n in range(10000):
    n = str(n).zfill(4)
    flag = True
    for i in range(10):
        if s[i] == 'o':
            if not str(i) in n:
                flag = False
        elif s[i] == 'x':
            if str(i) in n:
                flag = False
    if flag:
        ans += 1
print(ans)






# ------------------ Sample Input -------------------
ooo???xxxx

xxxxx?xxxo

xxxxxxxxxo

??????????

# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
