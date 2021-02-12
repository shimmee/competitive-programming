# ABC027B - 島と橋
# URL: https://atcoder.jp/contests/abc027/tasks/abc027_b
# Date: 2021/02/11

# ---------- Ideas ----------
# 合計人数が島の数で割り切れる必要がある
# 最終的な1つの島あたりの人数=の人数/島の数

# ------------------- Solution --------------------
# 左から走査していって，「これまで繋がっている島にいる総人数=島の個数*理想人数」になってれば
# OKなので，今の島から次の島には橋は必要ない
# otherwise, 橋を書ける: ansをインクリメント

# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))
total = sum(a)
if total % n != 0:
    print(-1); exit()

num_p = total//n # 島1つあたりの理想人数
ans = 0
cnt = 0 # 繋がっている島の個数
cum_p = 0 # 繋がっている島の合計人数

for i in range(n):
    cnt += 1
    cum_p += a[i]
    if cum_p == cnt*num_p:
        cnt = 0
        cum_p = 0
    else:
        ans += 1
print(ans)

# ------------------ Sample Input -------------------
3
1 2 3

5
2 0 0 0 3

# ----------------- Length of time ------------------
# 9分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/abc027
# 簡単だった: 一昔前の緑diffだからすぐ解けた
# この人と同じ考え方: https://te-sh.github.io/procon/abc/027/b.html

# ----------------- Category ------------------
#AtCoder
#緑diff
#平均化
