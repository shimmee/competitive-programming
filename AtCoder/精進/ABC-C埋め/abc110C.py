# ABC110C - String Transformation
# URL: https://atcoder.jp/contests/abc110/tasks/abc110_c
# 日付: 2020/12/03

# ---------- 思ったこと / 気づいたこと ----------
# アルファベットを交換する表があったら良さそう

# ------------------- 方針 --------------------
# 26*26のインデックスがアルファベットに対応した配列を作る: 全部はFalse
# Sのi文字目とTのi文字目に対応する配列の場所にTrueを入れる
# ある行，ある列を見た時に，Trueが2つ以上ある場合，どうやっても文字を変換できないので，ダメ

# ------------------- 解答 --------------------
#code:python

# 変更行列を作ってみる

S = input()
T = input()
alpha2num = lambda c: ord(c) - ord('a')

table = [[False]*26 for _ in range(26)]

for i in range(len(S)):
    si = alpha2num(S[i])
    ti = alpha2num(T[i])
    table[si][ti] = True

flag = True
for i in range(26):
    if sum(table[i]) > 1 or sum([table[j][i] for j in range(26)]) > 1:
        flag = False
if flag: print('Yes')
else: print('No')


# ------------------ 入力例 -------------------
azzel
apple

chokudai
redcoder

abcdefghijklmnopqrstuvwxyz
ibyhqfrekavclxjstdwgpzmonu

# ----------------- 解答時間 ------------------
# 35分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc109/editorial.pdf
# 解説通りに溶けた！

# ----------------- カテゴリ ------------------
#AtCoder #abc
#文字列



# ボツ解答
# S = input()
# T = input()
# alpha2num = lambda c: ord(c) - ord('a')
#
# change = [False]*26
# keep = [False]*26
#
# for i in range(len(S)):
#     si = alpha2num(S[i])
#     ti = alpha2num(T[i])
#     if S[i] == T[i]:
#         keep[si] = True
#     else:
#         change[ti] = True
#
# flag = True
# for i in range(26):
#     if change[i] and keep[i]:
#         flag = False
# if flag: print('Yes')
# else: print('No')
#
# # 14/24 WAなのでおそらく嘘解法