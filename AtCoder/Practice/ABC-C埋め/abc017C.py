# ABC017C - ハイスコア
# URL: https://atcoder.jp/contests/abc017/tasks/abc017_3
# 日付: 2020/12/12

# ---------- 思ったこと / 気づいたこと ----------
# 取得しない宝石が1つでもあれば魔王は現れないので，どの宝石を取得しないのかを決めたい

# ------------------- 方針 --------------------
# アイデア4を参照

# ------------------- 解答 --------------------
#code:python

# アイデア1: 得点が高い順にソートして貪欲に解いてみる
# 獲得した宝石番号をsetで管理する
n, m = map(int, input().split())
lrs = [[int(i) for i in input().split()] for _ in range(n)]
lrs = sorted(lrs, key=lambda x: x[2], reverse=True)
jewelry = set([])

ans = 0
for i in range(n):
    l, r, s = lrs[i]
    get = set([j for j in range(l, r+1)])
    if len(jewelry.union(get)) == m:
        continue
    else:
        jewelry = jewelry.union(get)
        ans += s
print(ans)

# 63中 40AC, 4WA, 19TLE


# アイデア2: 宝石が少ない順に貪欲に解く
n, m = map(int, input().split())
lrsk = []
for i in range(n):
    l, r, s = map(int, input().split())
    lrsk.append([l, r, s, r-l+1])

lrsk = sorted(lrsk, key=lambda x: (x[3], x[2]))
jewelry = set([])

ans = 0
for i in range(n):
    l, r, s, k = lrsk[i]
    get = set([j for j in range(l, r+1)])
    if len(jewelry.union(get)) == m:
        continue
    else:
        jewelry = jewelry.union(get)
        ans += s
print(ans)
# 63中 38AC, 6WA, 19TLE

# アイデア3: 取得しない宝石1つをループで決めて，各遺跡にその宝石がなかったらインクリメント
n, m = map(int, input().split())
lrs = [[int(i) for i in input().split()] for _ in range(n)]

ans = 0
for j in range(1, m+1): # 取得しない宝石の番号
    score = 0
    for i in range(n): # 遺跡の番号
        l, r, s = lrs[i]
        if j < l or r < j: # もしjがlとrの間に入ってなければOK
            score += s
    ans = max(ans, score)
print(ans)
# 63中 44AC, 19TLE

# アイデア4: アイデア3の無駄を取り除く
# 各宝石jを取り除くときめたときに，その宝石を含む全て遺跡の点数を失うので，失う点数が少なくなるような宝石jを決めたい
# リストl = 「宝石jを取らないと決めた時に失う点の合計」
# これをimos法でゲットする
# lの最小値が，失う点数なので，これをトータルの得点から引けばいい

from itertools import accumulate
n, m = map(int, input().split())
lrs = [[int(i) for i in input().split()] for _ in range(n)]

imos = [0]*(m+2)
total = 0
for i in range(n):
    l, r, s = lrs[i]
    imos[l] += s
    imos[r+1] -= s
    total += s

cum = list(accumulate(imos))
cum.pop(0)
cum.pop()

print(total - min(cum))

# ------------------ 入力例 -------------------
4 6
1 3 30
2 3 40
3 6 25
6 6 10

2 7
1 3 90
5 7 90

1 4
1 4 70


# ----------------- 解答時間 ------------------
# 71分 自力でAC!!! 嬉しい!!!

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc017
# 満点解法と全く同じ解き方ができた！！！！！
# 一番大事だった考え方は「取らない宝石を1つ決める」という点
# 「全部揃うとダメ」なら「揃えないための1つを決める」という発想

# ----------------- カテゴリ ------------------
#AtCoder #abc
#いもす法
#imos
#全部揃うとダメ
