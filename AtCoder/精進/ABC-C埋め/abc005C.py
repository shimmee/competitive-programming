# ABC005C - おいしいたこ焼きの売り方
# URL: https://atcoder.jp/contests/abc005/tasks/abc005_3
# 日付: 2020/12/14

# ---------- 思ったこと / 気づいたこと ----------
# 古いたこ焼きから売っていく貪欲法

# ------------------- 方針 --------------------
# 各たこ焼きの売れる時間帯の閉区間のリストA_をつくる
# 作るたこ焼きが売れたかどうかのフラッグリストsold
# 各お客さんに売ったかどうかのフラッグリストserve
# お客さんとたこ焼きでループを回す
# お客さんが来た時間に提供できるたこ焼きがあれば，soldとserveをTrueにする
# たこ焼きのループが回り終わったときに，お客さんiにserveできてなければNO
# ループが無事周り終われば全員に売れているのでOK


# ------------------- 解答 --------------------
#code:python
t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_ = [[i, i+t] for i in A]
sold = [False]*n
serve = [False]*m
for i in range(m):
    b = B[i]
    for j in range(n):
        a = A_[j]
        if (not sold[j]) and a[0] <= b <= a[1]: # 売れてなくてかつ，時間的に販売可能
            sold[j] = True
            serve[i] = True
            break
        else:
            continue
    if not serve[i]: # もしi番目のお客さんに売れてなかったらダメ
        print('no')
        exit()
print('yes')


# ------------------ 入力例 -------------------
1
3
1 2 3
3
2 3 4

1
3
1 2 3
3
2 3 5

1
3
1 2 3
10
1 2 3 4 5 6 7 8 9 10

1
3
1 2 3
3
1 2 2


2
5
1 3 6 10 15
3
4 8 16

# ----------------- 解答時間 ------------------
# 11分

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc005
# ただの貪欲！

# ----------------- カテゴリ ------------------
#AtCoder #abc
#flagを上手く使う
#貪欲法
