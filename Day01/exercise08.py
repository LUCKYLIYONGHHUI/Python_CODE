# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 10:24
# 名言名句：万般皆下品惟有读书高
'''
    在控制台中获取总秒数，计算几小时零几分钟零几秒
'''

minute = int(input('请输入总秒数：'))

huor = minute // 3600
second = minute % 3600 // 60
minute1 = minute % 3600 % 60

print('%d是%.f小时%.f分钟%.f秒' % (minute, huor, second, minute1))
