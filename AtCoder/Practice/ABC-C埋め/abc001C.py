# ABC001C - 風力観測
# URL: https://atcoder.jp/contests/abc001/tasks/abc001_3
# 日付: 2020/12/18

# ---------- 思ったこと / 気づいたこと ----------
# 細かな処理が大変そう

# ------------------- 方針 --------------------
#

# ------------------- 解答 --------------------
#code:python
def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p
round
dire = []
a = 0
b = 11.25
for i in range(16):
    dire.append([a, b])
    a, b = b, b+22.5
dire.append([348.75, 360])
dire_name = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']

l = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6]

speed = []
a = 0
for i in range(len(l)):
    speed.append([a, l[i]])
    a = my_round(l[i] + 0.1, 1)
speed.append([32.7, 10**10])
speed_name = [i for i in range(13)]



deg, dis = map(int, input().split())

for i in range(len(dire)):
    if dire[i][0] <= deg/10 < dire[i][1]:
        ans_dir = dire_name[i]

for i in range(len(speed)):
    if speed[i][0] <= my_round(dis/60, 1) <= speed[i][1]:
        ans_wind = speed_name[i]

if ans_wind == 0:
    print('C', 0)
else:
    print(ans_dir, ans_wind)

# ------------------ 入力例 -------------------
2750 628

161 8


3263 15

# ----------------- 解答時間 ------------------
# 25分

# -------------- 解説 / 感想 / 反省 -------------
# https://www.slideshare.net/chokudai/abc001
# 浮動点小数の処理次第でWAが出る問題
# いい感じに四捨五入してくれる関数が必要だが，pythonのデフォルトのroundは一番近い偶数にまるめてくれるだけ。
# アホみたいに長くなった


# ----------------- カテゴリ ------------------
#AtCoder #abc
#浮動点小数
