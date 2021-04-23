# 天下一プログラマーコンテスト2015予選B B - 天下一リテラル
# URL: https://atcoder.jp/contests/tenka1-2015-qualb/tasks/tenka1_2015_qualB_b
# Date: 2021/04/21

# ---------- Ideas ----------
# カッコ列と同じ要領で，ポインタを持って{と}で増減していく
# ポインタの値が1のときにコロンがきたら必ず辞書なので確定

# ------------------- Answer --------------------
#code:python
s = input()
if s == '{}': print('dict'); exit()
n = len(s)
cnt = 0
for i in range(n):
    if cnt == 1 and s[i] == ':':
        print('dict')
        exit()
    if s[i] == '{': cnt += 1
    if s[i] == '}': cnt -= 1
print('set')

# ------------------ Sample Input -------------------
{1:2}
{1,2}
{}

# ----------------- Length of time ------------------
# 10分

# -------------- Editorial / my impression -------------
# 解説なかった
# 最初，cnt==1のときにカンマならsetって出力してたらWAが10とれなくて，その方法はやめた
# ひらめき問題だった

# ----------------- Category ------------------
#AtCoder
#カッコ列
#水色diff
#ポインター