# ARC024B - 赤と黒の木
# URL: https://atcoder.jp/contests/arc024/tasks/arc024_2
# Date: 2021/04/15

# ---------- Ideas ----------
# 同じ色が最長で続く個数が求まれば，それ割る2くらいが答え
# itertools.groupbyの出番
# 最初と最後の色が同じ場合，がっちゃんこすればいい
# 最後に一番長いgroupを数える

# ------------------- Answer --------------------
#code:python
n = int(input())
color = [int(input()) for _ in range(n)]

if all([i == 1 for i in color]) or all([i == 0 for i in color]):
    print(-1)
    exit()

from itertools import groupby
gr = groupby(color)
l = []
for key, group in gr:
    l.append(list(group))

if color[0] == color[-1]:
    l[0] += l[-1]
    l.pop()

max_len = max(len(i) for i in l)
print((max_len-1)//2 + 1) # ここは勘


# ------------------ Sample Input -------------------
6
1
1
0
1
1
1

# ----------------- Length of time ------------------
# 9分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc024
# 今なら茶diffかな
# groupbyが便利すぎる

# ----------------- Category ------------------
#AtCoder
#groupby
#最長の連続する要素の個数
#水色diff