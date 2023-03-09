# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/10 21:32
# 名言名句：万般皆下品惟有读书高

'''
    判断年份是否为闰年。
    闰年（True）：年份能被4整除，但是不能被100整除
    能被400整除
    平年（False）
'''

isLeapYear = int(input('请输入年份：'))

if isLeapYear % 4 == 0 and isLeapYear % 100 != 0 or isLeapYear % 400 == 0:
    print('%d是闰年！' % (isLeapYear))
else:
    print('%d是平年！' % (isLeapYear))
