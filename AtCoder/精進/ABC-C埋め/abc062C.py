# ABC062C - Chocolate Bar
# URL: https://atcoder.jp/contests/arc074/tasks/arc074_a
# 日付: 2020/11/30

# ---------- 思ったこと / 気づいたこと ----------
# 2回切る家，少なくとも1回はhかwの橋から橋まで切るので，選び方はH+W
# 1回目の切り方を選んで面積をs1とする。
# 次に残った長方形を切るが，できれば半分に切りたい。
# マスの数が偶数であれば半分にできる: s2 = s3 = 残りの半分
# マスの数が奇数であれば，「縦にきったときのs2とs3の差」v.s.  「横に切った時のs2とs3の差」で小さい方を採用


# ------------------- 解答 --------------------
#code:python
H, W = map(int, input().split())

ans = 10**10
# 1回目縦に切る (Wの方向)
for i in range(1, W):
    s1 = i*H # 最初の長方形の面積

    # 残りの辺の長さ
    h = H
    w = W-i

    # 2回めの切り方
    if h*w % 2 == 0: # 面積が偶数なら半分に割る
        s2 = h * w // 2
        s3 = h * w // 2
    else: # 面積が奇数なら
        # 縦に切る
        s2_tate = int(w/2)*h
        s3_tate = (w - int(w/2))*h

        # 横にきる
        s2_yoko = int(h / 2)*w
        s3_yoko = (h - int(h / 2)) * w

        if abs(s2_tate-s3_tate) > abs(s2_yoko-s3_yoko):
            s2 = s2_yoko
            s3 = s3_yoko
        else:
            s2 = s2_tate
            s3 = s3_tate

    s_max = max(s1, s2, s3)
    s_min = min(s1, s2, s3)
    ans = min(ans, s_max-s_min)

# 1回目横に切る (Hの方向)
for i in range(1, H):
    s1 = i * W  # 最初の長方形の面積

    # 残りの辺の長さ
    h = H - i
    w = W
    if h * w % 2 == 0:  # 面積が偶数なら半分に割る
        s2 = h * w // 2
        s3 = h * w // 2
    else:  # 面積が奇数なら
        # 縦に切る
        s2_tate = int(w / 2) * h
        s3_tate = (w - int(w / 2)) * h

        # 横にきる
        s2_yoko = int(h / 2) * w
        s3_yoko = (h - int(h / 2)) * w

        if abs(s2_tate - s3_tate) > abs(s2_yoko - s3_yoko):
            s2 = s2_yoko
            s3 = s3_yoko
        else:
            s2 = s2_tate
            s3 = s3_tate

    s_max = max(s1, s2, s3)
    s_min = min(s1, s2, s3)
    ans = min(ans, s_max - s_min)

print(ans)


# ------------------ 入力例 -------------------
3 5

4 5

# ----------------- 解答時間 ------------------
# 15分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/arc074/editorial.pdf
# 解説通りといたけど，他の人のpypy解答みたら自分のほうが圧倒的に長い
# これ水色diffだけど，今の水色より昔の水色問題のほうが簡単っぽい。

# ----------------- カテゴリ ------------------
#AtCoder #abc
#O(HW)をO(H+W)にする