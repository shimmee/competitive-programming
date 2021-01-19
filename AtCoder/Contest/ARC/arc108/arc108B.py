# ARC108-B :
# URL:
# 日付: 2020年11月21日

# ---------- 思ったこと / 気づいたこと ----------
# 解の公式

# ------------------- 方針 --------------------
#

# ------------------- 解答 --------------------
#code:python
n = int(input())
s = input()

while True:
    new = s.replace('fox', '')
    if len(new) == len(s):
        break
    s = new
print(len(new))



n = int(input())
s = input()
s = [i for i in s]


r = []
fox = 0
for i in range(n):
    r.append(s[i])

    if r[-3:] == ['f', 'o', 'x']:
        r.pop()
        r.pop()
        r.pop()
print(len(r))








# ------------------ 入力例 -------------------
6
icefox

7
firebox


48
ffoxoxuvgjyzmehmopfohrupffoxoxfofofoxffoxoxejffo


# ----------------- 解答時間 ------------------
#

# -------------- 解説 / 感想 / 反省 -------------
#

# ----------------- カテゴリ ------------------
#AtCoder #arc
#知ってるアルゴリズムだった
#知らないアルゴリズムだった
#非自明な論証が含まれていた