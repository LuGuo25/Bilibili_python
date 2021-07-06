# 变量.py
# print是一个内置函数， 518是被输出的值
print(518)

# 常用快捷键
# Ctrl + /  添加注释
# Ctrl + Alt + L  规范格式

print('唐三')
# 英文输入引号逗号等
print('唐三', '小舞')
# sep是seperate的缩写，后面括号里面的字符就是分隔多个变量的一个符号
print('唐三', '小武', '马洪俊', sep=',')
print('唐三', '小武', '马洪俊', sep='-')
# end后面引号的内容就是以这个结尾
# print('唐三', '小武', end='-')
# 默认end会输出如下 \n 意为换行
print('唐三', '小武', end='\n')

# \+特定字符 产生了一个新的含义， 就是转义字符
# \\ \t等

# 变量
name = '史莱克七怪'

temp = name

name = '唐门'

print(name)
print(temp)

# 变量命名规范
# 1.有一定的意义 最好是一个单词
# 2.数字 字母 下划线 age good_man cher_9
# 3.不能以数字开头 如123abc是不合法的

# = 读作赋值 叫赋值符号
age = 234

# 9.9  选用以下哪个变量名赋值比较合适呢？
# a money age name

# answer:money

name = input('请输入一个史莱克七怪的名字：')
password = input('请输入密码：')
print(name, password, sep=":")
