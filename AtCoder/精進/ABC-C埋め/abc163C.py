# ABC165C - many requirements
# URL: https://atcoder.jp/contests/abc165/tasks/abc165_c
# 日付: 2020/11/22

# ---------- 思ったこと / 気づいたこと ----------
# dでソートして高い点の方からピックアップ？
# DPの臭いもする

# ------------------- 方針 --------------------
# 解答見た: 組み合わせ全探索？みたいな感じ
# ありうる数列を深さ優先探索で決めて，数列が決まったらq個の式を見てスコアを測る
# from itertools import combinations_with_replacementってのがあった。すごい

# ------------------- 解答 --------------------
#code:python
from itertools import combinations_with_replacement
n,m,q = map(int, input().split())
abcd = [[int(i) for i in input().split()] for _ in range(q)]
pattern = list(combinations_with_replacement([i for i in range(1, m+1)], n))

ans = 0
for p in pattern:
    temp_ans = 0
    for a,b,c,d in abcd:
        a -= 1
        b -= 1
        if p[b]-p[a] == c:
            temp_ans += d
    ans = max(ans, temp_ans)
print(ans)




# ------------------ 入力例 -------------------
3 4 3
1 3 3 100
1 2 2 10
2 3 2 10


4 6 10
2 4 1 86568
1 4 0 90629
2 3 0 90310
3 4 1 29211
3 4 3 78537
3 4 2 8580
1 2 1 96263
1 4 2 2156
1 2 0 94325
1 4 3 94328
# ----------------- 解答時間 ------------------
# 1時間以上かかってわからんかった

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc165/editorial.pdf
# そもそも全ての数列の列挙の方法で間に合うと思わなかったし，列挙の仕方もわからなかった。
# combinations_with_replacementこんなのあるとはびっくりした
# https://docs.python.org/2/library/itertools.html

# ----------------- カテゴリ ------------------
#AtCoder #abc
#全探索 #itertools
#combinations_with_replacement


# ゴミ
# n,m,q = map(int, input().split())
# abcd = [[int(i) for i in input().split()] for _ in range(q)]
# abcd = sorted(abcd, key=lambda x: x[3],  reverse=True)
#
# tab = [[-1]*n for _ in range(n)]
#
# for i in range(q):
#     a,b,c,d = abcd[i]
#     if tab[a-1][b-1] == -1:
#         tab[a-1][b-1] = c
