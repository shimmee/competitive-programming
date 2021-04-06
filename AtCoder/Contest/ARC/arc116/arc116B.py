# ARC116B - Products of Min-Max
# URL: https://atcoder.jp/contests/arc116/submissions/me
# Date: 2021/03/28

# ---------- Ideas ----------
# 図書いて式変形して概要を掴む
# 累積和でO(N^2)を避ける


# ------------------- Answer --------------------
#code:python
n = int(input())
A = sorted(list(map(int, input().split())))
mod = 998244353

# 累積和: 考察の☆
cum = [0]
for i in reversed(range(1, n)):
    cum.append((cum[n-(i+1)]*2 + A[i])% mod)
cum = cum[::-1]

# 考察のSの部分
ans = 0
for i in range(n):
    a = A[i]
    ans = (ans + a**2 + (a*cum[i])) % mod
print(ans)

# ------------------ Sample Input -------------------
3
2 4 3


5
1 3 6 10 12

# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# これが解けなくてno-subです
# 三角形の合計を求めれば良いところまでわかってたけど，O(N)にする方法がわからなかった
# 三角形を30分くらい眺めて結局あきらめたけど，解説を見た今なら，どうやって三角形から規則を見つけるかが分かった (図中の青と赤字)
# この問題のdiffが800なのは辛い...
# 式変形しても解ける(?)問題だし，三角形から法則見つけても解ける問題だったけど，
# そもそも本番中に式に起こすことがなかったし，三角形から法則を見つけることもできなかったから，だめだった
# 反省点としては，「キレイな図が書けてあとは法則見つけるだけ，というところまで来たら諦めない」ということ

# ----------------- Category ------------------
#AtCoder
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#累積和
#シグマの式変形
#式変形
#べき乗を含む数列の和
#実験
#ソート
#数列の三角形