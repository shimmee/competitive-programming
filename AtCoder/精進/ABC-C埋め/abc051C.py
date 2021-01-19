# ABC051C - Back and Forth
# URL: https://atcoder.jp/contests/abc051/tasks/abc051_c
# 日付: 2020/12/10

# ---------- 思ったこと / 気づいたこと ----------
# 入力例を一般化する

# ------------------- 方針 --------------------
# step1: 上に行って右にいく
# step2: 下に行って左にいく
# step3: 左上から回り込む
# step4: 右下から回り込む

# ------------------- 解答 --------------------
#code:python
sx,sy,tx,ty = map(int, input().split())
x = tx-sx
y = ty-sy

step1 = 'U'*y + 'R'*x
step2 = 'D'*y + 'L'*x
step3 = 'L' + 'U'*(y+1) + 'R'*(x+1) + 'D'
step4 = 'R' + 'D'*(y+1) + 'L'*(x+1) + 'U'

print(step1 + step2 + step3 + step4)

# ------------------ 入力例 -------------------
0 0 1 2

-2 -2 1 1

UURDDLLUUURRDRDDDLLU
UURDDLLUUURRDRDDDLLU

UUURRRDDDLLLLUUUURRRRDRDDDDLLLLU
UURRURRDDDLLDLLULUUURRURRDDDLLDL

# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc051/editorial.pdf
# この解法でいいのかよくわからんかったけど，通ったからよかった

# ----------------- カテゴリ ------------------
#AtCoder #abc

