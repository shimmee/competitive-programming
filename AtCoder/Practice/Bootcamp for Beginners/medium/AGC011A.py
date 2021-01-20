# AGC011A - Airport Bus
# Bootcamp For Beginners - Medium
# URL:
# 日付: 2020/12/30

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 貪欲に解いてみる
# 手前の人からどんどん載せない理由がない
# ソートしたいけど，数が大きすぎて全部読み込めないから厳しそう -> 行ける

# ------------------- 解答 --------------------
#code:python

n, c, k = map(int, input().split())
T = [int(input()) for _ in range(n)]
T.sort()

# 1人目の乗客
first = T[0]
passenger = 1

ans = 0
for i in range(1, n):
    t = T[i]
    # 次の人を載せようとしたときに，バスの定員を満たすか，firstの時間＋kになったらバスは出発
    if passenger + 1 > c or first + k < t:
        first = t
        passenger = 1
        ans += 1 # バス出発でインクリメント
    else:
        if i == n-1: # 最後の人だったら出発させる
            ans += 1  # バス出発でインクリメント
            passenger = 0 # 乗客は0人になる
        else:
            passenger += 1
if passenger > 0:
    print(ans+1)
else:
    print(ans)


# ------------------ 入力例 -------------------
5 3 5
1
2
3
6
12

6 3 3
7
6
2
8
10
6

# ----------------- 解答時間 ------------------
# 30分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/agc011/editorial.pdf
# ただの貪欲なのに，ちょっと時間がかかりすぎ

# ----------------- カテゴリ ------------------
#AtCoder
#BootcampForBeginners-medium
#貪欲法
