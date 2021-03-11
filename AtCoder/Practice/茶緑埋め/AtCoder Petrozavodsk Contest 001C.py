# AtCoder Petrozavodsk Contest 001C - Vacant Seat
# URL: https://atcoder.jp/contests/apc001/tasks/apc001_c
# Date: 2021/03/10

# ---------- Ideas ----------
# 空席がなければ男女男女男女...と並んでいるが，空席があればどこかでずれる
# 二分探索っぽく解けそう
# 20回までクエリを与えられるので，2**20=1048576の長さであれば特定できる。N<=99999なので余裕で行ける
# 男女男女と並んでいれば，o-indexedで偶数番目に男，奇数番目に女が座っているはず。
# 2, 4, 8, 16という感じでクエリを増やして行って，あるクエリまでは同じなのに，突然違う答えが出てきたら
# 直前のクエリと現在のクエリの間のどこかに空席があると分かる
# けどこの増やすパターンだと後ろの方に1つだけ空席が合った場合，16回目くらいのクエリでやっとクエリのある間隔が特定できるだけなので，そのあと困りそう
# だから大きいのから小さいのにしていく
# 0と(n-1)//2を尋ねる -> もし同じであれば，後半に必ず空席があり，もし異なれば，前半に空席がある
#


# ------------------- Solution --------------------
# low=0, high=n，と初期化して，二分探索みたいに行う
# mid = low + (high-low)//2
# lowとmidをクエリに投げて，それぞれのsを得る
# lowとmidのパリティが同じとき，s_lowとs_midは同じであれば，男女男女と並んでおり，
# lowとmidの間には空席がないことになるので，midとhighの間に空席があることになる。-> lowをmidで更新
# s_lowとs_midが異なれば，男女男女のなかに空席がある。-> highをmidで更新
# これを繰り返して範囲を狭めていって，Vacantがでるまで頑張る
# lowとmidのパリティが異なるときは，この逆でOK

# ------------------- Answer --------------------
#code:python
def isVacant(s):
    if s == 'Vacant':
        exit()
n = int(input())
low = 0
high = n

print(low)
s_low = input()
isVacant(s_low)

for _ in range(19):

    mid = (high - low) // 2 + low
    print(mid)
    s_mid = input()
    isVacant(s_mid)

    if low % 2 == mid % 2: # 偶奇が一致してる時:
        if s_low == s_mid: # 同じ文字であれば後半に空席がある
            low = mid
        else: # 前半に空席があるので，highをmidで更新
            high = mid

    else: # 偶奇が一致していないとき
        if s_low != s_mid: # 後半に空席があるので，lowとmidで更新
            low = mid
            s_low = s_mid
        else: # 前半に空席があるので，highをmidで更新
            high = mid

# ACしたけど
# もう少しきれいに描けそう

def get_input(s):
    print(s)
    s = input()
    if s == 'Vacant':
        exit()
    else:
        return s
n = int(input())
low = 0
high = n

s_low = get_input(low)

for _ in range(19):
    mid = (high - low) // 2 + low
    s_mid = get_input(mid)

    if (low % 2 == mid % 2 and s_low == s_mid) or (low % 2 != mid % 2 and s_low != s_mid):
        low = mid
        s_low = s_mid
    else:
        high = mid

# ----------------- Length of time ------------------
# 49分

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/apc001/editorial.pdf
# 二分探索はソートされた単調な数列にしか適用できないと思っていたが，そうではなかった。
# 初めてのインタラクティブ問題だった
# 自力で解けたのがとても嬉しい
# けんちょんさん: https://drken1215.hatenablog.com/entry/2020/03/16/155800

# ----------------- Category ------------------
#AtCoder
#インタラクティブ
#二分探索
#境界のうちの1つを見つける二分探索
#数珠
#循環するものを二周させる
#パリティ
#緑diff