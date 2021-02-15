# ARC009B - おとぎの国の高橋君
# URL: https://atcoder.jp/contests/arc009/tasks/arc009_2
# Date: 2021/02/14

# ---------- Ideas ----------
# アルファベットに当てはめて変換して，ソートして戻せば良さそう

# ------------------- Solution --------------------
# aからjまでのアルファベットを入力のの数字の順番に対応させて辞書つくる
# 出力対象のn個の数列にアルファベットを対応させてリストつくる
# 桁数ごとにソートする
# ソートされた順番に，アルファベットを数字に戻して出力する

# ------------------- Answer --------------------
#code:python
b = list(map(int, input().split()))
n = int(input())
A = [int(input()) for _ in range(n)]

import string
alpha = list(string.ascii_lowercase)[:10]
dic1 = {key: val for key, val in zip(b, alpha)}
dic2 = {key: val for key, val in zip(alpha, b)}

A_alpha = []
for a in A:
    a_alpha = ''
    for s in str(a):
        a_alpha += dic1[int(s)]
    A_alpha.append(a_alpha)

# 桁数ごとにソート
A_alpha_sort = []
for i in range(1, max([len(i) for i in A_alpha])+1):
    tmp = []
    for s in A_alpha:
        if len(s) == i:
            tmp.append(s)
    tmp.sort()
    A_alpha_sort += tmp


for S in A_alpha_sort:
    a_int = ''
    for s in S:
        a_int += str(dic2[s])
    print(a_int)

# アルファベットに変換するという方法で無理やりACした
# str.maketrans()という便利なものがあるっぽい
# 参考解答: https://atcoder.jp/contests/arc009/submissions/20118748

# str.maketrans()の使い方1
s = 'ABCABC'
trans = str.maketrans({'A': '_', 'B': '.'})
s.translate(trans)

# str.maketrans()の使い方2
t1 = 'abcdefg'
t2 = 'zyuwlpq'
str.maketrans(t1, t2)

###################################
# str.maketrans()でやってみる
b = input().replace(' ','')
n = int(input())
A = [int(input()) for _ in range(n)]

trans = str.maketrans(b, '0123456789')
rtrans = str.maketrans('0123456789', b)

A_trans = []
for a in A:
    A_trans.append(int(str(a).translate(trans)))

A_trans.sort()

for a in A_trans:
    print(str(a).translate(rtrans))

# ------------------ Sample Input -------------------
0 8 1 3 5 4 9 7 6 2
10
1
2
3
4
5
6
7
8
9
10

# ----------------- Length of time ------------------
# 16分

# -------------- Editorial / my impression -------------
# 実装がアホみたいに長くなった
# str.maketrans()という便利関数を学んだ
# 結局やってることは，アルファベットに変換，ではなくて現実世界の数字に変換してるだけだった

# ----------------- Category ------------------
#AtCoder
#str.maketrans
#文字列操作
#翻訳
#wanna_review #hard復習 #復習したい
