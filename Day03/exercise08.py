# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 15:04
# 名言名句：万般皆下品惟有读书高

'''
    累加10~50之间个位不是2,5,9的整数
'''

sum_val = 0
for item in range(10, 51):
    unit = item % 10
    if unit == 2 or unit == 5 or unit == 9:
        continue
    sum_val += item
    # else:
    #     sum_val += item
print('%d' % sum_val)
