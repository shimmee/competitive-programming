# ABC106C - To Infinity
# URL: https://atcoder.jp/contests/abc106/tasks/abc106_c
# 日付: 2020/11/28

# ---------- 思ったこと / 気づいたこと ----------
# 5000兆日目には最初に現れた1以外の数が序盤を占める
# 1が頭にある個数を数えればいい
#

# ------------------- 方針 --------------------
# 1が最初に連続してる個数iを数える
# kよりiが大きければ1を出力
# otherwise, 最初に現れた1以外の数字を出力

# ------------------- 解答 --------------------
#code:python
n = input()
k = int(input())

for i in range(len(n)):
    if n[i] != '1':
        break
if i >= k:
    print(1)
else:
    print(int(n[i]))


# ------------------ 入力例 -------------------
1214
4

3
157


299792458
9460730472580800



# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc106/editorial.pdf
# 紙とペンがあれば簡単に思いつけた

# ----------------- カテゴリ ------------------
#AtCoder #abc
#文字列
