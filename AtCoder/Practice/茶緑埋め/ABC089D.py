# ABC089D - Practical Skill Test
# URL: https://atcoder.jp/contests/abc089/tasks/abc089_d
# Date: 2021/02/14

# ---------- Ideas ----------
# エラトステネスっぽく解けそうな気がしてきた
# 出発時点が違うと訪れるマスも変わるんだけど，クエリごとにDが同じなのがミソで，
# D=4だったら訪れるマスのパターンが4種類しかないから，
# (1,5,9,13,17,...)
# (2,6,10,14,18,...)
# (3,7,11,15,19,...)
# (4,8,12,16,20...)
# (5,9,13,17,...) <- これは1番目と同じ
#
# 4種類の配列だけ用意しておけばよさそうで，
# 一般化すると，保持しておくべきトータルの配列の大きさはDの大きさによらずh*wでよさそう
# 各Dごとの配列は累積和として持っておく

# ------------------- Answer --------------------
#code:python
from itertools import accumulate
h,w,d = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(h)]

# 各マスの座標を保存
pos = [[] for _ in range(h*w+1)]
for y in range(h):
    for x in range(w):
        pos[A[y][x]] = [y, x]

# スタート時点の候補は1,2,3,...,dのd個: インデックスはdで割ると1余り，2余り,3余り,...,d-1余り，0余り
dist_cum = [] # スタート時点sごとに入れる距離のリスト: sから幅dごとに訪れるマスの距離の累積和
for s in range(1, d+1): # スタート時点のインデックス
    dist = []
    for i in range(s, h*w+1-d, d): # スタート時点sから幅dで訪れるマスのインデックス
        dist.append(abs(pos[i][0]-pos[i+d][0])+abs(pos[i][1]-pos[i+d][1]))
    cum = [0]+list(accumulate(dist))
    dist_cum.append(cum)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    # lに対応するdist_cumのインデックス: 1,2,3,...,d
    # スタート時点sはlをdで割った余り
    if l % d != 0:
        dist = dist_cum[l%d-1]
        print(dist[r // d] - dist[l // d])
    else:
        dist = dist_cum[d-1]
        print(dist[r // d - 1] - dist[l // d - 1])

# ACしました！


# ------------------ Sample Input -------------------
3 3 2
1 4 3
2 5 7
8 9 6
2
4 8
3 9

5 5 4
13 25 7 15 17
16 22 20 2 9
14 11 12 1 19
10 6 23 8 18
3 21 5 24 4
3
13 13
2 10
13 13

# ----------------- Length of time ------------------
# 1時間

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc089/editorial.pdf
# D個の配列を用意したけど，1つの配列にmod Dごとに累積和を保存しておけばいいっぽい
# modごとに累積和は初めて見た
# 駒のD歩ごとの移動は，今回のようにmodやエラトステネスっぽい考えでどうにかなる？

# ----------------- Category ------------------
#AtCoder
#累積和
#mod
#