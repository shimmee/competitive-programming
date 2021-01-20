# ABC130C - Rectangle Cutting
# URL:https://atcoder.jp/contests/abc130/tasks/abc130_c
# 日付: 2020/11/26

# ---------- 思ったこと / 気づいたこと ----------
# ただのif文では？
#

# ------------------- 解答 --------------------
#code:python
w,h,x,y=map(int, input().split())

# 縦に切る
l = x*h
r=(w-x)*h
tate = min(l, r)

# 横にきる
u=w*(h-y)
d=w*y
yoko=min(u,d)

if tate==yoko:
    print(tate, 1)
else:
    print(max(tate, yoko), 0)

# 3ケースWA
# 縦横に切るだけじゃなくて斜めにもきってOK っぽい
# そしたら必ず半分に割れる気がする。常に(w*h)//2が答え
# 分割方法が複数あるかどうかはxとyが対照かどうか
# x,yがそれぞれ0-wとo-hの中点にあればOK

w,h,x,y=map(int, input().split())
area = (w*h)/2
if x == w/2 and y == h/2:
    print(area, 1)
else:
    print(area, 0)



# ------------------ 入力例 -------------------
2 3 1 2

2 2 1 1

# ----------------- 解答時間 ------------------
# 20分AC

# -------------- 解説 / 感想 / 反省 -------------
# 問題文が不親切で，斜めに切ることに気づかなかった
# でも面白かった。良い幾何だった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#
