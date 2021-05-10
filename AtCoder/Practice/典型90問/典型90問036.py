# 典型90問036 - Max Manhattan Distance
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_aj
# Date: 2021/05/10

# ---------- Ideas ----------
# 45度回転してチェビシェフ距離にする
# (x, y)を(x-y, x+y)と変換する
# マンハッタン距離がチェビシェフ距離で図れるようになる。つまり，max(|x2-x1|, |y2-y1|)が2点の距離になる
# xとyのベクトルをそれぞれソートする
# クエリの点からの最大距離となりうる候補の点はxの最小値，最大値，yの最小値，最大値の4点なので，全部試して一番遠いところを出力する

# ------------------- Answer --------------------
#code:python
n, Q = map(int, input().split())
x_vec = []
y_vec = []
for i in range(n):
    x, y = map(int, input().split())
    x, y = x-y, x+y
    x_vec.append([x, i])
    y_vec.append([y, i])

x_vec_sorted, y_vec_sorted = sorted(x_vec), sorted(y_vec)

for _ in range(Q):
    q = int(input()) - 1
    x1, y1 = x_vec[q][0], y_vec[q][0]
    ans = 0
    ans = max(ans, abs(x1 - x_vec_sorted[0][0]))
    ans = max(ans, abs(x1 - x_vec_sorted[-1][0]))
    ans = max(ans, abs(y1 - y_vec_sorted[0][0]))
    ans = max(ans, abs(y1 - y_vec_sorted[-1][0]))

    print(ans)


# ------------------ Sample Input -------------------
3 3
-1 2
1 1
-2 -3
1
2
3


# ----------------- Length of time ------------------
# 18分

# -------------- Editorial / my impression -------------
# 45度回転は知らないと解けないよね

# ----------------- Category ------------------
#AtCoder
#チェビシェフ距離
#マンハッタン距離
#45度回転
#座標