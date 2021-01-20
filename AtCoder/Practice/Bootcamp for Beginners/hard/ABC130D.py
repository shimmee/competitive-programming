# ABC130D - Enough Array
# Bootcamp For Beginners - Hard
# URL: https://atcoder.jp/contests/abc130/tasks/abc130_d
# Date: 2021/01/13

# ---------- Ideas ----------
# K以下だったら尺取法で行ける
# K以下じゃなくてK以上なのが厄介
# しゃくとり法で右に動かしていって，Kを超えた時点で，それ以上右に行っても増え続けるだけなんだから，その分インクリメントする
# Kを超えたらやめる

# ------------------- Solution -------------------- 
# 

# ------------------- Answer --------------------
#code:python
n, k = map(int, input().split())
a = list(map(int, input().split()))

right = 0
ans = 0
total = a[0]  # leftからrightまでの区間で関心のあるものを溜め込むリストorセットを作る

for left in range(n):  # leftをループで動かす。

    # あるleftに対して，rightを行ける所まで右に動かす
    while (right < n - 1) and (total + a[right + 1] < k):  # 次のものをトータルに足してkに届いてなければ
        total += a[right + 1]
        right += 1  # 右にすすめる

    if right < n - 1:
        if total + a[right + 1] >= k:
            ans += n - (right + 1)
    else:
        if total >= k:
            ans += 1

    if left == right:  # leftがrightに追いついたらrightを+1して両方すすめる
        right += 1
        total += a[right]
    else:  # leftがrightに追いついてないなら，totalからleftの分を引く
        total -= a[left]

print(ans)
# 2/29WA

# 解説: https://img.atcoder.jp/abc130/editorial.pdf
# 累積和を取ってから二分探索か尺取法
# 二分探索で解いてみる
n, k = map(int, input().split())
a = list(map(int, input().split()))

from itertools import accumulate
cum = [0] + list(accumulate(a))
ans = 0
for i in range(n):

    # 右がOKの二分探索
    ok = n
    ng = i-1
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if cum[mid] - cum[i] >= k:
            ok = mid
        else:
            ng = mid
    if cum[ok] - cum[i] >= k:
        ans += n - ok + 1
print(ans)


# bisectで解いてみる
# 参考: https://ami-atcoder.hatenablog.com/entry/20190621/1561089016
n, k = map(int, input().split())
a = list(map(int, input().split()))

from itertools import accumulate
from bisect import bisect_left
cum = [0] + list(accumulate(a))
ans = 0
for i in range(n):
    idx = bisect_left(cum, k + cum[i])
    ans += n - idx + 1
print(ans)


# しゃくとり法で解き直し 2021/01/14

n, k = map(int, input().split())
a = list(map(int, input().split()))

right = 0
ans = 0
total = a[0]  # leftからrightまでの区間で関心のあるものを溜め込むリストorセットを作る

for left in range(n):  # leftをループで動かす。

    while right < n-1 and total < k: # leftからの合計がkを超えるまでrightを動かす
        right += 1
        total += a[right]
    if total >= k:
        ans += n - right

    # leftが次右に一つ動くので，totalから引いておく
    total -= a[left]

print(ans)

# 今まで解いたしゃくとり法と少し違う
# 違う点: if left == right:だったらright+=1という部分が最後にない
# これはleftが追いついたとしても，次で必ずrightが右に移るので，いらないということ

# ------------------ Sample Input -------------------
8 10
6 1 2 7 10 1 2 1


3 5
3 3 3

10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352


4 10
6 1 2 7


# ----------------- Length of time ------------------
# 1.5hで解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/abc130/editorial.pdf
# 尺取法で考え方は完全にあってるのになぜかサンプルですらWAがでる
# 尺取法でインデックスが一生バグったので解説みた
# 累積和とってから二分探索で書いたら簡単にかけた
# bisect使えるようになりたい
# 尺取法でやり直した

# ----------------- Category ------------------
#AtCoder  
#BootcampForBeginners-hard
#AC_with_editorial #解説AC
#wanna_review #hard復習 #復習したい
#二分探索
#しゃくとり法
#ABC-D
#累積和
