# キーエンス プログラミング コンテスト 2020 B - Robot Arms
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b
# Date: 2021/01/15

# ---------- Ideas ----------
# 区間スケジューリング問題と同じ
# x=2, l=4だったら区間(l,r)=[-2, 6]と考えられる
# 区間の右端(r)でソートする
# 貪欲に，rの小さい順から取っていって，lが前に含んだr (now_r)より大きかったらOK
# 前のと今回のが被ってたら(l<now_r)ならスキップ

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
n = int(input())
lr = []
for _ in range(n):
    x, length = map(int, input().split())
    lr.append([x-length, x+length])

lr = sorted(lr, key=lambda x: x[1])
ans = 1
now_r = lr[0][1]
for l, r in lr[1:]:
    if now_r <= l:
        ans += 1
        now_r = r
print(ans)



# ------------------ Sample Input -------------------
4
2 4
4 3
9 3
100 5

2
8 20
1 10

5
10 1
2 1
4 1
6 1
8 1


# ----------------- Length of time ------------------
# 8分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/keyence2020/editorial.pdf
# 区間の範囲がかぶらない=区間スケジューリング問題
#

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#区間スケジューリング問題
#greedy
#貪欲法
#緑diff
#ロボット
#一直線上のN点の問題