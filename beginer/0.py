a = input()
bc = input()
s = input()
al = int(a) + int(bc.split()[0])+ int(bc.split()[1])
print(str(al) + " " + s)

############正答############
# -*- coding: utf-8 -*-
# 整数の入力
a = int(input())
# スペース区切りの整数の入力
b, c = map(int, input().split())
# 文字列の入力
s = input()
# 出力
print("{} {}".format(a+b+c, s))