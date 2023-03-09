# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 17:55
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中获取一个年份，如果是闰年，为变量day赋值29，否则赋值28
'''

isLeapYear = int(input('请输入一个年份：'))

# 真值表达式（方法一）
isTure = isLeapYear % 4 == 0 and isLeapYear % 100 != 0 or isLeapYear % 400 == 0
if isTure:
    day = 29
else:
    day = 28

# 条件表达式（方法二）
# day = 29 if isLeapYear % 4 == 0 and isLeapYear % 100 != 0 or isLeapYear % 400 == 0 else 28

print('%d年有%d天' % (isLeapYear, day))
