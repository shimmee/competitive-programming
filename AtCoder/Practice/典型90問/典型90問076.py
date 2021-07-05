# 典型90問076 - Cake Cut（★3）
# URL: https://atcoder.jp/contests/typical90/tasks/typical90_bx
# Date: 2021/06/24

# ---------- Ideas ----------
# 尺取法します
# rightがn未満なら，rightは常にleft以上
# rightがnを超えてたら，rightをnで割った余りがleftを超えてはダメ

# 今日のやつnで割った余りとか面倒なことしなくても，入力の配列を2つ繋げればいいだけかも

# ------------------- Answer --------------------
#code:python
n = int(input())
A = list(map(int, input().split()))

if sum(A) % 10 != 0: print('No'); exit()
obj = sum(A)//10

right = 0
sumA = A[0]
for left in range(n):
    while ((right < n-1) or (right >= n-1 and (right+1) % n < left)) and sumA < obj:
        right = right+1
        sumA += A[right % n]

    if sumA == obj:
        print('Yes')
        exit()
        break

    # もしleftがrightに追いついていたらrightを1つ右に
    if left == right+1:
        right += 1
    else:
        # leftが右に1つ動くので，sumAから引いておく
        sumA -= A[left]

print('No')

#################################
# 配列Aを2つ繋げて考える: 普通に尺取
#################################

n = int(input())
A = list(map(int, input().split()))

if sum(A) % 10 != 0: print('No'); exit()
obj = sum(A)//10
A = A + A

right = 0
sumA = A[0]
for left in range(n):
    # rightを行ける最大限右に行かせる
    while right < left + n and sumA < obj:
        right = right+1
        sumA += A[right]

    # 今の時点でobjに一致してたら出力して終わり
    if sumA == obj:
        print('Yes')
        exit()
        break

    # もしleftがrightに追いついていたらrightを1つ右に
    if left == right+1:
        right += 1
    else:
        # leftが右に1つ動くので，sumAから引いておく
        sumA -= A[left]

print('No')

#################################
# 上のを短く書く
#################################

n = int(input())
A = list(map(int, input().split()))
obj = sum(A)/10
A = A + A

right = 0
sumA = A[0]
for left in range(n):
    while right < left + n and sumA < obj:
        right = right+1
        sumA += A[right]
    if sumA == obj: print('Yes'); exit()
    if left == right+1: right += 1
    else: sumA -= A[left]
print('No')


#################################
# 累積和 + 二分探索で解いてみる
#################################

from itertools import accumulate
n = int(input())
A = list(map(int, input().split()))

if sum(A) % 10 != 0: print('No'); exit()
obj = sum(A)//10

cum = [0] + list(accumulate(A+A))
for i in range(n): # スタート地点
    # iからjまでの和が初めてobj以上になるようなjを探す (ただし，jはi+n以下じゃないとダメ)
    # sumA = A[i]+A[i+1]+...+A[j] = cum[j]-cum[i] <= objの間は右にmidを進める

    # 左がOKの二分探索:
    ok = i # 絶対okの範囲
    ng = n+i # 絶対にngの範囲
    while (abs(ng - ok) > 1):
        mid = (ok + ng) // 2
        sumA = cum[mid] - cum[i]
        if sumA <= obj:
            ok = mid
        else:
            ng = mid

    # iからokまでの和がobjに一致してたらOK
    if cum[ok] - cum[i] == obj:
        print('Yes')
        exit()
        break
print('No')



# ------------------ Sample Input -------------------


5
1 20 7 1 1

4
2 11 16 1

10
1 1 1 1 1 1 1 1 1 1

3
1 18 1
# ----------------- Length of time ------------------
#

# -------------- Editorial / my impression -------------
#

# ----------------- Category ------------------
#AtCoder
#累積和
#尺取法
#しゃくとり法
#二分探索
#円
#円を2倍にする
#典型90問