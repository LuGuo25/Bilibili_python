# 运算符.py

# 算术运算符 % 求余 // 取整 ** 求幂运算
# 赋值运算符 += -= *= /=
# 关系运算符 > < == !=
# 逻辑运算符 and or not

# 算数运算符
# bounty是赏金的意思
# bounty = 3000
#
# print(bounty / 100)
#
# print(bounty % 100)
#
# print(bounty % 55)
#
# number = input('请输入一个数字：')
# number = int(number)
# result = number % 2
# print(result)
#
# bounty = 5000
#
# print(bounty / 280) #实除
#
# print(bounty // 280) #整除
#
# number = 4
# result = number ** 0.5
# print(result)

# 赋值运算符
# number = 5000
# bounty = 5000
# # += -= *= /=
# number += 1 #等价于 number = number + 1
# print(number)
# # 其他同理
# number -= 1
# print(number)
#
# # 关系运算符
# bounty1 = 10000
# bounty2 = 10002
#
# print(bounty1 > bounty2)
#
# print('a' < 'b') #比较ASCⅡ码值

# 判断用户名是否相等
# username = input('请输入用户名:')
#
# print(username == 'admin')

# 逻辑运算符

# and
# print(True and True)
# print(True and False)
#
# # or
# print(False or True)
# print(False or False)
#
# # not
# print(not False)

# print(5 > 3 and 4 > 9)  # 即print(True and False)
# print(5 < 3 and 10 > 9) # 即print(False and True)
# print(5 == 3 and 4 > 9) # 即print(False and False)
# print(5 > 3 or 4 > 9) # 即print(True or False)
# print(not 5 > 3) # 即print(not True)
#
# print(5 > 3 and not 4 > 9) # not的优先级高于and和or

name = input('输入名字：')
bounty = input('输入赏金：')

print(name == '路飞' and bounty == '1亿')

