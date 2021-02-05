# DigitalArts プログラミングコンテスト2012A - C-Filter
# URL: https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1
# Date: 2021/02/04

# ---------- Ideas ---------- 
# Sの各単語がn個のNGワードのいずれかに一致していれば，文字数分の***を出力する
# 一致してなければ元の単語を出力
# 一致の判定は，*の箇所を削った文字列が一致してるかどうか

# ------------------- Answer --------------------
#code:python
S = input().split()
n = int(input())
T = [input() for _ in range(n)]

for s in S:
    flag = True # sがいずれかのNGに一致していればFalseにする
    for t in T:
        s_ = ''
        t_ = ''
        if len(s) == len(t): # sとtの長さが違う時は無視: NGは一致しない
            for i in range(len(t)):
                if t[i] != '*':
                    s_ += s[i]
                    t_ += t[i]
            if s_ == t_: # 完全一致しれいれば
                flag = False
    if flag:
        print(s)
    else:
        print('*'*len(s))

# AC!!!!
# 一致の判定でもう少し賢い書き方をしている人がいた: https://atcoder.jp/contests/digitalarts2012/submissions/19834599
# あんまり変わらないか？
S = input().split()
n = int(input())
T = [input() for _ in range(n)]

for s in S:
    flag = True # sがいずれかのNGに一致していればFalseにする
    for t in T:
        if len(s) == len(t): # sとtの長さが違う時は無視: NGは一致しない
            flag2 = True
            for i in range(len(t)):
                if not(t[i] == '*' or t[i] == s[i]): # ここが賢い
                    flag2 = False
            if flag2: # 完全一致しれいれば
                flag = False
    if flag:
        print(s)
    else:
        print('*'*len(s))

# ------------------ Sample Input -------------------
abc aaa ababa abcba abc
2
abc
**a**

# ----------------- Length of time ------------------
# 9分

# -------------- Editorial / my impression -------------
# 解説がないという謎
# 文字列にインクリメント操作しているのにpypyで出してMLEしてしまった
# pythonで提出したらOK
# 昔同じような問題を解いた覚えがある

# ----------------- Category ------------------
#AtCoder  
#文字列操作
#文字列の一致
#
