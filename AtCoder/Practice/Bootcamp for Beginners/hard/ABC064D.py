# ABC064D - Insertion
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc064/tasks/abc064_d
# Date: 2021/01/17

# ---------- Ideas ---------- 
# 左から見ていって
# (があったら，)が来るまでor文字列が終わるまで，連続する(を数える。(に対する数の)があればOK。足りなかったら右に足す
# )があったら，(が来るまでor文字列が終わるまで，連続する)を数える。一番左に対応する数の(をくっつける

# 辞書順にするには，必要な(は左端に，)は右端に持ってくる
# (のあとには必ず同じ数の)が必要

# ------------------- Solution -------------------- 
# 

# ------------------- Answer --------------------
#code:python
n = int(input())
S = input()
T = ''
i = 0
while i < n:
    now = S[i]
    flag = False
    if now == '(':
        cnt_left = 0
        for j in range(i, n):
            if S[j] == '(': cnt_left += 1
            else: flag=True; break # S[j]には)が入ってる


        T += '('*cnt_left
        T += ')' * cnt_left

        if not flag and j == n-1:
            break

        for k in range(j, min(j+cnt_left, n)):
            if S[k] == '(': break
        i = k+1

    else: # i番目が)のとき
        cnt_right = 0
        for j in range(i, n):
            if S[j] == ')': cnt_right += 1
            else: flag = True; break

        T += ')' * cnt_right
        T = '(' * cnt_right + T

        if not flag and j == n-1:
            break

        i = j

print(T)

# 5/12 WA
# 900give up
# itertools.groupbyで再チャレンジ

from itertools import groupby
n = int(input())
S = input()

gr = groupby(S)
l = []
for key, group in gr:
    l.append([key, len(list(group))])

T = ''
m = len(l)
i=0
while i < m:
    dir1, cnt1 = l[i]
    if dir1 == '(':
        T += '('*cnt1
        T += ')'*cnt1
        if i == m-1: break
        dir2, cnt2 = l[i + 1]
        if cnt2 > cnt1:
            l[i + 1] = [dir2, cnt2-cnt1]
            i += 1
        else:
            i += 2
    else:
        T += ')' * cnt1
        T = '(' * cnt1 + T
        i += 1
print(T)
# 最初の解き方と同じく5つWA！！
# なんでWAなのかわからなくて気持ち悪いけど，正攻法の解き方があるらしいから，今回は諦めてそちらを学ぶ
# 解答:
# 左から見ていった時に「(の個数」ー「)の個数」が負にならず、最後までいくと0になれば、括弧列です。

# 類題AGC005Aのけんちょんさん解説: https://drken1215.hatenablog.com/entry/2018/06/27/130200
# わかりやすい解説: https://hiro-kato.hatenablog.jp/entry/2019/06/24/230019

# pointer=0とneed_left=0を用意。
# Sの左からループを回しながら，pointerで'('の個数を数えていって，')'が来たら減らすという作業
# pointerが0のときに')'が来たら，'('が足りないことになるので，左端に'('が必要になるので，need_leftに1インクリメント
# 最終的にpointerが正の値で残っていたら，'('が余分にあるということなので，対応する分だけ')'を追加する

n = int(input())
S = input()

need_left = 0
pointer = 0
for i in range(n):
    if S[i] == '(': pointer += 1
    else:
        if pointer == 0:
            need_left += 1
        else:
            pointer -= 1
need_right = pointer
print('('*need_left + S + ')'*need_right)

# ------------------ Sample Input -------------------
4
(())

9
(()))(()(

5
)))))

6
)()())

7
())((()

7
))())))


3
())

10
(((())))))

6
)))())

8
))))((((

# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# editorial: https://img.atcoder.jp/abc064/editorial.pdf
# カッコ列と呼ばれる超典型問題らしい
# けんちょん: https://drken1215.hatenablog.com/entry/2019/02/16/080900
# 初めてカッコ列解いた。groupbyで解けると思って悪あがきを1時間以上してしまった
# 正しい解法が美しすぎて清々しい。
# 超典型問題なので復習は必ず必要

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#カッコ列
#緑diff
#ABC-D
#stack
