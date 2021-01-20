# ABC026C - 高橋君の給料
# URL: https://atcoder.jp/contests/abc026/tasks/abc026_c
# 日付: 2020/12/22

# ---------- 思ったこと / 気づいたこと ----------
#

# ------------------- 方針 --------------------
# 各社員の部下の人数のリスト，部下の社員番号のリスト，各社員の給料の初期化したリストを作る
# 部下が居ない人の給料を埋める
# 部下が1人の人の給料を埋める
# 部下が2人以上の人の給料を埋める
# 部下が1人の人の給料を埋める
# 部下が2人以上の人の給料を埋める
# これを何回か繰り返すときっと埋まる...


# ------------------- 解答 --------------------
#code:python
n = int(input())
B = [int(input()) for _ in range(n-1)]

num_buka = [0]*n # インデックスの社員番号の人が持つ部下の人数
buka_id = [[] for _ in range(n)] # インデックスの社員番号の人が持つ部下の人数
for i in range(n-1):
    joshi = B[i]
    num_buka[joshi-1] += 1
    buka_id[joshi-1].append(i+1)

salary = [0]*n
for i in range(n):
    if num_buka[i] == 0:
        salary[i] = 1

def buka1():
    prev = []
    while prev != salary:
        prev = salary[:]
        for i in range(n):
            if num_buka[i] == 1:
                for buka in buka_id[i]:
                    if salary[buka] == 0:
                        continue
                    salary[i] = salary[buka] * 2 + 1
    return salary

def buka2():
    prev = []
    while prev != salary:
        prev = salary[:]
        for i in range(n):
            if num_buka[i] >= 2:
                buka_salary = []
                for buka in buka_id[i]:
                    buka_salary.append(salary[buka])
                if min(buka_salary) == 0:
                    continue
                else:
                    salary[i] = max(buka_salary) + min(buka_salary) + 1
    return salary

salary = buka1()
salary = buka2()
salary = buka1()
salary = buka2()
salary = buka1()

print(salary[0])



# ゴミクソコードなので，解説を参考に綺麗に書く
# わかりやすい解説: https://blog.reud.net/2019/08/21/post-744/
# 社員番号が大きい人(新入り)から順に求めていけばいいらしい
# 再帰関数で書く

n = int(input())
buka_id = [[] for _ in range(n)] # インデックスの社員番号の人が持つ部下のid
for i in range(n-1):
    b = int(input())
    buka_id[b-1].append(i+1)

def dfs(salary=[0]*n, id=0):
    # iは社員番号
    if buka_id[id] == []: # 部下が居ない人は
        salary[id] = 1 # 給料が1
        return salary
    temp = [] # idさんの部下の給料一覧
    for buka in buka_id[id]: # idさんの全ての部下
        if salary[buka] == 0: # もしまだ部下の給料が決まってなかったら，再帰で探しに行く
            salary = dfs(salary, buka)
        temp.append(salary[buka]) # 部下の給料をtempに保存
    if len(temp) == 1: # 部下が1人しかいないときは，部下の給料*2＋1
        salary[id] = temp[0]*2+1
    else: # 部下が複数いるときは，max+min+1
        salary[id] = max(temp) + min(temp) + 1
    return salary

print(dfs()[0])

# 自力で再帰書いた！
# 実はsalaryの引数いらないのではないのか？
n = int(input())
buka_id = [[] for _ in range(n)] # インデックスの社員番号の人が持つ部下のid
for i in range(n-1):
    b = int(input())
    buka_id[b-1].append(i+1)

def dfs(i): # 社員番号iさんの給料を出力する関数
    if buka_id[i] == []: # 部下が居ない人は給料が1
        return 1
    temp = [dfs(j) for j in buka_id[i]] # idさんの部下の給料一覧
    if len(temp) == 1: # 部下が1人しかいないときは，部下の給料*2＋1
        return temp[0]*2+1
    else: # 部下が複数いるときは，max+min+1
        return max(temp) + min(temp) + 1

print(dfs(0))



# 部下が1人のときと2人以上のときは，実は分ける必要はない: というのもmax(temp)+min(temp)=temp[0]*2になってるから

n = int(input())
buka_id = [[] for _ in range(n)] # インデックスの社員番号の人が持つ部下のid
for i in range(n-1):
    b = int(input())
    buka_id[b-1].append(i+1)

def dfs(i): # 社員番号iさんの給料を出力する関数
    if buka_id[i] == []: # 部下が居ない人は給料が1
        return 1
    temp = [dfs(j) for j in buka_id[i]] # idさんの部下の給料一覧
    return max(temp) + min(temp) + 1 # 部下が1人でも2人でもこの式でいける

print(dfs(0))

# きれいな再帰関数: https://atcoder.jp/contests/abc026/submissions/18800377



# ------------------ 入力例 -------------------
5
1
1
1
1

7
1
1
2
2
3
3

6
1
2
3
3
2


10
1
2
3
4
5
6
7
8
9

# ----------------- 解答時間 ------------------
# 25分

# -------------- 解説 / 感想 / 反省 -------------
# やばいコードを書いてしまった。
# 難しかった点は，部下の給料が決まらないと上司の給料も決まらない，という点，あと部下が1人のときと2人以上で給料体系が違う点
# 部下が1人の人の給料を決めてから，部下が2人の人の給料を決めたとしても，「部下が1人で，その部下には2人以上の部下がいる」人の給料は決定されない
# 深さ優先探索の再帰関数で超キレイにかけた。めっちゃ学びが大きい。

# ----------------- カテゴリ ------------------
#AtCoder #abc
#解説AC #復習したい
#再帰関数
#深さ優先探索
#DFS
