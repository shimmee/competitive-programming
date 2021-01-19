# キーエンス プログラミング コンテスト 2021 C:
# URL: https://atcoder.jp/contests/keyence2021/tasks/keyence2021_c
# Date: 2021/01/16

# ---------- Ideas ----------
# DPやぞ
# 次行く場所に書き込みがないとき，文字数分

# カウントするのは置いといて，どうやって盤面を決定していくか？
# (h,w)に到達可能な盤面の通りは求められるか？求める必要はあるか？

# 愚直に解くなら，「盤面を1つ決定する-> 経路の個数を求める」これを全盤面に対して行う
# あるマスにおけるans=盤面の通り * 経路の個数?

# 全ての白マスにR,D,Xをそれぞれ置いたと考えて，3つのテーブルを用意する？
# 貰うDP

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
mod = 998244353
H, W, K = map(int, input().split())
G = [['.' for _ in range(W)] for _ in range(H)]
for _ in range(K):
    h, w, c = map(str, input().split())
    G[int(h)-1][int(w)-1] = c

dp_R = [[0 for _ in range(W)] for _ in range(H)]
dp_D = [[0 for _ in range(W)] for _ in range(H)]
dp_X = [[0 for _ in range(W)] for _ in range(H)]

if G[0][0] == '.':
    dp_R[0][0], dp_D[0][0], dp_X[0][0] = 3, 3, 3
else:
    dp_R[0][0], dp_D[0][0], dp_X[0][0] = 1, 1, 1

for y in range(H):
    for x in range(W):
        if x == y == 0: continue

        # 左から貰う: 左がDじゃなければ貰える
        if G[y][x-1] != 'D' and x >= 1:
            R_fromL = dp_R[y][x - 1] + dp_X[y][x - 1]
            dp_D[y][x] = dp_R[y][x - 1] + dp_X[y][x - 1]
            dp_X[y][x] = dp_R[y][x - 1] + dp_X[y][x - 1]

        # 上から貰う: 上がRじゃなければ貰える
        if G[y-1][x] != 'R' and y >= 1:
            dp_R[y][x] = dp_D[y - 1][x] + dp_X[y - 1][x]
            dp_D[y][x] = dp_D[y - 1][x] + dp_X[y - 1][x]
            dp_X[y][x] = dp_D[y - 1][x] + dp_X[y - 1][x]




# ------------------ Sample Input -------------------
2 2 3
1 1 X
2 1 R
2 2 R


# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#キーエンスプログラミングコンテスト2021
#500点問題

#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
