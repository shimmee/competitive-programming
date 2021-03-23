# ABC196D - Hanjo
# URL: https://atcoder.jp/contests/abc196/tasks/abc196_d
# Date: 2021/03/20

# ---------- Ideas ----------
# 2*1タイルの置き方を決めれば1*1の置き方は決まるので，2*1の置き方を決める
# H*W <= 16なので，全探索できそう

# ------------------- Solution --------------------
# A枚の2*1タイルを置く場所を全探索して，おけたらansをインクリメント
# n = h*wとすると，n個からA個選ぶ組み合わせがあるので，組み合わせ全探索で全部試せばよい: itertools.combinations
# あと，それぞれのA枚を縦と横におけるので，この部分はbit全探索する: itertools.product
# 組み合わせは一次元になるから，二次元のタイルと対応させる必要がある

# ------------------- Answer --------------------
#code:python
from itertools import combinations
import itertools
h, w, a, b = map(int, input().split())
n = h*w

ans = 0
all_pattern = list(combinations([i for i in range(n)], a)) # 一次元で得る
all_direction = list(itertools.product([0, 1], repeat=a))
for pattern in all_pattern:
    for direction in all_direction:
        grid = [[True] * w for _ in range(h)]  # 各マスに置けるかどうかのフラグ
        flag = True # a枚がちゃんと納まるフラグ: 1枚でもおこなかったらFalseにする
        for i in range(a): # A枚のうちのi枚目
            p = pattern[i] # タイルを置く場所 (一次元)
            y, x = divmod(p, w) # タイルを置く場所 (二次元)
            if direction[i] == 1: # 横に置く
                if x <= w-2 and grid[y][x] and grid[y][x+1]: # タイルを置く場所(x,y)とその右側(x+1, y)にまたがる
                    grid[y][x] = False
                    grid[y][x+1] = False
                else:
                    flag = False
            else: # 縦に置く
                if y <= h-2 and grid[y][x] and grid[y+1][x]:
                    grid[y][x] = False
                    grid[y+1][x] = False
                else:
                    flag = False

        if flag:
            ans += 1
print(ans)

# ------------------ Sample Input -------------------
3 3 4 1

# ----------------- Length of time ------------------
# 40分

# -------------- Editorial / my impression -------------
# many requirementsに似てた。
# itertoolsが便利すぎた。
# 解説の想定解法はdfsだったけど，こっちで解いてよかった。
# 水diffだったこの問題を解けたおかげで水パフォ出せた！

# ----------------- Category ------------------
#AtCoder
#組み合わせ全探索
#bit全探索
#itertools
#畳の置き方
#数え上げ問題