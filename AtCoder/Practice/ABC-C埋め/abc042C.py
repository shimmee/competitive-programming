# ABC042C - こだわり者いろはちゃん
# URL: https://atcoder.jp/contests/abc042/tasks/arc058_a
# 日付: 2020/12/21


# ------------------- 方針 --------------------
# N<=10000なので全探索できる
# iを0から100000まで回して，嫌いな文字が含まれてなかったら，支払金額より多かったら出力

# ------------------- 解答 --------------------
#code:python
n, k = map(int, input().split())
D = list(map(int, input().split()))

ans = 100000
for i in range(100000):
    flag = True
    for d in D:
        if str(d) in str(i): # もし金額に嫌いな文字が入ってたら
            flag = False
    if flag and i >= n: # 嫌いな文字がなくて，かつ支払金額より高かったらOK
        ans = min(ans, i)
print(ans)


# ------------------ 入力例 -------------------
1000 8
1 3 4 5 6 7 8 9

9999 1
0

# ----------------- 解答時間 ------------------
# 3分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/arc/058/editorial.pdf
# 緑diffを3分で解けた！

# ----------------- カテゴリ ------------------
#AtCoder #abc

