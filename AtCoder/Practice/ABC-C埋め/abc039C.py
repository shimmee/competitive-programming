# ABC039C - ピアニスト高橋君
# URL: https://atcoder.jp/contests/abc039/tasks/abc039_c
# 日付: 2020/12/08

# ---------- 思ったこと / 気づいたこと ----------
# 白2回連続はミ/ファ と シ/ド

# ------------------- 方針 --------------------
# ミorシの場所を特定して，上手いことずらす

# ------------------- 解答 --------------------
#code:python
s = input()
for i in range(len(s) - 1):
    if s[i] == 'W' and s[i + 1] == 'W':
        pos = i  # このiは'Mi'に対応する

        # iから+7と+8がWならそれはシ・ドを表すので，現在i=Miになる
        if i+8 <= 20:
            if (s[i+7] == 'W' and s[i+8] == 'W'):
                now = 'Mi'
            else:
                now = 'Si'
            break
        elif 0 <= i - 5:
            if (s[i - 4] == 'W' and s[i - 5] == 'W'):
                now = 'Mi'
            else:
                now = 'Si'
            break

Mi = ['Fa', 'Fa', 'So', 'So', 'La', 'La', 'Si', 'Do', 'Do', 'Re', 'Re', 'Mi']
Si = ['Do', 'Do', 'Re', 'Re', 'Mi', 'Fa', 'Fa', 'So', 'So', 'La', 'La', 'Si']

if now == 'Mi':
    print(Mi[-(i + 1)])
else:
    print(Si[-(i + 1)])

# ------------------ 入力例 -------------------
WBWBWWBWBWBWWBWBWWBW


# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/abc/039/editorial.pdf
# 解説見たらWBWBWWを探索してドを探してた。こっちのほうが綺麗かも

# ----------------- カテゴリ ------------------
#AtCoder #abc
#文字列
