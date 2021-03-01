# ABC178E - Dist Max
# URL: https://atcoder.jp/contests/abc178/tasks/abc178_e
# Date: 2021/02/28

# ---------- Ideas ----------
# 座標を45度回転するとチェビシェフ距離になって扱いやすくなる
# 全ての座標を(x,y)から(x+y,x-y)で変換する
# 変換前のマンハッタン距離 = 変換後のチェビシェフ距離: max(|x2-x1|, |y2-y1|)
# max(x)-min(x) か max(y)-min(y) が答えになる

# ------------------- Answer --------------------
#code:python
n = int(input())
x_vec = []
y_vec = []
for _ in range(n):
    x, y = map(int, input().split())
    x, y = x+y, x-y
    x_vec.append(x)
    y_vec.append(y)

print(max(max(x_vec)-min(x_vec), max(y_vec)-min(y_vec)))


# ------------------ Sample Input -------------------
3
1 1
2 4
3 2


# ----------------- Length of time ------------------
# 17分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc178/editorial-E-phcdiydzyqa.pdf
# 45度回転のテクニックを初めて知った
# とても便利

# ----------------- Category ------------------
#AtCoder
#マンハッタン距離
#45度回転
#ABC-E
#緑diff
#二次元平面上のN点の問題
#O(N^2)個のものを考える問題
#絶対値に関する問題
#45度回す
#チェビシェフ距離
