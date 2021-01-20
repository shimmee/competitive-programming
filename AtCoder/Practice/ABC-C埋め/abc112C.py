# ABC112 C-Pyramid
# URL: https://atcoder.jp/contests/abc112/tasks/abc112_c
# 日付: 2020/12/03


# ------------------- 方針 --------------------
# x,y,hが与えられたときにcx, cy, Hを求めたい
# cxとcy<=100なので，，この2変数については全探索する
# cxとcyを固定し，各入力に対してH=h+|x-cx|+|y-cy|を求めて，全部同じHだったらOK
# 入力のhが0だったとき，max(H-|x-cx|-|y-cy|, 0)のうち0となっている。
# つまりH-|x-cx|-|y-cy| < 0 -> H<|x-cx|+|y-cy| なので，この条件を確認する

# ------------------- 解答 --------------------
#code:python
n = int(input())
xyh = [[int(i) for i in input().split()] for _ in range(n)]

for cx in range(101):
    for cy in range(101):
        Z = []  # hが0のとき|x-cx|+|y-cy|を貯める
        H = [] # hが0よりのときHを貯める
        for i in range(n):
            x, y, h = xyh[i]
            if h == 0:
                Z.append(abs(x - cx) + abs(y - cy))
            else:
                H.append(h + abs(x - cx) + abs(y - cy))

        if len(set(H)) == 1: # Hが全て同じ要素(uniqueが1つ)のときだけOK
            flag = True
            for z in Z: # 全てのz=|x-cx|+|y-cy|はHより大きい必要がある
                if z < H[0]:
                        flag = False # もし1つでもviolateしていればfalse
            if flag: # flagがTrueのときだけOK
                print(cx, cy, H[0])
                exit()

# ------------------ 入力例 -------------------
4
2 3 5
2 1 5
1 2 5
3 2 5

2
0 0 100
1 1 98

3
99 1 191
100 1 192
99 0 192

# ----------------- 解答時間 ------------------
# 35分AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc112/editorial.pdf
# 最初，max(H-|x-cx|-|y-cy|, 0)の0の方を考慮できてなくてWAだった
# C問題にしては実装重めだった


# ----------------- カテゴリ ------------------
#AtCoder #abc
#全探索

