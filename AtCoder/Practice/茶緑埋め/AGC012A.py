# AGC012A - AtCoder Group Contest
# URL: https://atcoder.jp/contests/agc012/tasks/agc012_a
# Date: 2021/02/03

# ---------- Ideas ----------
# ソートしてからどうにか貪欲で取るんだろう
# 1番小さいやつ，2番目に大きいやつ，1番大きいやつ，この3つを組みにして取っていく
# dequeで処理する

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
from collections import deque
n = int(input())
que = deque(sorted(list(map(int, input().split()))))

ans = 0
while que:
    a = que.popleft()
    b = que.pop()
    c = que.pop()
    ans += c
print(ans)

# ------------------ Sample Input -------------------
2
5 2 8 5 1 5

10
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000


# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# 解説: https://img.atcoder.jp/agc012/editorial.pdf
# けんちょんさん: https://drken1215.hatenablog.com/entry/2019/03/26/204200
# けんちょんさんと同じ方法で解けた

# ----------------- Category ------------------
#AtCoder
#AGC-A
#ソート
#Greedy
#貪欲
#自明な上界が最適解
#グルーピング
#茶diff
