# ABC195B - Many Oranges
# URL: https://atcoder.jp/contests/abc195/tasks/abc195_b
# Date: 2021/03/13

# ---------- Ideas ----------
# ナップサックDPっぽさがある
# さすがに組み合わせを全部試すみたいなことはB問題だしありえないだろうから，簡単に解けるはず
# Wは1000倍したい
# a*n <= w <= b*nとなるようなnが一つも無ければUNSATISFIABLE
# 最小はceil(w/b)，最大はfloor(w/a)

# ------------------- Answer --------------------
#code:python
a, b, w = map(int, input().split())
w *= 1000
flag = True
for i in range(1, 1000**2+1):
    if a*i <= w <= b*i:
        flag = False
        break

if flag:
    print('UNSATISFIABLE')
else:
    print((w+b-1)//b, w//a)


# ------------------ Sample Input -------------------
100 200 2

120 150 2

300 333 1

# ----------------- Length of time ------------------
# 20分くらい

# -------------- Editorial / my impression -------------
# 基本的にはできるし，最小と最大の部分だけ考えればOKという問題だった。たまにみる。

# ----------------- Category ------------------
#AtCoder
#末端だけ考えればOK
#全部作れる
#全探索
