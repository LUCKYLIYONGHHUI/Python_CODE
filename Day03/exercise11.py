# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 19:06
# 名言名句：万般皆下品惟有读书高

'''
   在控制台中获取一个整数作为边长，根据边长打印矩形
   如:4
   ****
   *  *
   *  *
   ****
'''

str_sto = int(input('请输入一个整数：'))

# 计数器
i = 0
for item in range(str_sto):
    if i == 0 or i == str_sto - 1:
        print('*' * str_sto)
    else:
        print('*' + ' ' * (str_sto - 2) + '*')
    i += 1
