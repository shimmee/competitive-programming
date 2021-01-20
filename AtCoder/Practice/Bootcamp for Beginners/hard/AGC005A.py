# AGC005A - STring
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/agc005/tasks/agc005_a
# Date: 2021/01/19

# ---------- Ideas ----------
# ARC108B Abbreviate Foxと同じ!

# ------------------- Solution --------------------
# 空のリストYを作って，Xを左から追加していく
# Yの最後の2要素がS,Tなら2つぶんpopしてYから消し去る

# ------------------- Answer --------------------
#code:python
X = input()
X = [i for i in X]
Y = []

for i in range(len(X)):
    x = X[i]
    Y.append(x)

    if len(Y) >= 2:
        if Y[-2] == 'S' and Y[-1] == 'T':
            Y.pop()
            Y.pop()
print(len(Y))

# ------------------ Sample Input -------------------
TSTTSS

SSTTST

TSSTTTSS

# ----------------- Length of time ------------------
# 5分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/data/agc/005/editorial.pdf
# 超定番の問題
# stackを使っていることになるらしい
# カッコ列と同じ問題らしい: https://drken1215.hatenablog.com/entry/2018/06/27/130200

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#文字列操作
#特定の文字を消す
#stack
#カッコ列
#操作を好きな回数だけ行える
#緑diff
#AGC-A


