# diverta 2019 Programming Contest:C - AB Substrings
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c
# Date: 2021/01/14

# ---------- Ideas ---------- 
# Aで終わってBで始まるものをくっつければ，ABが1つ増える
# 各sに入ってるABを数える
# (1) B....A  (Bで始まってAで終わる文字列)
# (2) B....?  (Bで始まってA以外で終わる文字列)
# (3) ?....A，を数える
# (1)と(2) or (1)と(3)を結合してABをインクリメントして，(2)と(3)にしていく

# ------------------- Solution -------------------- 
# 

# ------------------- Answer --------------------
#code:python
n = int(input())
AB_cnt = 0
start_B_end_A = 0
start_B = 0
end_A = 0
for _ in range(n):
    s = input()
    m = len(s)
    for i in range(m-1):
        if s[i] + s[i+1] == 'AB':
            AB_cnt += 1
    if s[0] == 'B' and s[-1] == 'A':
        start_B_end_A += 1
    if s[0] != 'B' and s[-1] == 'A':
        end_A += 1
    if s[0] == 'B' and s[-1] != 'A':
        start_B += 1


if start_B > 0 or end_A > 0:
    while start_B_end_A > 0: # A...Bを結合してなくす

        if start_B > 0: # B...A + B...? = B...?
            start_B_end_A -= 1
            AB_cnt += 1
        if start_B_end_A == 0:
            break

        if end_A > 0: # ?...A + B...A = ?...A
            start_B_end_A -= 1
            AB_cnt += 1
else: # A...Bしかない場合
    AB_cnt += max(0, start_B_end_A-1)

# ?...B と A...?の組ができる分だけ結合してABを作る
AB_cnt += min(end_A, start_B)

print(AB_cnt)



# きれいに書いてみる
n = int(input())
cnt = 0
ab = 0
a, b = 0, 0
for _ in range(n):
    s = input()
    m = len(s)
    for i in range(m-1):
        if s[i] + s[i+1] == 'AB':
            cnt += 1
    if s[0] == 'B' and s[-1] == 'A': ab += 1
    if s[0] != 'B' and s[-1] == 'A': a += 1
    if s[0] == 'B' and s[-1] != 'A': b += 1


if b > 0 or a > 0:
    while ab > 0: # A...Bを結合してなくす

        if b > 0: # B...A + B...? = B...?
            ab -= 1
            cnt += 1
        if ab == 0:
            break

        if a > 0: # ?...A + B...A = ?...A
            ab -= 1
            cnt += 1
else: # A...Bしかない場合
    cnt += max(0, ab-1)

# ?...B と A...?の組ができる分だけ結合してABを作る
cnt += min(a, b)

print(cnt)


# ------------------ Sample Input -------------------
3
ABCA
XBAZ
BAD

9
BEWPVCRWH
ZZNQYIJX
BAVREA
PA
HJMYITEOX
BCJHMRMNK
BP
QVFABZ
PRGKSPUNA

7
RABYBBE
JOZ
BMHQUVA
BPA
ISU
MCMABAOBHZ
SZMEHMA

# ----------------- Length of time ------------------
# 39分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/diverta2019/editorial.pdf
# 楽しかった
# ちょっと時間かかりすぎたけどまあいいや

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#文字列操作
