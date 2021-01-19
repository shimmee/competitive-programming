# ABC 167C - Skill Up
# URL: https://atcoder.jp/contests/abc167/tasks/abc167_c
# 日付: 2020/11/22

# ---------- 思ったこと / 気づいたこと ----------
# 買う買わないのbit全探索

# ------------------- 方針 --------------------
# bitで買う本があった場合，理解度とコストを溜め込んでいく
# 買う本をピックアップしたのち，理解度がxより大きい場合OKなので，ansのコストを更新する

# ------------------- 解答 --------------------
#code:python
import numpy as np
n,m,x=map(int, input().split())
C = []
A = []

for i in range(n):
    ca = list(map(int, input().split()))
    C.append(ca[0])
    A.append(ca[1:])

C = np.array(C)
A = np.array(A)

inf = float('INF')
ans = inf
for i in range(2**n):
    r = np.zeros((m), int) #理解度のリスト
    cost = 0
    for j in range(n):
        if (i >> j) & 1: #j番目の本を買う
            r += A[j]
            cost += C[j]

    if sum(r >= x) == m: #全アルゴリズムの理解度がxを超えてるなら
        ans = min(ans, cost)

if ans == inf:
    print(-1)
else:
    print(ans)


# ------------------ 入力例 -------------------
3 3 10
60 2 2 4
70 8 7 9
50 2 3 9

3 3 10
100 3 1 4
100 1 5 9
100 2 6 5


8 5 22
100 3 7 5 3 1
164 4 5 2 7 8
334 7 2 7 2 9
234 4 7 2 8 2
541 5 4 3 3 6
235 4 8 6 9 7
394 3 6 1 6 2
872 8 4 3 7 2

# ----------------- 解答時間 ------------------
# 10分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc167/editorial.pdf
# bit全探索は空で書けるようになった！！

# ----------------- カテゴリ ------------------
#AtCoder #abc
#bit全探索
