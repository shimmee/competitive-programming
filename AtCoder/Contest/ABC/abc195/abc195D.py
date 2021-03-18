# ABC195D - Shipping Center
# URL: https://atcoder.jp/contests/abc195/tasks/abc195_d
# Date: 2021/03/13

# ---------- Ideas ----------
# 一つの箱に一つの荷物しか入らないから，価値の高い荷物から入れていけばOK
# 価値の高い荷物から順に，荷物が入る最小の箱に入れていく
# 制約が小さいのでクエリごとに操作する

# ------------------- Answer --------------------
#code:python
n, m, q = map(int, input().split())
wv = [[int(i) for i in input().split()] for _ in range(n)]
wv = sorted(wv, key=lambda x: x[1], reverse=True)
X = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    boxes = sorted(X[:l] + X[r:])
    used = [False]*len(boxes)

    ans = 0
    for w, v in wv:
        for i in range(len(boxes)):
            box = boxes[i]
            if not used[i] and box >= w:
                ans += v
                used[i] = True
                break
    print(ans)


# ------------------ Sample Input -------------------
3 4 3
1 9
5 3
7 8
1 8 6 9
4 4
1 4
1 3


# ----------------- Length of time ------------------
# 20分くらい？

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc195/editorial
# ナップサックDPかビンパッキング問題か，その当たりかなと思ってたら，箱に入るのは1つだったから簡単だった

# ----------------- Category ------------------
#AtCoder
#greedy
#貪欲
#ソート
#クエリ
#ソートして貪欲