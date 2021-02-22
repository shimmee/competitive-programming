# ABC166E - This Message Will Self-Destruct in 5s
# URL: https://atcoder.jp/contests/abc166/tasks/abc166_e
# Date: 2021/02/20

# ---------- Ideas ----------
# a[i]+i のリスト，j-a[j]のリストを作成
# これらが一致するペアの数を数えたいので，
# j-a[j]をの出現回数をcounterしておく
# a[i]+iを走査して，ansにインクリメント

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
n = int(input())
A = list(map(int, input().split()))

A_plus_i = [i+1+A[i] for i in range(n)]
j_minus_A = [j+1-A[j] for j in range(n)]
counter = Counter(j_minus_A)

ans = 0
for i in range(n):
    a_plus_i = A_plus_i[i]
    ans += counter[a_plus_i]
print(ans)

# ------------------ Sample Input -------------------
6
2 3 3 1 3 1


# ----------------- Length of time ------------------
# 8分AC

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc166/editorial
# 何か簡単に解けた
# 式展開したら簡単だった
# Diffが高いのはE問題だからかな
# C問題でもおかしくなさそう

# ----------------- Category ------------------
#AtCoder
#緑diff
#ABC-E
#O(N^2)個のものを考える問題
#式展開
#工夫して全探索
#事前計算