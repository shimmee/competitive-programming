# ABC168-C - :colon
# URL: https://atcoder.jp/contests/abc168/tasks/abc168_c
# 日付: 2020/11/21

# ---------- 思ったこと / 気づいたこと ----------
# まずなす角が必要
# 長身は1分で6度，単身は0.5度進む


# ------------------- 解答 --------------------
#code:python
# 参考: https://qiita.com/dannchu/items/ef27ee0b54dc6ebbcda9

import math
a,b,h,m = map(int, input().split())
def angle(h, m):
    return min(abs(m*5.5-h*30)%360, 360 - abs(m*5.5-h*30)%360)

theta = angle(h, m)
c = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(theta)))
print(c)

# ------------------ 入力例 -------------------
3 4 9 0
3 4 10 40


# ----------------- 解答時間 ------------------
# 11分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc168/editorial.pdf
# なす角を計算するのに時間かかった

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#三角関数
#時計
