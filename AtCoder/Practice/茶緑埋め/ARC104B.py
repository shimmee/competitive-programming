# ARC104B - DNA Sequence
# URL: https://atcoder.jp/contests/arc104/tasks/arc104_b
# Date: 2021/02/04

# ---------- Ideas ----------
# 連続部分列
# AとT，CとGの出現回数が正で同じ場合にのみ相補的
# O(n^2)が回るので，iとjを動かしながら出現回数を溜め込みながら条件みたすかどうか確認する

# ------------------- Answer --------------------
#code:python
n, s = input().split()
n = int(n)

d = {'A':0, 'T':1, 'C':2, 'G':3} # 配列のインデックス
ans = 0
for i in range(n-1):
    cnt = [0,0,0,0] # A,T,C,Gの出現回数を初期化
    cnt[d[s[i]]] += 1 # s[i]の出現回数を1つインクリメント
    for j in range(i+1, n):
        cnt[d[s[j]]] += 1
        # (Aの出現回数 > 0 または Cの出現回数>0) かつ (AとTが同じ回数でかつCとGが同じ回数)
        if (cnt[0] > 0 or cnt[2] > 0) and (cnt[0] == cnt[1] and cnt[2] == cnt[3]):
            ans += 1
print(ans)


# ------------------ Sample Input -------------------
10 AAATACCGCG

# ----------------- Length of time ------------------
# 12分

# -------------- Editorial / my impression -------------
# https://atcoder.jp/contests/arc104/editorial
# けんちょんさんの解き方がかしこい: https://drken1215.hatenablog.com/entry/2020/10/05/120000
# 200点問題の最高峰AGC023A: Zero-Sum Rangesと同じ問題らしい

# ----------------- Category ------------------
#AtCoder
#アナグラム
#文字列問題
#nC2
#O(N^2)個のものを考える問題
#ARC-B 数え上げ問題
#茶diff
#連続部分列を扱う問題
