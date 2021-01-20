# 「みんなのプロコン2019」C - When I hit my pocket...
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_c
# 日付: 2020/12/30

# ---------- 思ったこと / 気づいたこと ----------
# 2回使ってA枚をB枚にふやす
# A+2 <= Bだったら交換したほうがいい
# そうじゃなければ叩き続けたほうがいい
# 交換するにはA枚必要
# A枚まで増やして交換を続ける

# O(1)でとく必要がある

# ------------------- 方針 --------------------
# 貪欲のはず


# ------------------- 解答 --------------------
#code:python
k, a, b = map(int, input().split())
cnt = 0 # 回数
biscuits = 1
if b-a >= 2: # できるだけ交換したほうがいい
    # 最初biscuitsがaに足りなければ，それまで叩く
    cnt += min(a-biscuits, k)
    biscuits = a # この時点でビスケットはA枚ある

    # 残り回数k-cntが偶数なら最大限交換し続ける
    if (k-cnt) % 2 == 0:
        biscuits += (b - a) * ((k-cnt) // 2)
    else: # 奇数なら
        biscuits += (b - a) * ((k - cnt) // 2) + 1
else:
    biscuits += k
print(biscuits)


# ------------------ 入力例 -------------------
4 2 6

7 3 4

314159265 35897932 384626433

# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/yahoo-procon2019-qual/editorial.pdf
# 貪欲と気づけてよかった。
# この問題ににてる: https://atcoder.jp/contests/abc180/tasks/abc180_d

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#貪欲法