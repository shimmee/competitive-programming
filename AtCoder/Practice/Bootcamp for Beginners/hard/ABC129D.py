# ABC129D - Lamp
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc129/tasks/abc129_d
# Date: 2021/01/22

# ---------- Ideas ----------
# どう全探索するか

# ------------------- Solution --------------------
# 行をループで回す。各行についてgroupbyする
# 各cellについて，横に何マス広がりがあるのか(次の障害物まで何マスあるか)がわかるので，テーブルに埋める

# 同じことを列についても行う
# 最後に行と列でループを回して，上記の2つのテーブルの和が一番大きいセルが優勝
# ランプを置く場所は縦も横もカウントされて重複があるので最後に1を引く

# ------------------- Answer --------------------
#code:python
from itertools import groupby
H, W = map(int, input().split())
S = [input() for _ in range(H)]

h_table = [[0 for _ in range(W)] for _ in range(H)]
w_table = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
    s = S[h]
    gr = groupby(s)
    i = 0
    for key, group in gr:
        m = len(list(group))
        if key == '.':
            for j in range(m):
                h_table[h][i+j] = m
        i += m

for w in range(W):
    s = [S[h][w] for h in range(H)]
    gr = groupby(s)
    i = 0
    for key, group in gr:
        m = len(list(group))
        if key == '.':
            for j in range(m):
                w_table[i + j][w] = m
        i += m

ans = 0
for h in range(H):
    for w in range(W):
       ans = max(ans, h_table[h][w] + w_table[h][w])
print(ans-1)
# ------------------ Sample Input -------------------
4 6
#..#..
.....#
....#.
#.#...

8 8
..#...#.
....#...
##......
..###..#
...#..#.
##....#.
#...#...
###.#..#

# ----------------- Length of time ------------------
# 24分

# -------------- Editorial / my impression -------------
# 解説: https://img.atcoder.jp/abc129/editorial.pdf
# けんひょん: https://drken1215.hatenablog.com/entry/2019/06/10/143300
# 今回はgroupbyを使って2回の前処理で終わらせたが，
# 公式の解法やけんちょんさん記事だと，各マスから「左に何マスで壁」「右に何マスで壁」「上に何マスで壁」「下に何マスで壁」
# の4つの前処理をして，全部足したものマイナス3で答えを出せる
# こっちの方が汎用性高そうなので覚えておきたい

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#グリッド
#前処理
#壁にぶつかるまで動く
#「次の要素」へのポインタを求める
#ランプ
#lamp
#緑diff
#ABC-D