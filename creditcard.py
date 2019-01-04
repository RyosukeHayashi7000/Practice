"""
クレジットカード番号は16桁の番号で表すことができますが、この番号は以下の性質を持っています。

一番右の桁を1桁目として、

・偶数桁の数字をそれぞれ2倍し総和をとったものをeven
（ただし、2倍したあと2桁の数字になるものは、1の位と10の位の数を足して1桁の数字にしたあと、総和をとる）
・奇数桁の数字の総和をとったものをodd
とすると、even + odd は10 で必ず割り切れます。

1桁目がX と書かれた16桁の番号が複数与えられるので、それぞれに対し、上記性質をみたすようにX に入る数字を求めてください。

入力例
4
628381026148991X
511070105176715X
273492510450813X
670891979616350X

出力例
5
9
7
2
"""

import re

input_lines = int(input())
credit_num_list = [input() for _ in range(input_lines)]
k_num_list = []
g_num_list = []

"""
・奇数番目のリスト
k_num_list = ['2312189X', '1000161X', '7421401X', '7817665X']
・偶数番目のリスト
g_num_list = ['68806491', '51715775', '23950583', '60999130']
"""

for i in credit_num_list:
    g_num_list.append((i[0::2]))
    k_num_list.append((i[1::2]))

"""
・奇数番目の数字を分割したリスト
k_list2 = [['2', '3', '1', '2', '1', '8', '9', 'X'], ['1', '0', '0', '0', '1', '6', '1', 'X'], 
          ['7', '4', '2', '1', '4', '0', '1', 'X'], ['7', '8', '1', '7', '6', '6', '5', 'X']]

・xを抜いたリスト          
f_list = [[2, 3, 1, 2, 1, 8, 9], [1, 0, 0, 0, 1, 6, 1], [7, 4, 2, 1, 4, 0, 1], [7, 8, 1, 7, 6, 6, 5]]
"""

k_list2 = []
for k in k_num_list:
    k_list2.append(list(k))

f_list = []
for f in k_list2:
    f.pop(-1)
    f_list.append(list(map(int, f)))


"""
・xを抜いた数字の総和のリスト
odd_sum_list = [26, 9, 19, 40]
"""
odd_sum_list = [sum(u) for u in f_list]


"""
・偶数番目のリスト
g_list2 = [[6, 8, 8, 0, 6, 4, 9, 1], [5, 1, 7, 1, 5, 7, 7, 5], [2, 3, 9, 5, 0, 5, 8, 3], [6, 0, 9, 9, 9, 1, 3, 0]]
"""
g_list2 = []
for g in g_num_list:
    g_list2.append(list(map(int, g)))

"""
・偶数桁の数字をそれぞれ2倍
t_list = [12, 16, 16, 0, 12, 8, 18, 2]
         [10, 2, 14, 2, 10, 14, 14, 10]
         [4, 6, 18, 10, 0, 10, 16, 6]
         [12, 0, 18, 18, 18, 2, 6, 0]

.2倍したあと2桁の数字になるものは、1の位と10の位の数を足して1桁の数字にする
t_list2 = [3, 7, 7, 0, 3, 8, 9, 2]
          [1, 2, 5, 2, 1, 5, 5, 1]
          [4, 6, 9, 1, 0, 1, 7, 6]
          [3, 0, 9, 9, 9, 2, 6, 0]

・総和
even_list = [39, 22, 34, 38]
"""

REGENEX = re.compile(r'(\d)(\d)$')
even_list = []
for t in g_list2:
    t_list = [y * 2 for y in t]

    t_list2 = []
    for j in t_list:
        if j > 9:
            m = REGENEX.match(str(j))  #jを１の位の数字と10の位の数字にコンパイルする。
            if m:
                j = int(m.group(1)) + int(m.group(2))
        t_list2.append(j)
    even_list.append(sum(t_list2))

"""
all_list = [(26, 39), (9, 22), (19, 34), (40, 38)]
"""
all_list = list(zip(odd_sum_list, even_list))

"""
a[0] = 奇数番目の総和
a[1] = 偶数番目の総和
二つの数字の和をbとして、10で割り算し、
xは、あまりが出たら10からあまりを引いた数字。あまりが0なら0になる。
"""
for a in all_list:
    b = a[0] + a[1]
    amari = b % 10
    if amari > 0:
        print(10 - amari)
    elif amari == 0:
        print(0)

