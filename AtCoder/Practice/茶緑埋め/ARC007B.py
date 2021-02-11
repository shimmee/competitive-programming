# ARC007B - 迷子のCDケース
# URL: https://atcoder.jp/contests/arc007/tasks/arc007_2
# Date: 2021/02/09

# ---------- Ideas ----------
# インデックスが位置，要素がCD番号
# cd1: 聞き終わったcd番号
# cd2: 次に聞くcd番号

# ------------------- Answer --------------------
#code:python
n, m = map(int, input().split())

case = [i for i in range(n+1)]
cd1 = 0
for i in range(m):
    cd2 = int(input())
    cd1_idx = case.index(cd1)
    cd2_idx = case.index(cd2)
    case[cd1_idx], case[cd2_idx] =  case[cd2_idx], case[cd1_idx]
    cd1 = cd2
print(*case[1:], sep='\n')


# ------------------ Sample Input -------------------
5 6
2
3
5
0
1
3

# ----------------- Length of time ------------------
# 15分

# -------------- Editorial / my impression -------------
# enumerate使えばもう少しきれいに書けた
# ABC-CのIDに似てる。

# ----------------- Category ------------------
#AtCoder
#enumerate