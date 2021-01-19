# キーエンス プログラミング コンテスト 2019 C - Exam and Wizard
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/keyence2019/tasks/keyence2019_c
# Date: 2021/01/09

# ---------- Ideas ----------
# AとBの差を考える
# AがBに足りない場合は必ず他のiの数字から借りる必要がある
# A-Bが正で大きいiについては余裕があるので，そういうiから貪欲に移していく
# そうすれば他のiを変えずに住む



# ------------------- Answer --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# aの総和<bの総和のときは無理
if sum(a) < sum(b):
    print(-1); exit()

# aの全ての要素がbより大きければ変更の必要なし
elif all(a[i] >= b[i] for i in range(n)):
    print(0); exit()

# 各iについてA-Bを求める: 負なら他から助けが必要，正なら余裕あり
sa = [a[i]-b[i] for i in range(n)]

cnt = len([i for i in sa if i < 0])  # 変更するiの個数: 初期値はsaが負の数の個数
gap = sum([i for i in sa if i < 0]) # 残り埋める必要のある点数: saのうち負の数の和
plus = sorted([i for i in sa if i > 0], reverse=True) # saが正の要素を降順にソート

# 一番余裕のあるiから使って，gapを埋めていく。gapが0以上になったらOK
for i in plus:
    cnt += 1
    gap += i

    if gap >= 0: break
print(cnt)


# ------------------ Sample Input -------------------
3
2 3 5
3 4 1

3
2 3 3
2 2 1

3
17 7 1
25 6 14


12
757232153 372327760 440075441 195848680 354974235 458054863 463477172 740174259 615762794 632963102 529866931 64991604
74164189 98239366 465611891 362739947 147060907 118867039 63189252 78303147 501410831 110823640 122948912 572905212

# ----------------- Length of time ------------------
# 14分AC!!!

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/keyence2019/editorial.pdf
# Completely same answer with the editorial!

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#greedy
#貪欲法
#ソートして貪欲