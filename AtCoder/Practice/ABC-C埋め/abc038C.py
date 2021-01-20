# ABC038C - 単調増加
# URL: https://atcoder.jp/contests/abc038/tasks/abc038_c
# 日付: 2020/12/08

# ---------- 思ったこと / 気づいたこと ----------
# 尺取法: O(N)で解く

# ------------------- 方針 --------------------
# leftをループで動かす
# あるleftに対してrightを行けるところまで行く
# パターン1: leftごとにrightをleftに戻す O(N^2)
# パターン2: leftが右に行ってもrightの位置はそのままで，rightに追いつくまでleftを動かす

# ------------------- 解答 --------------------
#code:python
# パターン1: leftごとにrightをleftに戻す O(N^2)
n = int(input())
a = list(map(int, input().split()))

ans = 0
for left in range(n):  # 尺取法の左側をループで回す
    right = left # 毎回rightを左からやり直す
    ans += 1
    while right < n - 1 and a[right] < a[right + 1]:  # rightがまだ右に行けて，かつ1つ右側の数が現在のrightの数より大きければrightを右に進める
        ans += 1
        right += 1  # 右に進める
    if left == right:  # leftがrightに追いついたら，rightを右に進める
        right += 1
print(ans)

# 毎回rightを左からやり直してるせいでTLE
# rightの位置を変えずにうまくカウントする必要がある

# パターン2: leftが右に行ってもrightの位置はそのままで，rightに追いつくまでleftを動かす
n = int(input())
a = list(map(int, input().split()))

right = 0
ans = 0
i = 0
for left in range(n):  # 尺取法の左をループで回す
    ans += 1 # 左が動くときは必ず単調増加になってるのでインクリメント
    while right < n-1 and a[right] < a[right+1]:  # rightがまだ右に行けて，かつ1つ右側の数が現在のrightの数より大きければrightを右に進める
        ans += 1 # 右に行けるのでインクリメント
        right += 1  # 右に進める
        i = left # whileが回ってるleftをiに保存
    if left == i: # leftがiに等しいとき，つまりwhileのループが終わった直後のみ，rightとleftの間の子達のカウントをしてあげる
        m = (right-left-1)
        ans += m*(m+1)//2 #
    if left == right:  # leftがrightに追いついたら，rightを右に進める
        right += 1
print(ans)

# これでAC


# 解説: https://img.atcoder.jp/data/abc/038/editorial.pdf
# whileで右の最大を探して，answer:=answer+(r-l+1)
n = int(input())
a = list(map(int, input().split()))

right = 0
ans = 0
for left in range(n):  # 尺取法の左をループで回す
    while right < n-1 and a[right] < a[right+1]:  # rightがまだ右に行けて，かつ1つ右側の数が現在のrightの数より大きければrightを右に進める
        right += 1
        # このwhileが終わった時点で，rightは現在のleftに対して最大のrightになってる
    ans += right-left+1
    if left == right:  # leftがrightに追いついたら，rightを右に進める
        right += 1
print(ans)


# 尺取法とは
# leftをループで動かす。
# あるleftに対して，rightを行ける所まで右に動かす
# leftを各ループでrightに追いつくまで動かす
# leftがrightに追いついたらrightを+1して両方すすめる


# ------------------ 入力例 -------------------
5
1 2 3 2 1

4
1 2 3 4

6
3 3 4 1 2 2

6
1 5 2 3 4 2


# ----------------- 解答時間 ------------------
# 36分AC

# -------------- 解説 / 感想 / 反省 -------------
# https://img.atcoder.jp/data/abc/038/editorial.pdf
# あるleftに対してwhileでrightが一番右まで到達したあとの処理が，自分のと解説で異なった
# 解説はそのあと普通にleftを右にループで順に動かしながらansにright-left+1をインクリメント
# 自分はそもそも各ループが回るたびにansにインクリメントしてたので，階差を処理した
# 解説の方が賢い
# 解説はlに対するrを探して固定してる
# 自分はrを探してlを固定してる感じ

# ----------------- カテゴリ ------------------
#AtCoder #abc
#尺取法
