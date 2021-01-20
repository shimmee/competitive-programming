# ABC032C − 列
# URL: https://atcoder.jp/contests/abc032/tasks/abc032_c
# 日付: 2020/12/07

# ---------- 思ったこと / 気づいたこと ----------
# 対数取って累積和取って二分探索!!!

# ------------------- 方針 --------------------
# 対数を取って積を和の形にしたい
# まず各要素の対数を取って，累積和を取る
# 要素iをループで回して，差を取ってlog(k)より小さくなる点を二分探索で探す

# ------------------- 解答 --------------------
code:python
    import math
    import itertools
    import bisect
    n, k = map(int, input().split())
    s = [int(input()) for _ in range(n)]

    if min(s) == 0:
        print(len(s))
        exit()
    if k == 0:
        print(0)
        exit()
    if min(s) > k:
        print(0)
        exit()

    k_log = math.log10(k)
    s_log = []
    for i in s:
        if i == 0:
            s_log.append(0)
        else:
            s_log.append(math.log10(i))
    #s_log = [math.log10(i) for i in s]
    s_log_cum = [0] + list(itertools.accumulate(s_log))

    ans = 0
    for i in range(n+1):
        index = bisect.bisect_left(s_log_cum, s_log_cum[i]-k_log)
        ans = max(ans, i-index+1)
    print(ans)

    # ----------------------------
    # logつかわないバージョン
    # ----------------------------

    n, k = map(int, input().split())
    s = [int(input()) for _ in range(n)]
    if min(s) == 0:
        print(len(s))
        exit()
    if k == 0:
        print(0)
        exit()
    if min(s) > k:
        print(0)
        exit()

    s_cum = [1]

    for i in range(n):
        s_cum.append(s_cum[i]*s[i])

    ans = 0
    for i in range(1, n+1):
        if s[i-1] > k: continue
        # 右がOKの二分探索
        ok = i
        ng = 0
        mid = i
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if s_cum[i] / s_cum[mid] <= k:  # 累積積がk以下
                ok = mid
            else:
                ng = mid
        ans = max(ans, i-mid)
    print(ans)

    # WAもTLEもある

    # ----------------------------
    # log使うバージョン
    # ----------------------------
    import itertools
    import math
    n, k = map(int, input().split())
    s = [int(input()) for _ in range(n)]
    if min(s) == 0:
        print(n)
        exit()
    if k == 0:
        print(0)
        exit()
    if min(s) > k:
        print(0)
        exit()

    k_log = math.log2(k)
    s_log = [math.log2(i) for i in s]
    s_log_cum = [0] + list(itertools.accumulate(s_log))

    ans = 0
    for i in range(1, n+1):
        if s_log[i - 1] > k_log: continue
        # 右がOKの二分探索
        ok = i
        ng = 0
        mid = 0
        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2
            if s_log_cum[i] - s_log_cum[mid] <= k_log:  # 累積積がk以下
                ok = mid
            else:
                ng = mid
        ans = max(ans, i-mid)
    print(ans)

    # この解法でケース1は綺麗に解けてる。途中経過も完璧。なのに半分くらいのケースでWA
    # 解説みたら別解に対数+累積和+二分探索があった
    # けど誤差に注意って書いてて，多分誤差でWAになってる
    # しゃくとり法が模範解答
    # 参考: https://nashidos.hatenablog.com/entry/2020/02/02/165319

    import itertools
    n, k = map(int, input().split())
    s = [int(input()) for _ in range(n)]
    if min(s) == 0: # 1つでも0が入っていれば全要素使っていい
        print(n)
        exit()
    else:
        right = 0
        prod = 1
        ans = 0
        for left in range(n): # 尺取法の左をループで回す
            while right < n and prod*s[right] <= k: # もしleftからrightまでの積がkより小さければ，rightを更に右に進める
                prod *= s[right] # prodを更新しても積がkより小さいので更新できる
                right += 1 # 右に進める
            ans = max(ans, right-left) # rightの移動が止まった時点で，そのleftにおけるrightが最大限右にいってる
            if left == right: # leftがrightに追いついたら，rightを右に進める
                right += 1
            else:
                prod //= s[left] # 次のループでleftが右に進むために，現在のleftの値をprodから割っておく (累積和で端っこ引くのと同じ)
    print(ans)


# ------------------ 入力例 -------------------
7 6
4
3
1
1
2
10
2

6 10
10
10
10
10
0
10


6 9
10
10
10
10
10
10

# ----------------- 解答時間 ------------------
# 1時間考えてgive up


# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc032
# 最初に思いついた対数+累積和+二分探索は別解にあったが，詳細がないし，誰も解答に載せてないから，どうしようもない
# しかたなく尺取法で解説AC
# ほかの尺取法のの問題解いてみたい


# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復讐したい
#しゃくとり法 #累積和