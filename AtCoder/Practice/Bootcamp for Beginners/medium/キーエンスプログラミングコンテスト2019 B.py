# キーエンスプログラミングコンテスト2019 B - KEYENCE String
# URL: https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b
# 日付: 2020/12/25


# ------------------- 方針 --------------------
# Because of |S|<=100, it's easy to conduct full search
# 取り除く部分文字列の文字数と，部分文字列を取り除き始めるインデックスをそれぞれループで回す

# ------------------- 解答 --------------------
#code:python
S = input()
n = len(S)

# Sの部分文字列を1度だけ取り除いてkeyenceにしたい
# Sのうち，j番目からとj+i番目までの文字を取り除く
for i in range(n-7+1): # 取り除く文字数
    for j in range(n-i): # 取り除く部分文字列が始まるインデックス
        s = S[0:j] + S[j+i:] # 前半(jまで) + 後半(j+i以降)
        if s == 'keyence':
            print('YES')
            exit()
print('NO')

# ------------------ 入力例 -------------------
keyaence

keyofscience

mpyszsbznf

keyence

# ----------------- 解答時間 ------------------
# 20分

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/keyence2019/editorial.pdf
# 1箇所だけ取り除く，という文言に気づかず，WA出しまくった

# ----------------- カテゴリ ------------------
#部分文字列を取り除く
#復習したい

