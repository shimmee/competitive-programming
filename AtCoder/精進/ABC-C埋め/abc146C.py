# ABC146C - Buy an Integer
# URL: https://atcoder.jp/contests/abc146/tasks/abc146_c
# 日付: 2020/11/23

# ------------------- 方針 --------------------
# 桁が高々xの桁以下なので，全探索できるそう

# ------------------- 解答 --------------------
#code:python
a,b,x=map(int, input().split())
d = [] #桁数のパターン
for i in range(1, len(str(x))+1):
    if b*i <= x:
        d.append(i)

# 桁数を全探索
ans = 0
for i in d:
    a_n = x-b*i
    n = a_n//a

    if len(str(n)) == i: # 桁数とnが一致しているときだけOK
        ans = max(ans, a_n//a) #nの最大値を更新
print(min(ans, 10**9))

# 1ケースだけWA: 完全にコーナーケース
# 解説見たら二分探索だった
# 10**9からどんどん探していく

a,b,x=map(int, input().split())
# okが左側
ok = 0 # 絶対にOKの数
ng = 10**10 # 絶対にngの数
while (abs(ng - ok) > 1):
    mid = (ok + ng) // 2
    d = len(str(mid))
    cost = a*mid+b*d
    if x >= cost:
        ok = mid
    else: ng = mid
print(min(ok, 10**9))


# ------------------ 入力例 -------------------
10 7 100
2 1 100000000000

1234 56789 314159265

# ----------------- 解答時間 ------------------
# 30分以上

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc146/editorial.pdf
# 二分探索思いつかなかった悔しい
# 最初のやり方でなんでだめだったのかよくわからん

# ----------------- カテゴリ ------------------
#AtCoder #abc
#二分探索
