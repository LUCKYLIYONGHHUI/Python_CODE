# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 13:31
# 名言名句：万般皆下品惟有读书高

'''
    练习1：累加1~100的和
    练习2：累加1~100之间的偶数和
    练习3：累加10~36之间的和
'''

# 练习1

# sum_1 = 0
# for item in range(1, 101):
#     # sum_1 = sum_1 + item
#     sum_1 += item
# print('sum=%d' % sum_1)

# 练习2

# 方法一
# sum_2 = 0
# for item in range(1, 101):
#     if item % 2 == 0:
#         sum_2 += item
# print('sum=%d' % sum_2)

# 方法二
sum_2 = 0
for item in range(2, 101, 2):
    sum_2 += item
print('sum=%d' % sum_2)

# 练习3

# sum_3 = 0
# for item in range(10, 37):
#     sum_3 += item
# print('sum=%d' % sum_3)
