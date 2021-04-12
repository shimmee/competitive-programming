# ABC198D - Send More Money
# URL: https://atcoder.jp/contests/abc198/tasks/abc198_d
# Date: 2021/04/11

# ---------- Ideas ----------
# 覆面算
# 本番はググりまくってWA出しまくってACできなかった
# 冷静に問題を読めば単純な順列全探索ということに気付く...

# ------------------- Solution --------------------
# まずは出現した文字の種類を数える
# 文字の種類に応じて，0から9までの数字を割り当てる全探索をitertools.permutations()で行う
# ちゃんと数式が一致していればOK

# ------------------- Answer --------------------
#code:python
from itertools import combinations, permutations
S = [input() for _ in range(3)]
letter = list(set([i for i in S[0]] + [i for i in S[1]] + [i for i in S[2]]))
letter = ''.join([str(i) for i in letter])
m = len(letter)

if m > 10 or S[0] == S[2] or S[1] == S[2]:
    print('UNSOLVABLE')
    exit()

for pattern in permutations(range(10), m):
    # pattern = ''.join([str(i) for i in pattern])
    # trans = str.maketrans(letter, pattern)

    s1 = ''.join([str(pattern[letter.index(S[0][i])]) for i in range(len(S[0]))])
    s2 = ''.join([str(pattern[letter.index(S[1][i])]) for i in range(len(S[1]))])
    s3 = ''.join([str(pattern[letter.index(S[2][i])]) for i in range(len(S[2]))])

    # s1 = S[0].translate(trans)
    # s2 = S[1].translate(trans)
    # s3 = S[2].translate(trans)

    if s1[0] == '0' or s2[0] == '0' or s3[0] == '0':
        continue

    if int(s1) + int(s2) == int(s3) and int(s1) > 0 and int(s2) > 0 and int(s3) > 0:
        print(s1, s2, s3)
        exit()
        break
print('UNSOLVABLE')

# ------------------ Sample Input -------------------
p
q
p

send
more
money

a
b
c

# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# 本番終わってとき解説みて解き直した
# maketrans()を使うとなぜかTLEになって結局原因がわからなかった
#

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#覆面算
#順列全探索
#10の階乗
#制限時間5秒
#水色diff