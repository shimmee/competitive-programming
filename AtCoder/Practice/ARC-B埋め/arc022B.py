# ARC022B - 細長いお菓子
# URL: https://atcoder.jp/contests/arc022/tasks/arc022_2
# 日付: 2020/12/08

# ---------- 思ったこと / 気づいたこと ----------
# 尺取法

# ------------------- 方針 --------------------
# 尺取法とは
# leftからrightまでの区間で関心のあるものを溜め込むリストorセットを作る
# leftをループで動かす。
# あるleftに対して，rightを行ける所まで右に動かす
# leftを各ループでrightに追いつくまで動かす
# leftがrightに追いついたらrightを+1して両方すすめる
# leftがrightに追いついてないなら，溜め込むリストからleftの分を除く

# ------------------- 解答 --------------------
#code:python
n = int(input())
a = list(map(int, input().split()))

right = 0
ans = 0
# leftからrightまでの区間で関心のあるものを溜め込むリストorセットを作る
sweet = set([a[0]]) # お菓子の種類を保存するハッシュテーブル
for left in range(n): # leftをループで動かす。

    # あるleftに対して，rightを行ける所まで右に動かす
    while right < n - 1 and (not a[right + 1] in sweet): # 次のお菓子がテーブルに入ってなければ追加
        sweet.add(a[right + 1]) # 次のお菓子を入れる
        right += 1 #
    ans = max(ans, right-left+1)

    if left == right: # leftがrightに追いついたらrightを+1して両方すすめる
        right += 1
    else: # leftがrightに追いついてないなら，溜め込むリストからleftの分を除く
        sweet.remove(a[left])
print(ans)

# ------------------ 入力例 -------------------
7
1 2 1 3 1 4 4

1
100

# ----------------- 解答時間 ------------------
# 8分

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/arc022
# 水色diffなのに8分で解けた
# 尺取法になれた！結構好きなアルゴリズム
# バグらないから好き

# ----------------- カテゴリ ------------------
#AtCoder #arc
#尺取法
