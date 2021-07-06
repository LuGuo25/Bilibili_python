# 四则运算和类型转换
money1 = 10
money2 = 20


print(money1 + money2)
print(money1 - money2)

print(money1 * money2)
print(money1 / money2)

print((100 - 40)*2 - 88 / 4)
# 1.优先级
# 2.从左至右

# 字符串中的加号就是连接符号
name = '漩涡鸣人'
tips = '666'
print(name + tips)

age = 8
# print(name + age)
# 类型转换
print(name + str(age))

# int - float
new_age = 8
new_money = 500.6

print(float(new_age))
print(int(new_money))
# 浮点型转换成整型可能会丢失数据

new_age2 = 8
print(type(str(age)))

new_money2 = '888'
print(type(int(new_money2)))

print(int(new_money2) + 10)

value = 'abc123'
# print(int(value))
# 会报错

value = '8.9'
# print(int(value))
print(value)
# float - str
new_money3 = 1.23
new_age3 = '18'

print(str(new_money3))
print(float(new_age3))