# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 14:32
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中输入一个数字，再输入一个运算符（+ - * /），最后输入一个数字。
    根据运算符，计算两个数字。
    要求：如果运算符，不是加减乘除，则提示“你输入的运算符有误！”
'''

num_1 = float(input('请输入一个数字:'))
operator = input('请输入一个运算符:')
num_2 = float(input('请再输入一个数字:'))

if operator == '+':
    result = num_1 + num_2
    print('最后的结果是:%.f' % (result))
elif operator == '-':
    result = num_1 - num_2
    print('最后的结果是:%.f' % (result))
elif operator == '*':
    result = num_1 * num_2
    print('最后的结果是:%.f' % (result))
elif operator == '/':
    result = num_1 / num_2
    print('最后的结果是:%.f' % (result))
else:
    print('你输入的运算符有误！')
