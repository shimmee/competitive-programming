# ARC040B - 直線塗り
# URL: https://atcoder.jp/contests/arc040/tasks/arc040_b
# Date: 2021/02/01

# ---------- Ideas ----------
# 区間スケジューリング？違うか
# 貪欲に解く
# 自分からrマス伸ばして，最後のdotに届くなら+1して終わり
# 自分がdotなら必ず塗って1マス進む
# 自分がoなら1マス進む

# ------------------- Answer --------------------
#code:python
n, r = map(int, input().split())
S = input()

# 最初から全部oなら0を出力して終わり
if all(i == 'o' for i in S): print(0); exit()

# 最後のdotマスのインデックス
k = max([i for i in range(n) if S[i] == '.'])

cnt = -1 # 行動のカウンター
for i in range(n):
    cnt += 1 # 右に移動するたびにインクリメント
    if i + r - 1 >= k: # 今の場所からkまで届くならそれで終わり
        cnt += 1
        break
    if S[i] == '.': # もし自分が白ならrマス分塗る
        cnt += 1
        S = S[:i] + 'o'*r + S[i+r:]
print(cnt)

map(int, input().split())
# ------------------ Sample Input -------------------
7 3
...o.o.

4 4
oooo


# ----------------- Length of time ------------------
# 22分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc040
# 結構バグった右に移動するたびにインクリメントするのを最後にelseとして書いてしまっていた
# つまり，打つ時は移動したのがカウントされてなかった。
# これに気づくのに時間がかかった
# 結構短く書けたほうだとおもう
# 最後のマスを確保しておくのがポイントだった


# ----------------- Category ------------------
#AtCoder
#貪欲
