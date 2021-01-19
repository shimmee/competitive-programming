# ABC054C - One-stroke Path
# URL: https://atcoder.jp/contests/abc054/tasks/abc054_c
# 日付: 2020/12/17

# ---------- 思ったこと / 気づいたこと ----------
# N<=8なので順列全探索では？

# ------------------- 方針 --------------------
# 順列のパターンを用意する
# (1, 3, 4, 2)というパターンだったら，頂点1から3にいけて，3から4に行けて，4から2に行けるようなグラフかどうかを調べればいい
# flagがTrueであり続ければansにインクリメントしよう

# ------------------- 解答 --------------------
#code:python
from itertools import permutations
n, m = map(int, input().split())

# 隣接リストとしてグラフを受け取る
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

all_pattern = list(permutations([i for i in range(n)]))
ans = 0
for pattern in all_pattern:
    if pattern[0] != 0: continue # 必ず0からスタートする
    flag = True
    for i in range(n-1):
        from_ = pattern[i] # 出発する頂点 from_
        to_ = pattern[i+1] # 到着する頂点 to_

        if to_ in G[from_]: pass # 出発する頂点 from_の行き先として，到着する頂点 to_が入ってればOK
        else: flag = False

    if flag:
        ans += 1
print(ans)


# ------------------ 入力例 -------------------
3 3
1 2
1 3
2 3

7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7


# ----------------- 解答時間 ------------------
# 9分 速い！ 水色diffなのに！

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc054/editorial.pdf
# 解説はBFSで解いてる。順列全探索は別解

# ----------------- カテゴリ ------------------
#AtCoder #abc
#順列全探索
#グラフ
