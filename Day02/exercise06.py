# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 16:22
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中获取一个月份，并打印天数,或者输入有误
    1 3 5 7 8 10 12 --> 31天
    4 6 9 11 --> 30天
    2 --> 28天
'''

month = int(input('请输入一个月份：'))

if month <= 0 or month >= 15:
    print('sorry！输入有误！')
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print('%d月有31天' % month)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('%d月有30天' % month)
else:
    print('%d月有28天' % month)
