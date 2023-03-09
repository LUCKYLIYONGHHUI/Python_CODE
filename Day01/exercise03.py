# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/10 19:01
# 名言名句：万般皆下品惟有读书高
'''
    在控制台中获取分钟；再获取小时；再获取天；计算总秒数
'''

clock = float(input('请输入分钟数：'))
hour = float(input('请输入小时数：'))
# today = float(input('请输入天数：'))
minute = float(input('请输入秒数：'))

# second = (clock * 60) + (hour * 60 * 60) + (today * 24 * 60 * 60)
second = (clock * 60) + (hour * 60 * 60) + minute

print('%.f分钟是%.d秒' % (clock, clock * 60))
print('%.f小时是%.d秒' % (hour, hour * 60 * 60))
# print('%.f天是%.d秒' % (today, today * 24 * 60 * 60))
print('总秒数是%.d' % (second))
