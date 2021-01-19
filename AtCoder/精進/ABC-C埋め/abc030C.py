# ABC030C - 飛行機乗り
# URL: https://atcoder.jp/contests/abc030/tasks/abc030_c
# 日付: 2020/12/22

# ---------- 思ったこと / 気づいたこと ----------
# 貪欲に単純にループかけばいいやん
# 今いる時間に乗れる一番早い時間の便にのる。それだけ
# 尺取法みたいに進んで止まって，みたいな感じ?

# ------------------- 方針 --------------------
# A,Bそれぞれの出発時刻のリストをdequeで管理
# 今いる空港と現在の時刻を変数で管理
# 今いる空港の最新の出発時間をdequeからpopして，現在時刻に間に合えば飛ぶ，間に合わなければ次の時刻をpop
# 間に合う場合には，出発時刻+x (Bならy)で現在時刻を更新
# Bを出発した回数が往復の回数になるので，Bを出発できた時点でインクリメント
# 現在AにいてAの出発時刻のdequeが空になる or Bにいてリストが空になる，と何もできなくなるので終了
# O(N+M)で解ける

# ------------------- 解答 --------------------
#code:python
from collections import deque

n, m = map(int, input().split())
x, y = map(int, input().split())
a = deque(map(int, input().split()))
b = deque(map(int, input().split()))

time = 0
here = 'a'
ans = 0

while True:
    if here == 'a': # Aにいるとき
        # 便がなくなれば終わり
        if len(a) == 0:
            break
        next_departure = a.popleft()
        if time <= next_departure: # 時間が間に合えば乗ってBにいける
            here = 'b'
            time = next_departure + x

    elif here == 'b': # Bにいるとき
        # 便がなくなれば終わり
        if len(b) == 0:
            break
        next_departure = b.popleft()
        if time <= next_departure: # 時間が間に合えば乗ってBにいける
            here = 'a'
            time = next_departure + y
            ans += 1 # 往復できるのでインクリメント

print(ans)

# 解けた!!
# 解説みてみたら二分探索とか書いてる: https://www.slideshare.net/chokudai/abc030
# 他の人の解説見たら二分探索じゃなくてもいいよねって書いてる。Nが小さいし
# https://kmjp.hatenablog.jp/entry/2015/10/24/1000
# 今いる時刻に最も近い出発時刻の飛行機を貪欲に探せばよい。lower_bound等で二分探索してもよいし、尺取法の要領でもよい。


# ------------------ 入力例 -------------------
3 4
2 3
1 5 7
3 8 12 13

1 1
1 1
1
1

6 7
5 3
1 7 12 19 20 26
4 9 15 23 24 31 33


# ----------------- 解答時間 ------------------
# 15分: コピペみすって時間かかった

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc030
# 満点解法は二分探索とか書いてるけどいらない

# ----------------- カテゴリ ------------------
#AtCoder #abc
#全探索?
