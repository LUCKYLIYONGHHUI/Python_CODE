# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 10:17
# 名言名句：万般皆下品惟有读书高

'''
    一张纸的厚度是0.01毫米，
    请计算对折多少次，超过珠穆朗玛峰（8844.43米）
'''

thickness = 0.01 * 0.001
hight = 8844.43

count = 0
while thickness < hight:
    thickness *= 2
    count += 1
    # print('%f' % thickness)
print('对折%d次，超过珠穆朗玛峰' % count)
