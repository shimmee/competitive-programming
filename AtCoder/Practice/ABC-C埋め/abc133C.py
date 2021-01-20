# ABC133C - Remainder Minimization 2019
# URL: https://atcoder.jp/contests/abc133/tasks/abc133_c
# 日付: 2020/11/25

# ---------- 思ったこと / 気づいたこと ----------
# あまりのパターンは2019通り

# ------------------- 方針 --------------------
# rとlの差が2019より大きい時，余り0が作れるので，答え0
# 差が2019以下の時，余りを全通り列挙して，min*(min+1)

# ------------------- 解答 --------------------
#code:python
l, r = map(int, input().split())
sa = r-l
if sa >= 2019:
    print(0)
else:
    amari = []
    for i in range(l, r+1):
        amari.append(i % 2019)
    amari.sort()
    print(amari[0]*amari[1] % 2019)

# 半分WAなのでどっちかのifがおかしい
# 差が2019より大きいときの処理がおそらくダメ: 誤読してる可能性
# amariをソートするとi<jという順番が崩れてる
# 愚直にi, jの2019パターンで全探索してみる
l, r = map(int, input().split())
sa = r-l
if sa > 2019:
    print(0)
else:
    amari = []
    for i in range(l, r+1):
        amari.append(i % 2019)
    ans = 10**10
    for i in range(len(amari)):
        for j in range(i+1, len(amari)):
            ans = min(ans, (amari[i]*amari[j])%2019)
    print(ans)

# 1ケースだけWA
# ------------------ 入力例 -------------------
0 2000000000

2000 2018

2000 2100

2020 2040

4 5

# ----------------- 解答時間 ------------------
# 30分

# -------------- 解説 / 感想 / 反省 -------------
# サンプルケースが条件分岐の1つのパターンしかなかったので，WAが回避できなかった
# https://img.atcoder.jp/abc133/editorial.pdf
# 解説みてミスに気づいた。ソートしたらi<jの順番が崩れるので，ちゃんと全探索する必要があった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#mod
