# ABC194C - Squared Error
# URL: https://atcoder.jp/contests/abc194/tasks/abc194_c
# Date: 2021/03/06

# ---------- Ideas ----------
# 式展開する
# 求めるものは，(n-1)*sum(Aの各要素の2乗) - 2*(Aの各要素の総当りの積)
# 総当りの積はnマス計算みたいな感じで表を書いて，右上三角を求めればいい
# 全マスの和 = sum(A)**2
# 対角線の和 = sum(Aの各要素の2乗)
# 右上三角 = (sum(A)**2 - sum(Aの各要素の2乗))//2


# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))

a2 = sum([a**2 for a in A])
ab = (sum(A)**2 - a2)//2
ans = ((n-1)*a2 - 2*ab)
print(ans)

# ------------------ Sample Input -------------------
3
2 8 4

3
-1 -2 3

5
-5 8 9 -4 -3

# ----------------- Length of time ------------------
# 20分くらい？

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc194/editorial
# 最初式展開の一般化を間違えてて，(n-1)じゃなくて2をかけてしまってた。
# 解説の式変形とはことなったが，どうになかった
# 統計学でよくでてくる式変形だった。

# ----------------- Category ------------------
#AtCoder
#式展開
#残差二乗和
#総当りの計算

