# ABC176E - Bomber
# URL: https://atcoder.jp/contests/abc176/tasks/abc176_e
# Date: 2021/05/09

# ---------- Ideas ----------
# 行と列ごとに爆弾をカウントして，最大の個数を持つ行と列の候補を探す
# 行と列の最大個数がh_maxとw_maxで，候補がh_candiとw_candi
# この時点で，答え値はh_max + w_maxまたは h_max + w_max - 1
# 行と列の候補のうち，爆弾のない交点マスが1つでもあれば，h_max + w_maxになる
# 全ての交点マスに爆弾があれば，ダブルカウントせざるを得ないので，h_max + w_max - 1になる

# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
H, W, m = map(int, input().split())
h, w = [], []
h_graph = [set() for _ in range(H)]

for i in range(m):
    y, x = map(int, input().split())
    y, x = y-1, x-1
    h.append(y)
    w.append(x)
    h_graph[y].add(x)

h_count = Counter(h)
h_max = h_count.most_common()[0][1]
h_candi = [key for key, value in h_count.items() if value == h_max]

w_count = Counter(w)
w_max = w_count.most_common()[0][1]
w_candi = [key for key, value in w_count.items() if value == w_max]

ans = 0
flag = False # 行と列の候補の交点のうち爆弾がないマスがあればTrue，すべての交点マスに爆弾があればFalse
for y in h_candi:
    for x in w_candi:
        if not x in h_graph[y]:
            flag = True
            break
    if flag: break

ans = h_max + w_max
print(ans if flag else ans - 1)


# ------------------ Sample Input -------------------
5 5 10
2 5
4 3
2 3
5 5
2 2
5 4
5 3
5 1
3 5
1 4

# ----------------- Length of time ------------------
# 40分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc176/editorial
# しばらく前には全然わからなかったけど，解き直したらスラスラ溶けた
# 典型的な考え方は特になかった？

# ----------------- Category ------------------
#AtCoder
#ABC-E
#ダブルカウント
#水色diff
#grid
#爆弾
#巨大grid