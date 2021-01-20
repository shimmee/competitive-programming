# ABC164C - gacha
# URL: https://atcoder.jp/contests/abc164/tasks/abc164_c
# 日付: 2020/11/21

# ---------- 思ったこと / 気づいたこと ----------
# 単純にsetで重複削除すればよさそう


# ------------------- 解答 --------------------
#code:python
n = int(input())
s = []
for _ in range(n):
    s.append(input())
print(len(set(s)))

# ------------------ 入力例 -------------------
3
apple
orange
apple


5
grape
grape
grape
grape
grape

# ----------------- 解答時間 ------------------
# 2分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc164/editorial.pdf
# 簡単

# ----------------- カテゴリ ------------------
#AtCoder #abc-c
#ハッシュ
