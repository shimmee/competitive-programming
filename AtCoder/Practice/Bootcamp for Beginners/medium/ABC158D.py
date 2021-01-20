# ABC158D - String Formation
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/abc158/tasks/abc158_d
# 日付: 2020/12/31


# ------------------- 方針 --------------------
# T=1のたびに毎回反転させてたら10**10になって間に合わないので，T=1がきたら反転のフラグをもつ
# T=2のときにはfの情報と反転の情報から，頭に追加するかケツに追加するか決める
# 文字列ではなく，dequeで管理

# ------------------- 解答 --------------------
#code:python
from collections import deque
S = input()
Q = int(input())
l = deque([str(s) for s in S])

reverse = 0
for _ in range(Q):
    inp = input().split()
    if len(inp) == 1: # T=1のとき
        reverse = 1 - reverse
    if len(inp) == 3: # T=2のとき
        f, c = inp[1], inp[2]
        if reverse == 0 and f == '1': # リバースなしで先頭: 先頭にc追加
            l.appendleft(c)
        elif reverse == 1 and f == '1':  # リバースありで先頭: けつにc追加
            l.append(c)
        elif reverse == 0 and f == '2': # リバースなしでケツ: ケツにc追加
            l.append(c)
        elif reverse == 1 and f == '2':  # リバースありでケツ: 先頭にc追加
            l.appendleft(c)

# リバースすべきだったらする
if reverse == 0: print(''.join(l))
else: print(''.join(list(l)[::-1]))


# ------------------ 入力例 -------------------
a
4
2 1 p
1
2 2 c
1

a
6
2 2 a
2 1 b
1
2 2 c
1
1

y
1
2 1 x

# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc158/editorial.pdf
# 反転の処理が時間かかるということがポイント
# 解説通りにとけてとても嬉しい

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#deque
#appendleft
