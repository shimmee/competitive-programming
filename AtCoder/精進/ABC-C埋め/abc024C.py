# ABC024C - 民族大移動
# URL: https://atcoder.jp/contests/abc024/tasks/abc024_c
# 日付: 2020/12/22

# ---------- 思ったこと / 気づいたこと ----------
# 留まれるということは，最大限いける範囲を考えていけばいい
# 毎日どんどん範囲を広げていって，ゴールにたどり着ければOK

# ------------------- 方針 --------------------
# 各日付において，各民族が移動できる街の区間のリストを作る: 2次元配列
# 民族kと日付dでループを回す
# 民族がkがもしd日目に移動できる街にいるのであれば，行動範囲を広げて，行ける街の範囲を閉区間としてリストに保管する

# ------------------- 解答 --------------------
#code:python
N, D, K = map(int, input().split()) # D日，K個の民族
lr = [[int(i) for i in input().split()] for _ in range(D)]
st = [[int(i) for i in input().split()] for _ in range(K)]

able = [[[] for j in range(K)] for i in range(D+1)]

for k in range(K):
    able[0][k].append([st[k][0], st[k][0]])

flag = [False]*K
ans = [float('INF')]*K
for k in range(K):
    for d in range(1, D+1):
        goal = st[k][1]
        cities = able[d-1][k] # d日の1日前までに民族kが滞在できる街のリスト
        l, r = lr[d-1] # d日に移動できる街の閉区間
        for city in cities: # 現在までに滞在可能な街から，今日移動できるかどうか調べる
            if l <= city[0] <= r  or l <= city[1] <= r: # もしいけるのであれば，行動範囲を広げる
                able[d][k].append([min(city[0], city[1], l, r),
                                   max(city[0], city[1], l, r)])
                if l <= goal <= r: # 今回の移動でゴールできていればbreak
                    ans[k] = d
                    flag[k] = True
            else:
                able[d][k] += cities  # もし今日移動できないのであれば，滞在できる街は昨日と同じ
        if flag[k]:
            break


for i in range(K):
    print(ans[i])

# 解説: https://www.slideshare.net/chokudai/abc024
# 各民族は単純に貪欲に突き進めばいい。進めるのであれば留まる選択肢もあるのだから，大は小を兼ねるで，進めばいい。
# ゴールに到達した時点でOK

N, D, K = map(int, input().split()) # D日，K個の民族
lr = [[int(i) for i in input().split()] for _ in range(D)]
st = [[int(i) for i in input().split()] for _ in range(K)]

ans = [0]*K
for k in range(K):
    now = st[k][0]
    goal = st[k][1]
    flag = False

    for d in range(D):
        l, r = lr[d]
        if l <= now <= r: # 移動可能なら
            if now < goal:
                now = r
                if goal <= now: # ゴールに到達してたら終わり
                    ans[k] = d + 1
                    flag = True
                    break
            else: # 進む方向がゴールより大きいなら負の方向に進みたい
                now = l
                if now <= goal:
                    ans[k] = d + 1
                    flag = True
                    break

for i in range(K):
    print(ans[i])



# ------------------ 入力例 -------------------
10 10 3
1 5
3 6
7 10
5 8
4 4
1 4
2 9
1 3
1 1
4 5
1 6
2 7
10 1

10 10 4
1 2
2 4
3 6
4 8
5 10
9 10
7 8
5 6
3 5
1 3
10 1
3 8
2 4
1 3

314159265 10 1
1 10000
500 12031
1414 113232
111111 777777
666661 23423423
12345678 123456789
111111111 314159265
112334 235235235
1 223445
314 1592
1 314159265

# ----------------- 解答時間 ------------------
# 51分もかかった

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc024
# 「行ける街の中で一番ゴールに近い街だけ管理しておけばいい」ということに気づかず，効率の悪い実装をしてしまった
# 行ける街を全て管理してしまった。
# 復習したい。

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#貪欲法
