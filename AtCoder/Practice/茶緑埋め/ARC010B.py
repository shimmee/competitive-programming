# ARC010B - 超大型連休
# URL: https://atcoder.jp/contests/arc010/tasks/arc010_2
# Date: 2021/02/25

# ---------- Ideas ----------
# 土日のフラッグを立てたリストを作成
# 入力の日付を「1年の何日目か」に変換してリスト作成
# 366日でループを回して，残りの振替休日の日数を管理しながら，平日が来たらそれを消費

# ------------------- Answer --------------------
#code:python
from itertools import accumulate
n = int(input())
holiday = [1,0,0,0,0,0,1]*52 + [1] + [0]
day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list_cum = [0] + list(accumulate(day_list))

for _ in range(n):
    month, day = map(int, input().split('/'))
    days = day_list_cum[month-1] + day
    holiday[days - 1] += 1

ans = 0
renkyu = 0
for i in range(366):
    if holiday[i] > 0:
        renkyu += holiday[i]
    else:
        ans = max(ans, renkyu)
        renkyu = 0
print(ans)

# これだと70%くらいがWA
# 2013年に連休が突入してたりしてそう
# やり直し

from itertools import accumulate
n = int(input())
satsun = [True,False,False,False,False,False,True]*52 + [True] + [False]
day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list_cum = [0] + list(accumulate(day_list))

# 入力から祝日一覧リスト
holidays = []
for _ in range(n):
    month, day = map(int, input().split('/'))
    days = day_list_cum[month-1] + day
    holidays.append(days - 1)

substitute = 0 # 振替休日
renkyu = 0
ans = 0
for i in range(366):
    if satsun[i] and (i in holidays): # 今日が休日で祝日でもある: 振替休日が生まれる
        substitute += 1
        renkyu += 1
    elif satsun[i] or (i in holidays): # 今日が土日 or 今日が祝日
        renkyu += 1
    else: # 平日のとき
        if substitute > 0: # 振替休日が残ってれば使用
            renkyu += 1
            substitute -= 1
        else:
            renkyu = 0
    ans = max(ans, renkyu)
print(ans)


# ------------------ Sample Input -------------------
0

2
1/7
1/9

2
2/24
2/25

8
2/24
2/25
9/16
9/17
9/18
9/19
9/20
9/21




# ----------------- Length of time ------------------
# 60分

# -------------- Editorial / my impression -------------
# バグらせ散らかした
# こちらをヒントにACしたhttps://www.slideshare.net/yumainoue965/arc-010-b

# ----------------- Category ------------------
#AtCoder
#日付
#祝日
#ヒントAC