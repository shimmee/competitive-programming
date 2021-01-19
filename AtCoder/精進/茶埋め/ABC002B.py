# ABC002B - 割り切れる日付
# URL: https://atcoder.jp/contests/arc002/tasks/arc002_2
# Date: 2021/01/18

# ---------- Ideas ----------
# 1月1日には必ずy÷m÷dが整数になるので，高々365日調べればOK
# 入力の日付をdatetime型に変換
# ループで1日ずつ足していく (今日も含めてOKに注意)
# 足した日付からyear, month, dayを取り出す
# 整数になるか調べて，整数なら出力で終わり
# 出力は0でpadする必要があるので，zfillを用いる

# ------------------- Solution --------------------
#

# ------------------- Answer --------------------
#code:python
import datetime
ymd = input()
now = datetime.datetime.strptime(ymd, '%Y/%m/%d')
for i in range(366):
    next_day = now + datetime.timedelta(days=i)
    y, m, d = next_day.year, next_day.month, next_day.day
    if y/m/d == y//m//d:
        print(f'{y}/{str(m).zfill(2)}/{str(d).zfill(2)}')
        exit()

# ------------------ Sample Input -------------------
2012/05/02
2020/05/02
2088/02/28


# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc002
# datetimeを使う問題は初めてだったので，何かの対策になりそう。
#

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-hard
#ABC-B
#日付
#datetime