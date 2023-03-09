# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 17:53
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中获取一个整数，如果是偶数为变量state赋值“偶数”，否则赋值“基数”
'''

int_num = int(input('请输入一个整数：'))

# 方法一
if int_num % 2 == 0:
    state = '偶数'
else:
    state = '基数'

# 条件表达式（方法二）
# state = '偶数' if int_num % 2 == 0 else '基数'

print('%d是一个%s' % (int_num, state))
