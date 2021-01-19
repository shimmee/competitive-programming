# ABC013C - 節制
# URL: https://atcoder.jp/contests/abc013/tasks/abc013_3
# 日付: 2020/12/12

# ---------- 思ったこと / 気づいたこと ----------
# DPやん

# ------------------- 方針 --------------------
# DPで考えて，パスタ問題と似てるなと思って考えてたら，全然わからなくて2時間たった
# 解説見た

# ------------------- 解答 --------------------
#code:python

# 解答みた: https://www.slideshare.net/chokudai/abc013
# 100点解答
# 普通の食事の回数をx, 質素な食事をy回，飯抜きを(n-x−y)とする
# xとyをNの範囲で全探索してO(N^2)する
n, h = map(int, input().split())
a,b,c,d,e = map(int, input().split())
ans = float('INF')
for x in range(n+1):
    for y in range(n+1-x):
        z = n - x - y
        if h+b*x+d*y-e*z > 0:
            ans = min(ans, a*x + c*y)
print(ans)

# 101点解答
# 普通の食事の回数xをループで決める
# 不等式から，条件を満たす最小のyを得る
n, h = map(int, input().split())
a,b,c,d,e = map(int, input().split())
ans = float('INF')
for x in range(n+1):
    y = max(0, (e*n-h-(b+e)*x)//(d+e)+1) # yが0を下回る可能性があるので，その場合は0にしたい
    z = n - x - y
    if h + b * x + d * y - e * z > 0:
        ans = min(ans, a * x + c * y)
print(ans)

# ------------------ 入力例 -------------------
4 5
100 4 60 1 4

10 1
5000 2 2000 1 300

653 314159
6728 123456 5141 41928 222222

# ----------------- 解答時間 ------------------
# 解説AC

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc013
# DPかと思ったら貪欲法だった
# 順番を入れ替えていいものであれば，貪欲法に持ち込める可能性があることを覚えておくべき

# ----------------- カテゴリ ------------------
#AtCoder #abc
##解説AC #復習したい
#貪欲法
#不等式




# ゴミ回答
# n, h = map(int, input().split())
# a,b,c,d,e = map(int, input().split())
# food_choice = [b, d, -e]
# cost_choice = [a, c, 0]
#
#
# inf = float('INF')
# # インデックス0,1,2がそれぞれ普通の食事，質素な食事，食事抜き
#
# cost_pre = [[[inf]*3 for _ in range(3)]  for _ in range(3)]
# cost_now = [[[inf]*3 for _ in range(3)]  for _ in range(3)]
# full_pre = [[[0]*3 for _ in range(3)]  for _ in range(3)]
# full_now = [[[0]*3 for _ in range(3)]  for _ in range(3)]
#
# # 1日目の満足度とコスト
# for j in range(3): # 2日前の食事
#     for k in range(3): # 1日前の食事
#         for l in range(3): # 今日の食事
#             full_pre[j][k][l] = h + food_choice[l]
#             cost_pre[j][k][l] = 0 + cost_choice[l]
#
# #
#
# for i in range(1, n):
#     for j in range(3):  # 2日前の食事
#         for k in range(3):  # 1日前の食事
#             for l in range(3):  # 今日の食事
#                 full_now[j][k][l] = full_pre[][][]
#
#
#
# dp_cost = [[[inf for k in range(3)] for j in range(3)] for i in range(n+1)]
# dp_full = [[[0 for k in range(3)] for j in range(3)] for i in range(n+1)]