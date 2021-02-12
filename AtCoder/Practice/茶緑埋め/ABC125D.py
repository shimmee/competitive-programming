# ABC125D - Flipping Signs
# URL: https://atcoder.jp/contests/abc125/tasks/abc125_d
# Date: 2021/02/11

# ---------- Ideas ----------
# マイナスを真ん中に集めて一気に消すことができる！
# マイナスが偶数個あれば全部正にできるし，奇数子だったら必ず1つあまる
# 負の数の個数の偶奇で決まる！
# 負の数が奇数個あれば，n-1個は正にできて，最後に1つ必ず負が残る
# 負の数が整数個あれば，全て正にできる

# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))
total = sum([abs(a) for a in A])
min_A = min([abs(a) for a in A])

minus = len([1 for a in A if a < 0])
ans = total-2*min_A if minus % 2 == 1 else total
print(ans)


# ------------------ Sample Input -------------------
3
-10 5 -4

5
10 -4 -8 -11 3


# ----------------- Length of time ------------------
# 16分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc125/editorial.pdf
# 解説通りに解けた。
# 色々実験してたら思いつけた
# 隣り合う2つに同じ操作をし続ける問題は，偶奇に注目すればいいのかもしれない

# ----------------- Category ------------------
#AtCoder
#ABC-D
#偶奇に注目
#パリティ
#数列
#条件の言い換え
#操作:隣接swap
#操作によって出来上がるものの最適化問題
#緑diff
