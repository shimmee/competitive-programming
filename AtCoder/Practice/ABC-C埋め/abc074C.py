# ABC074C - Sugar Water
# URL: https://atcoder.jp/contests/abc074/tasks/arc083_a
# 日付: 2020/12/09

# ---------- 思ったこと / 気づいたこと ----------
# 全探索!!

# ------------------- 方針 --------------------
# A,B,C,Dを行う回数をそれぞれa,b,c,dとしてループを回す
# aを回せる回数は，Aを最大限にFまで入れる分なので，(F//A+1)回
# bを回せる回数は，a回のあとなので，F - (F//A+1)回
# cとdも同様
# ループ内でa,b,c,dが決まったら，水の量xと砂糖の量yを計算する
# x, yのあたいが濃度の条件Eと総量の条件Fを満たすか調べて，
# 満たせば更新: objに最大の濃度を保存する


# ------------------- 解答 --------------------
#code:python
A,B,C,D,E,F = map(int, input().split())
A = A*100
B = B*100

water = 0
sugar = 0
obj = 0
for a in range(F // A + 1):
    rest = F - A*a
    for b in range(rest // B + 1):
        rest = F - B * b
        for c in range(rest // C + 1):
            rest = rest - C * c
            for d in range(rest // D + 1):
                x = A*a + B*b
                y = C*c+D*d
                if x + y != 0: # 分母は0じゃだめ
                    if x+y <= F and (y/(x+y)) <= E/(100+E):
                        if obj <= y/(x+y):
                            obj = y/(x+y)
                            water = x
                            sugar = y

print(water+sugar, sugar)


# ------------------ 入力例 -------------------
1 2 10 20 15 200

1 2 1 2 100 1000

17 19 22 26 55 2802


# ----------------- 解答時間 ------------------
# 33分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc083/editorial.pdf
# 解説通りに溶けた
# 全探索に気づくまでに時間がかかった: 紙に色々書き出してからわかった
# ループの中の条件を書くのに色々必要だったから，紙に書いてよかった

# ----------------- カテゴリ ------------------
#AtCoder #abc
#全探索
