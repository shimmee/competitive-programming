# ABC171 C - One Quadrillion and One Dalmatians
# URL: https://atcoder.jp/contests/abc171/tasks/abc171_c
# 日付: 2020/11/21

# ---------- 思ったこと / 気づいたこと ----------
# 26進法でいけるやん

# ------------------- 方針 --------------------
# 関数パクってくるだけ: https://tanuhack.com/num2alpha-alpha2num/

# ------------------- 解答 --------------------
#code:python
# これでいける: https://tanuhack.com/num2alpha-alpha2num/
def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)

n = int(input())
print(num2alpha(n).lower())

# ------------------ 入力例 -------------------
2

27

1

123456789

# ----------------- 解答時間 ------------------
# 2分くらい

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc171/editorial.pdf
# 関数の中身はよくわかってない

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#26進法
#アルファベット