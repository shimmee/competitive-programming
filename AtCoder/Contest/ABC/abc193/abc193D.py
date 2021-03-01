# キャディプログラミングコンテスト2021(AtCoder Beginner Contest 193): D - Poker
# URL: https://atcoder.jp/contests/abc193/tasks/abc193_d
# Date: 2021/02/27

# ---------- Ideas ----------
# カードを全て区別して考える: 組み合わせじゃなくて順列
# 残ってるカードの枚数を数える
# 高橋と青木の裏のカードを全探索する
# 高橋が勝っているとき，2人のカードの引き方の場合の数を数えてインクリメント
# 同じカードを引く時と別のカードを引く時で計算が違うので注意


# ------------------- Answer --------------------
#code:python
from collections import deque, Counter
K = int(input())
S = input()
T = input()
def get_score(string):
    d = Counter(string)
    score = 0
    for i in range(1, 10):
        score += i*10**d[str(i)]
    return score

rest = [K]*9
for i in range(4):
    s = int(S[i]) - 1
    t = int(T[i]) - 1
    rest[s] -= 1
    rest[t] -= 1

total = sum(rest)
all_cases = total*(total-1)
case = 0
for taka in range(1, 10):
    for aoki in range(1, 10):
        S = S[:4] + str(taka)
        T = T[:4] + str(aoki)

        taka_score = get_score(S)
        aoki_score = get_score(T)

        if taka_score > aoki_score: # 高橋のかち
            if taka == aoki and rest[taka-1] >= 2: # 同じかーどが2枚以上残ってれば，2人が同じカードを引ける
                case += rest[taka-1]*(rest[taka-1]-1)
            elif taka != aoki and rest[taka-1] > 0 and rest[aoki-1] > 0: # 別のカードの時
                case += rest[taka-1]*rest[aoki-1]
print(case/all_cases)


# ------------------ Sample Input -------------------
2
1144#
2233#

2
9988#
1122#

6
1122#
2228#

100000
3226#
3597#


# ----------------- Length of time ------------------
# 30分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/abc193/editorial
# 緑diffだった！これが本番で解けたおかげで温まった！

# ----------------- Category ------------------
#AtCoder
#確率
#順列
#文字列
#ゲーム
#緑diff