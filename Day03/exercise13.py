# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 19:10
# 名言名句：万般皆下品惟有读书高

'''
    一个小球从100m的高度落下
    每次弹回原高度的一半
    计算：总共弹起多少次（最小弹起高度0.01m）
    总共走了多少米
'''

high_min = 0.01
high_end = 100
high_total = high_end

count = 0
while True:
    # high_end = high_end / 2
    high_end /= 2
    if high_end >= high_min:
        count += 1
        high_total += high_end * 2
    else:
        break
# high_total += 100
print('总共弹起%d次' % count)
print('总共走了%.2f米' % high_total)
