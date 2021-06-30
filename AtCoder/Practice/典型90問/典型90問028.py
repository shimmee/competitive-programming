# 典型90問028 - Cluttered Paper
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_ab
# Date: 2021/05/13

# ---------- Ideas ----------
# 2次元いもす法: imos配列も2次元
# 一般的な座標平面の場合
# 矩形の左下に+1，左上に−1を，右下に−1を，右下に+1を加算
# 左から右に累積和，下から上に累積和
# これで終わり


# ------------------- Answer --------------------
#code:python
n = int(input())
m = 1000
imos = [[0]*(m+1) for _ in range(m+1)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    imos[y1][x1] += 1
    imos[y2][x2] += 1
    imos[y1][x2] -= 1
    imos[y2][x1] -= 1

for x in range(m):
    for y in range(m):
        imos[y+1][x] += imos[y][x]

for y in range(m):
    for x in range(m):
        imos[y][x+1] += imos[y][x]

count = [0]*(n+1)
for y in range(m):
    for x in range(m):
        count[imos[y][x]] += 1
for i in range(1, n+1):
    print(count[i])

# ------------------ Sample Input -------------------
2
1 1 3 2
2 1 4 2


# ----------------- Length of time ------------------
# 解説やらヒント見て1時間かかった

# -------------- Editorial / my impression -------------
# そもそもitertools.chain.from_iterable(imos)という謎のflatten関数を使ったらWAになった。
# これ使わなかったら30分でいけてた
# 初めての二次元いもすだった，面白かった

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#二次元にもす法
#imos
#2次元いもす
#累積和
#典型90問
