# ARC113C - String Invasion
# URL: https://atcoder.jp/contests/arc113/tasks/arc113_c
# Date: 2021/02/21

# ---------- Ideas ----------
# 後ろから貪欲に見ていく: 後ろにある2個以上連続を右に侵食させる
# aabceefg -> aabceeee -> aaaaaaaa
# 同じ侵食が2回連続だと，書き換わる分が少ないのに注意: arrarra -> arrarrr (1個) -> arrrrrr (1個)
# まずgroupbyで[s=連続する文字, a=連続の始まりidx, b=終わりidx]をリストで用意する
# 後ろから見るためにリストを反転
# 前回までの侵食で侵食した長さをdとする，nowを前回の侵食した文字とする
# 今回の侵食のstart=b+1, 前回の侵食までの直前goal=n-d
# 今回侵食できる分 = nowがsと異なるならd分行ける + startとgoalの間に存在するsじゃない文字列は侵食できる


# ------------------- Answer --------------------
#code:python
S = input()
n = len(S)

from itertools import groupby
gr = groupby(S)
l = []
now = 0
for key, group in gr:
    m = len(list(group))
    if m >= 2:
        l.append([key, now, now+m-1])
    now += m

l = l[::-1]

ans = 0
d = 0 # 前回までの侵食の長さ
now = None
for s, a, b in l:
    start = b + 1
    goal = n - d
    cnt = 0
    # startからgoalの間のsの個数を数える: この分は侵食できない
    for i in range(start, goal):
        if S[i] == s:
            cnt += 1

    # nowがsと異なるならd分行ける: 一緒ならdは侵食できない
    if now == s:
        ans += n - start - cnt - d
    else:
        ans += n - start - cnt

    # dとnowを更新
    d += goal - a
    now = s
print(ans)

# ------------------ Sample Input -------------------
anerroroccurred
arrarra
aabccd
aaaaaaaa
aabcdeee
aaabbbc



# ----------------- Length of time ------------------
# 40分

# -------------- Editorial / my impression -------------
#
# 初めてARCのC問題解けた！
# この問題が解けたおかげでレートが812になって緑コーダーになった！
# インデックスバグりそうだったけどなんとかなった

# ----------------- Category ------------------
#AtCoder
#ARC-C
#文字列操作
#貪欲
#greedy
#groupby