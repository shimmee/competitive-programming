# ABC119C - Synthetic Kadomatsu
# URL: https://atcoder.jp/contests/abc119/tasks/abc119_c
# 日付: 2020/12/01

# ---------- 思ったこと / 気づいたこと ----------
#



# ------------------- 解答 --------------------
#code:python
import itertools
def get_min_dist(abc, l):
    min_dist = 10**10
    pattern = list(itertools.permutations([i for i in range(len(l))], len(abc)))
    for p in pattern:
        dist = 0
        for i in range(len(p)):
            dist += abs(abc[i]-l[p[i]])
        min_dist = min(min_dist, dist)
    return min_dist

n, a, b, c = map(int, input().split())
abc = [a,b,c]
l = [int(input()) for _ in range(n)]

# abcとlに同じ要素があれば，もはや出来上がっているので消す
remove_list = []
for i in abc:
    if i in l:
        remove_list.append(i)
for i in remove_list:
    abc.remove(i)
    l.remove(i)
abc.sort()
l.sort()

ans = get_min_dist(abc, l)

if len(l) > len(abc) and len(abc) > 0:
    for k in range(1, n-len(abc)+1): # k回 合成魔法
        comb = list(itertools.combinations([i for i in range(len(l))], 2))
        for c1, c2 in comb:
            l_ = l[:]
            new = l_[c1] + l_[c2]
            if new > max(abc):
                continue
            else:
                for index in sorted([c1, c2], reverse=True):
                    del l_[index]
                l_.append(new)
                dist = get_min_dist(abc, l_) + k*10
                if ans > dist:
                    l_best = l_[:]
                    ans = dist
        l = l_best[:]
print(ans)



# WAです。複雑すぎます。もう少しシンプルに考えましょう。
# 4進数のbit全探索でうまくかけそう
# つまり，Aの材料にする，Bの材料にする，Cの材料にする，使わないの4種類
import itertools
n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

# 0ならAの材料，1ならBの材料，2ならCの材料，3なら使わない
pattern = itertools.product([0,1,2,3], repeat=n)
ans = 10**10
for p in pattern:
    abc_l = [0, 0, 0] # 竹を組み合わせてA,B,Cに対応する長さを作る
    for i in range(n):
        if p[i] == 0: abc_l[0] += l[i] # 0ならAの材料
        if p[i] == 1: abc_l[1] += l[i] # 1ならBの材料
        if p[i] == 2: abc_l[2] += l[i] # 2ならCの材料
    if 0 in abc_l: continue # 1本でも長さ0だったら，ルール違反

    # 竹と目標ABCの距離 = 延長魔法と短縮魔法の必要MP
    dist = abs(abc_l[0]-a) + abs(abc_l[1]-b) + abs(abc_l[2]-c)
    # 合成魔法のMP=使う回数*10
    dist += (n-3-p.count(3))*10

    ans = min(ans, dist)
print(ans)


# bit全探索のテンプレ
import itertools
pattern = itertools.product([0, 1], repeat=n)
for p in pattern:
    for i in range(n):
        if p[i] == 1:


# ------------------ 入力例 -------------------
5 100 90 80
98
40
30
21
80

8 100 90 80
100
100
90
90
90
80
80
80

8 1000 800 100
300
333
400
444
500
555
600
666

# ----------------- 解答時間 ------------------
# 解説ACした:

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc119/editorial.pdf
# bit全探索するとき bit演算で表現してたけど，product使ったほうが良さそう
# C問題のなかでトップを争う難しさらしい
# 解説見たら再帰(dfs)で解いてる。そろそろちゃんと書けるようにならなきゃ。

# ----------------- カテゴリ ------------------
#AtCoder #abc
#bit全探索
#4進数
#itertools
#再帰関数
