# ARC019B - こだわりの名前
# URL: https://atcoder.jp/contests/arc019/tasks/arc019_2
# Date: 2021/04/15

# ---------- Ideas ----------
# SとSを反転したものを比較して，異なるインデックスの数(cnt)を数えて場合分け
# 1文字: どうやっても回文になる
# cntが0: もともと回文-> 偶数文字ならどこ変えても回分じゃなくなる, 奇数文字なら真ん中は変えても意味なくてそれ以外変えて必ず回文になる
# cntが2: 1文字変えれば回文になる (ARCなど) -> 2箇所は24文字，それ以外は25文字のポテンシャル
# それ以外: どう変えても回分じゃない


# ------------------- Answer --------------------
#code:python
S = input()
S_rev = S[::-1]
n = len(S)
cnt = 0 # 反転して一致してない個数
for i in range(n):
    if S[i] != S_rev[i]:
        cnt += 1

if n == 1:
    print(0)
elif cnt == 0 and n % 2 == 0: # 完全な回文で偶数文字: どこを変えても回分じゃなくなる
    print(n*25)
elif cnt == 0 and n % 2 == 1: # 完全な回文で奇数文字: 真ん中は変えても回文
    print((n-1) * 25)
elif cnt == 2:
    print((n-2)*25 + 2*24)
else:
    print(n*25)



# ------------------ Sample Input -------------------
ARC

NOLEMONNOMELON


# ----------------- Length of time ------------------
# 6分

# -------------- Editorial / my impression -------------
# https://www.slideshare.net/chokudai/arc019
# 回文問題すきになってきた

# ----------------- Category ------------------
#AtCoder
#回文判定
#回文は元の文字列を反転して判定
#偶奇に注目
#場合分け