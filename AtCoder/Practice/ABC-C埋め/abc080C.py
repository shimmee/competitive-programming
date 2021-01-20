# ABC080C - Shopping Street
# URL: https://atcoder.jp/contests/abc080/tasks/abc080_c
# 日付: 2020/12/06

# ---------- 思ったこと / 気づいたこと ----------
# お店を開く時間帯のbit全探索: 2**10でとける
# Pの意味が分かりづらい

# ------------------- 方針 --------------------
# bitのスニペットを使って’実装

# ------------------- 解答 --------------------
#code:python
n = int(input())
F = [[int(i) for i in input().split()] for _ in range(n)]
P = [[int(i) for i in input().split()] for _ in range(n)]

# 曜日/時間帯 (k)のbit全探索
import itertools
pattern = itertools.product([0, 1], repeat=10)

ans = -float('INF') # 負にもなることに注意。解は利益の最大化
for p in pattern:
    if sum(p) == 0:
        continue
    c = [0]*n # 姉ちゃん店と店iが両方空いてる時間帯の個数
    for i in range(n): # お店のループ
        for k in range(10): # 時間帯のループ
            if p[k] == 1 and F[i][k] == 1: # 時間kにjoisinoお姉ちゃんの店が開いて，かつ店iの店も空いている
                c[i] += 1

    profit = 0
    for i in range(n):
        profit += P[i][c[i]]
    ans = max(ans, profit)
print(ans)
# ------------------ 入力例 -------------------
1
1 1 0 1 0 0 0 1 0 1
3 4 5 6 7 8 9 -2 -3 4 -2

2
1 1 1 1 1 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1
0 -2 -2 -2 -2 -2 -1 -1 -1 -1 -1

3
1 1 1 1 1 1 0 0 1 1
0 1 0 1 1 1 1 0 1 0
1 0 1 1 0 1 0 1 0 1
-8 6 -2 -8 -8 4 8 7 -6 2 2
-9 2 0 1 7 -5 0 -2 -6 5 5
6 -6 7 -9 6 -5 8 0 -9 -7 -7


# ----------------- 解答時間 ------------------
# 37分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc080/editorial.pdf
# 実装重めのbit全探索だった
# P[i][ci]の意味が理解できずにとても困った

# ----------------- カテゴリ ------------------
#AtCoder #abc
#bit全探索