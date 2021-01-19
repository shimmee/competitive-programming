# AGC032A - Limited Insertion
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc032/tasks/agc032_a
# Date: 2021/01/06

# ---------- Ideas ----------
# 深さ優先探索っぽいな
# まずj=b_jとなってるものを探して，抜いてみる。
# またj=b_jとなってるものを探して抜いてみる。これを繰り返して全部なくせればOK

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python

import sys
sys.setrecursionlimit(1000000)
n = int(input())
b = list(map(int, input().split()))
b = [i-1 for i in b]

def dfs(b):
    if len(b) == 0:
        return []

    # j=b_jとなっている全てのインデックス
    l = [i for i in range(len(b)) if i == b[i]]
    if len(l) == 0:
        return -1

    a = b[:]

    for i in l:
        a = b[:]
        a.pop(i)
        ans = dfs(a)
        if ans != -1:
            ans.append(i)

    return ans
ans = dfs(b)

if ans == -1:
    print(-1)
else:
    for i in ans:
        print(i+1, end = ' ')

# サンプルは通る。このやり方は正しい答えを得られる。しかし，100**100になるのでTLEになる
# 1:04 半分以上TLEなのでgive up
# 解説: https://img.atcoder.jp/agc032/editorial.pdf
# 後ろから削っていく
n = int(input())
b = list(map(int, input().split()))
b = [i-1 for i in b]

ans = []
for i in range(len(b)):
    for j in reversed(range(len(b))):
        if j == b[j]:
            ans.append(j)
            b.pop(j)
            break

if len(ans) == n:
    for i in ans[::-1]:
        print(i + 1, end=' ')
else:
    print(-1)
# ------------------ Sample Input -------------------
3
1 2 1

2
2 2


9
1 1 1 2 2 1 2 3 2

# ----------------- Length of time ------------------
# 解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc032/editorial.pdf
# 再帰関数で全部試すんや！と意気込んで，100**100をやってしまった
# 後ろから見ればいいことに気づかなかった

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#AC_with_editorial #解説AC
#wanna_review #medium復習
#後ろから見る
#BFSでは間に合わない