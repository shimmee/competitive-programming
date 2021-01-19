# ABC185
# URL: https://atcoder.jp/contests/abc185/tasks/abc185_d
# 日付: 2020/12/13

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
#

# ------------------- 解答 --------------------
#code:python
import math
n, m = map(int, input().split())

if n==m:
    print(0)
    exit()
if m==0:
    print(1)
    exit()

a = list(map(int, input().split()))
a.sort()
if not 1 in a:
    a = [0] + a
if not n in a:
    a = a + [n + 1]

k = 10**10
for i in range(len(a)-1):
    if a[i+1]-a[i]-1 != 0:
        k = min(k, a[i+1]-a[i]-1)

ans = 0
for i in range(len(a)-1):
    ans += math.ceil((a[i+1]-a[i]-1)/k)
print(ans)

# AC9, WA12, RE9
# AC17, WA13

# ------------------ 入力例 -------------------
14 3
2 6 12

5 2
1 3

13 3
13 3 9

5 5
5 2 1 4 3

1 0


4 3
1 2 4


# ----------------- 解答時間 ------------------
#

# -------------- 解説 / 感想 / 反省 -------------
#

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい