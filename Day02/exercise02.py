# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 14:12
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中获取一个季度（春夏秋冬），
    显示相应的月份
'''

season = input('请输入一个季节：')

if season == '春':
    print('%s天有1月、2月、3月' % (season))
elif season == '夏':
    print('%s天有4月、5月、6月' % (season))
elif season == '秋':
    print('%s天有7月、8月、9月' % (season))
elif season == '冬':
    print('%s天有10月、11月、12月' % (season))
