# AGC031A - Colorful Subsequence
# Bootcamp For Beginners - Medium
# URL: https://atcoder.jp/contests/agc031/tasks/agc031_a
# Date: 2021/01/06

# ---------- Ideas ----------
# しゃくとり法？
# 尺取法

# ------------------- Solution --------------------
#
# 尺取法とは
# leftからrightまでの区間で関心のあるものを溜め込むリストorセットを作る
# leftをループで動かす。
# あるleftに対して，rightを行ける所まで右に動かす
# leftを各ループでrightに追いつくまで動かす
# leftがrightに追いついたらrightを+1して両方すすめる
# leftがrightに追いついてないなら，溜め込むリストからleftの分を除く

# 各伸ばしで最長になった時点で，インクリメント


# ------------------- Answer --------------------
#code:python
mod = 10**9+7
n = int(input())
S = input()

right = 0
ans = 0
# leftからrightまでの区間で関心のあるものを溜め込むリストorセットを作る
seen = set([S[0]])  # 出現したアルファベットを保存する集合
for left in range(n):  # leftをループで動かす。

    # あるleftに対して，rightを行ける所まで右に動かす
    while right < n - 1 and (not S[right + 1] in seen):  # 次のアルファベットがテーブルに入ってなければ追加
        seen.add(S[right + 1])  # 次のアルファベットを入れる
        right += 1  # 右にすすめる

    # 各伸ばしで最長になった時点で，インクリメント
    ans += len(seen)

    if left == right:  # leftがrightに追いついたらrightを+1して両方すすめる
        right += 1
    else:  # leftがrightに追いついてないなら，溜め込むリストからleftの分を除く
        seen.remove(S[left])

print(ans % mod)

# 連続部分列じゃありませんでした！！！
# 連続部分列であれば，おそらくこれで正解でした！！
# 11:05-11:35分


# 部分列なので，歯抜けで取っていい
# 2021/01/07やりなおし，9:17-
import string
alpha = list(string.ascii_lowercase)
alpha2num = lambda c: ord(c) - ord('a')

mod = 10**9+7
n = int(input())
S = input()

alpha_idx = [[] for _ in range(26)] # 各アルファベットが出現したインデックス
for i in range(n):
    num = alpha2num(S[i])
    alpha_idx[num].append(i)

ans = 0
for i in range(n):
    num = alpha2num(S[i])
    cnt = 0
    for j in range(26):
        if j != num and alpha_idx[j] > i:
            cnt += 1
    ans += cnt
print(ans)

9:47 give up

# 嘘解法1: 各アルファベットが最後に出現したインデックス -> abbだとabが1カウントになっちゃう
# 嘘解法2: 各アルファベットが出現したインデックスから，あるi以降に各アルファベットが出現した回数 -> abbcのときにacbが作れるかどうか不明


# 2021/01/10 リベンジ
# なにか事前計算やら事前の処理が必要でありそう
# 後ろから見てみるとか？
# 全事象から重複を含む文字の通りだけ引くとか? 全通りは2**n通りある
# ギブアップです

# 解説: https://img.atcoder.jp/agc031/editorial.pdf
# あるアルファベットの出現回数がk回だとすると，そのアルファベットの選択肢はk+1になる (選ばない選択肢もある)
# これを全てのアルファベットについてかけ合わせて，最後に1を引く (何も選ばない文)
mod = 10**9+7
n = int(input())
S = input()

from collections import Counter
ans = 1
for key, value in Counter(S).items():
    ans = (ans * (value+1)) % mod
print((ans-1) % mod)

# ------------------ Sample Input -------------------
4
abcd


3
baa


5
abcab


# ----------------- Length of time ------------------
# 3日かけて解説AC

# -------------- Editorial / my impression -------------
# https://img.atcoder.jp/agc031/editorial.pdf
# けんちょんさんによると，こんな感じで文字を区別しない問題の方が簡単らしい: https://drken1215.hatenablog.com/entry/2019/03/18/125300
# この問題がBootcamp for beginners - mediumの問題で最後まで残った。
# 一番難しかったかもしれない

# ----------------- Category ------------------
#AtCoder
#BootcampForBeginners-medium
#AC_with_editorial #解説AC
#wanna_review #medium復習
#復習したい
#数え上げ問題
#文字列問題