# ABC025C - 双子と○×ゲーム
# URL: https://atcoder.jp/contests/abc025/tasks/abc025_c
# 日付: 2020/12/12

# ---------- 思ったこと / 気づいたこと ----------
# GIVE UP

# ------------------- 方針 --------------------
# GIVE UP

# ------------------- 解答 --------------------
#code:python
# わかりやすい解説???: https://qiita.com/nomikura/items/1518bc8a6e04d2580b0d

# ゲーム木探索:評価値が最大となる局面を探すこと
# 評価値: 局面の形勢を数値で表したもの
# 評価関数: 評価値を返す関数，探索をシてその局面の有利さを評価値として返す

b = [[int(i) for i in input().split()] for _ in range(2)]
c = [[int(i) for i in input().split()] for _ in range(3)]

def cal_score(field):
    score = 0
    if field[0][0] == field[1][0]: score += b[0][0]
    if field[0][1] == field[1][1]: score += b[0][1]
    if field[0][2] == field[1][2]: score += b[0][2]
    if field[1][0] == field[2][0]: score += b[1][0]
    if field[1][1] == field[2][1]: score += b[1][1]
    if field[1][2] == field[2][2]: score += b[1][2]

    if field[0][0] == field[0][1]: score += c[0][0]
    if field[0][1] == field[0][2]: score += c[0][1]
    if field[1][0] == field[1][1]: score += c[1][0]
    if field[1][1] == field[1][2]: score += c[1][1]
    if field[2][0] == field[2][1]: score += c[2][0]
    if field[2][1] == field[2][2]: score += c[2][1]

    return score

# とりあえずまず最初に全部の盤面9!を列挙する
from itertools import permutations
all_pattern = list(permutations([i+1 for i in range(9)])) # 1-9は盤面のマス番号を表す: 左上が1，右下が9

ans = 0
for pattern in all_pattern:
    field = [['*'] * 3 for _ in range(3)]
    for k, p in enumerate(pattern):
        i, j = divmod(p-1, 3)
        if (k+1) % 2 == 1: # 直大の番
            field[i][j] = 'o'
        else:
            field[i][j] = 'x'
    ans = max(ans, cal_score(field))






b = [[int(i) for i in input().split()] for _ in range(2)]
c = [[int(i) for i in input().split()] for _ in range(3)]

S = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        s = []
        if i == 0: s.append(b[0][j])
        if i == 1: s.append(b[0][j]), s.append(b[1][j])
        if i == 2: s.append(b[1][j])

        if j == 0: s.append(c[i][0])
        if i == 1: s.append(c[i][0]), s.append(c[i][1])
        if j == 2: s.append(c[i][1])

        S[i][j] = max(s)


S[0][0] = min(b[0][0], c[0][0])
S[0][1] = min(b[0][1], c[0][0], c[0][0])


# ------------------ 入力例 -------------------
0 15 0
0 0 25
20 10
0 0
25 0


# ----------------- 解答時間 ------------------
# ACしてません

# -------------- 解説 / 感想 / 反省 -------------
# ゲーム木探索とミニマックス法がキーワード
# 9!の全局面を探索するらしいけど，理解できない
# いつかリベンジする

# ----------------- カテゴリ ------------------
#AtCoder #abc
#復習したい
#ACしてない
#ゲーム木
#最後から考える
#後ろから考える
#後ろから探索
#ミニマックス法
#ゲーム木探索
