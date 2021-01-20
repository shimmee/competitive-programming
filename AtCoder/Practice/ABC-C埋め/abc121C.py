# ABC121C - Energy Drink Collector
# URL: https://atcoder.jp/contests/abc121/tasks/abc121_c
# 日付: 2020/11/28

# ------------------- 方針 --------------------
# 安い店から順に買う，貪欲に買う

# ------------------- 解答 --------------------
#code:python
n,m=map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(n)]
ab.sort()
need = m
ans = 0
i = 0
for i in range(n):
    if need == 0:
        break
    else :
        buy = min(need, ab[i][1]) # i本目を買う本数
        need -= buy
        ans += buy*ab[i][0] # i本目を買う総額
        i += 1
print(ans)


# ------------------ 入力例 -------------------
2 5
4 9
2 4

1 100000
1000000000 100000

# ----------------- 解答時間 ------------------
# 9分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc121/editorial.pdf
# 簡単〜

# ----------------- カテゴリ ------------------
#AtCoder #abc
#ソートして貪欲
