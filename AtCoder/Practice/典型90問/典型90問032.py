# 典型90問032 - AtCoder Ekiden
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_af
# Date: 2021/05/09

# ---------- Ideas ----------
# 順列全探索
# itertoolsのpermutationsでインデックスの区間を走る選手を全探索
# 各区間の選手が決まれば，Aの情報からかかる時間をsum
# 次の人と仲悪かったらansを更新しない

# ------------------- Answer --------------------
#code:python
inf = float('inf')
n = int(input())
A = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
G = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)

from itertools import permutations
all_pattern = permutations(range(n)) # インデックスの区間を走る選手
ans = inf
for pattern in all_pattern:
    time = 0
    flag = True # どこかの区間で1組でも仲悪かったらFalse
    for j in range(n): # j区間
        i = pattern[j] # 選手i
        time += A[i][j] # かかる時

        # 仲悪い判定
        if j < n-1:
            i_next = pattern[j + 1]
            if i in G[i_next]:
                flag = False

    if flag:
        ans = min(ans, time)

print(ans if ans != inf else -1)

# ------------------ Sample Input -------------------
3
1 10 100
10 1 100
100 10 1
1
1 2


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/032.jpg
# こういう問題が出て欲しい
# すぐ解ける
# 仲悪い判定をもっときれいに書けなかったかな？

# ----------------- Category ------------------
#AtCoder
#順列全探索
#permutations