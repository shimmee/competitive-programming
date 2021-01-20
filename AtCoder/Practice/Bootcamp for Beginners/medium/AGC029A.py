# AGC029A - Irreversible operation
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc029/tasks/agc029_a
# 日付: 2020/12/28

# ---------- 思ったこと / 気づいたこと ----------
# 左右入れ替えると解釈できる
# Wを左の方に詰めたい
# 最後にはWWWW...WWBB....BBBみたいな感じになる

# ------------------- 方針 --------------------
#

# ------------------- 解答 --------------------
#code:python
S = input()
n = len(S)

cnt_W = 0
ans = 0
for i in range(n):
    if S[i] == 'W':
        ans += i - cnt_W
        cnt_W += 1
print(ans)

# 解説AC
# ------------------ 入力例 -------------------
BBW

BBWW

BWBWBW

# ----------------- 解答時間 ------------------
# 20分で解説AC

# -------------- 解説 / 感想 / 反省 -------------
# 9割できてた
# Wの位置を調べて，Wが本来いるべき位置との差分を取って，インクリメントする
# 1つめのWは一番左(インデックス0)，2つめのWは一番左から2番目(インデックス1)のようなかんじ
#

# ----------------- カテゴリ ------------------
#AtCoder
#AGC-A
#BootcampForBeginners-medium
#解説AC #medium復習
#