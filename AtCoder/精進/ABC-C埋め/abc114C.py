# ABC114C - 755
# URL: https://atcoder.jp/contests/abc114/tasks/abc114_c
# 日付: 2020/11/29


# ------------------- 方針 --------------------
# 文字列のリスト[3,5,7]のそれぞれの要素に[3,5,7]をくっつけるというループを9桁に至るまで続ける
# 重複したものをsetで除く
# 3と5と7を全て含む文字列だけ残す
# 入力より小さい753数の個数を出力する

# ------------------- 解答 --------------------
#code:python
l = ['3', '5', '7']
while True:
    if len(l[-1]) == 9: break
    l_ = l[:]
    for i in l_:
        l.append(i + '3')
        l.append(i + '5')
        l.append(i + '7')
l = set(l)
l753 = []
for i in l:
    if ('3' in i) and ('5' in i) and ('7' in i):
        l753.append(int(i))

n = int(input())
ans = 0
for i in l753:
    if i <= n:
        ans += 1
print(ans)


# AC!
# 解説みると，深さ優先探索で再帰してる: https://img.atcoder.jp/abc114/editorial.pdf
N = int(input())
def dfs(s): # 文字列 s で始まる七五三数の個数
    if int(s) > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0 # s 自体が七五三数なら +1
    for c in '753':
        ret += dfs(s + c)
    return ret

print(dfs('0'))
# ------------------ 入力例 -------------------
575

3600

# ----------------- 解答時間 ------------------
# 16分AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/abc114/editorial.pdf
# 解説の書き方が簡潔すぎてビビる: 特にifとかallの使い方

# ----------------- カテゴリ ------------------
#AtCoder #abc
#再帰
#文字列
