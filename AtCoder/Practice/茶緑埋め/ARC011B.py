# ARC011B - ルイス・キャロルの記憶術
# URL: https://atcoder.jp/contests/arc011/tasks/arc011_2
# Date: 2021/02/21

# ---------- Ideas ----------
# 母音とピリオド，カンマを消す
# スペースで区切る
# 翻訳する。終わり

# ------------------- Answer --------------------
#code:python
import re
trans = {'b': 1, 'c': 1,
         'd': 2, 'w': 2,
         't': 3, 'j': 3,
         'f': 4, 'q': 4,
         'l': 5, 'v': 5,
         's': 6, 'x': 6,
         'p': 7, 'm': 7,
         'h': 8, 'k': 8,
         'n': 9, 'g': 9,
         'z': 0, 'r': 0}
n = int(input())
S = input()
S = re.sub('a|i|u|e|o|y|A|I|U|E|O|Y|,|\\.', '', S)
S = S.split()

T = []
for s in S:
    t = ''
    for i in s.lower():
        t += str(trans[i])
    T.append(t)
print(*T)

# ------------------ Sample Input -------------------
3
Mozart plays magic.

7
I have a scissors for right hand.


3
Columbus found USA.

# ----------------- Length of time ------------------
# 7分

# -------------- Editorial / my impression -------------
# 辞書作るのが面倒だった
# str.maketransでも行けたっぽい

# ----------------- Category ------------------
#AtCoder
#str.maketrans
#翻訳
#文字列操作

