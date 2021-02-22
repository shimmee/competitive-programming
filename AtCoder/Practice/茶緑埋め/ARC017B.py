# ARC017B - 解像度が低い。
# URL: https://atcoder.jp/contests/arc017/tasks/arc017_2
# Date: 2021/02/20

# ---------- Ideas ----------
# 連続部分列
# 狭義単調増加
# 事前計算
# 連続で続く単調増加列の長さがわかればOK

# ------------------- Solution --------------------
# 単調増加の長さを測って，リストに保存
# k=3で，リストが[5,4]なら，3個＋2個できるので，5でOK

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

cnt = [] # 単調増加の長さを入れる
now = 1
for i in range(n-1):
    if A[i] < A[i+1]:
        now += 1
    else:
        if now >= k:
            cnt.append(now)
        now = 1

# 余った子を入れてあげる
if now >= k:
    cnt.append(now)

ans = 0
for i in cnt:
    ans += i - k + 1
print(ans)

# ACした!!
# けどよく考えたらリスト作らなくても，単調増加が終わるたびに随時ansにインクリメントすればいいやん
n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

cnt = 1
ans = 0
for i in range(n-1):
    if A[i] < A[i+1]:
        cnt += 1
    else:
        if cnt >= k:
           ans += cnt - k + 1
        cnt = 1
if cnt >= k:
    ans += cnt - k + 1
print(ans)
# ------------------ Sample Input -------------------
10 4
100
300
600
700
800
400
500
800
900
900


10 3
10
40
50
80
90
30
20
40
90
95


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc017/tasks/arc017_2
# 簡単に解けた！
#

# ----------------- Category ------------------
#AtCoder
#連続部分列
#単調増加
#数え上げ問題
#緑diff