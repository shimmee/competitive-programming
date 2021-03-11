# ABC191C - Digital Graffiti
# URL: https://atcoder.jp/contests/abc191/tasks/abc191_c
# Date: 2021/03/10

# ---------- Ideas ----------
# 各マスではなくて，マスの隙間，格子点，頂点に注目する。
# ある頂点の周辺4マスに#が一つであれば角1つ，#が横並びに2つあれば辺なので角なし
# #が3つあれば角1つ，#が4つあれば角なし


# ------------------- Answer --------------------
#code:python
h, w = map(int, input().split())
S = [input() for _ in range(h)]
d = [[0, 0], [0, 1], [1, 0], [1, 1]]

ans = 0
for y in range(h-1):
    for x in range(w-1):
        cnt = 0
        for dy, dx in d:
            X = x + dx
            Y = y + dy
            if S[Y][X] == '#':
                cnt += 1
        if cnt == 1 or cnt == 3: ans += 1
print(ans)


# ------------------ Sample Input -------------------
5 5
.....
.###.
.###.
.###.
.....


# ----------------- Length of time ------------------
# 9分でAC！！！ (少し前に解法を見たことが合った)

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc191/editorial
# 一番わかり易いやつ: https://note.com/momomo0214/n/nf5cd16b09b09
# これを初見で思いつくのはかなり厳しそう。
# 角に注目して周りの4マスを見るという発想の転換が必要

# ----------------- Category ------------------
#AtCoder
#多角形
#マスの間に注目
#角に注目
#周辺の4マス