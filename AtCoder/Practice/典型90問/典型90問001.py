# 典型90問001 - Yokan Party
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_a
# Date: 2021/05/10

# ---------- Ideas ----------
# 二分探索で答えを決め打ちして，Pとする
# そのPを実現する切り方が可能かどうかを判定する
# 左から順に切れ目を進んでいって，pを超えたら切る。
# 切った回数がkに達したらbreak
# ちゃんとbreakして，かつ最後に切った場所(now)から末端(L)までの距離がpを超えてたらTrue
# 切った回数がkに達さなかったら，pを達成できないということなのでFalse

# ------------------- Answer --------------------
#code:python
n, L  = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))
A = [0] + A + [L]

def judge(p):
    cnt = 0
    now = 0 # 最後に切った場所のcm
    flag = False # k回きり終わったフラッグ
    for i in range(1, n+1): # 左から順に切れ目を進んでいって，pを超えたら切る。
        if A[i] - now >= p:
            cnt += 1
            now = A[i]
        if cnt == k: # 切った回数がkに達したらbreak
            flag = True
            break
    if flag and L - now >= p:
        return True
    else:
        return False


# 左がOKの二分探索
ok = 0 # 絶対okの範囲
ng = 10**10 # 絶対にngの範囲
while (abs(ng - ok) > 1):
    mid = (ok + ng) // 2
    if judge(mid): # 条件
        ok = mid
    else:
        ng = mid

print(ok)
# ------------------ Sample Input -------------------
3 34
1
8 13 26

7 45
2
7 11 16 20 28 34 38

# ----------------- Length of time ------------------
# 22分

# -------------- Editorial / my impression -------------
# The決め打ち二分探索という感じの問題だった
# 緑diffはあると思う
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/001.jpg

# ----------------- Category ------------------
#AtCoder
#典型90問
#二分探索
#binary_search
#決め打ち二分探索