# ABC076C - Dubious Document 2
# URL: https://atcoder.jp/contests/abc076/tasks/abc076_c
# 日付: 2020/12/09

# ---------- 思ったこと / 気づいたこと ----------
# SとTが小さいから全探索できる

# ------------------- 方針 --------------------
# Tの文字数をmとする
# Sからループで順にm文字分取ってきて，Tに一致するかどうか調べる
# 一致してなくても，?だったら一致してることにする
# m文字分が完全に一致してる(flag = True)の場合には，Sのその箇所をTに書き換えて，candidateとして保存する
# 最後にcandidateの?を全てaに置き換えて，辞書順に並べて，一番速いやつを出力

# ------------------- 解答 --------------------
#code:python
S = input()
T = input()
m = len(T)

candidate = []
for i in range(len(S)-m+1):
    s = S[i:i+m] # Sのi番目からm文字分の部分文字列
    flag = True
    for j in range(m):
        if not(s[j] == T[j] or s[j] == '?'):
            flag = False
    if flag:
        S_ = S[:]
        for j in range(m):
            S_ = S_[:i+j] + T[j] + S[i+j+1:]
        candidate.append(S_)

if candidate == []:
    print('UNRESTORABLE')
else:
    candidate = [s.replace('?', 'a') for s in candidate]
    candidate.sort()
    print(candidate[0])

# ------------------ 入力例 -------------------
?tc????
coder

??p??d??
abc


# ----------------- 解答時間 ------------------
# 21分AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc076/editorial.pdf
# 小難しく解説書いてるけど，やってることは一緒

# ----------------- カテゴリ ------------------
#AtCoder #abc
#文字列
#一致する箇所を探す
