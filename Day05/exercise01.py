# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/14 13:58
# 名言名句：万般皆下品惟有读书高

'''
    使用range生成1~10之间的数字，将数字的平方存入list01中
    将list01中所有奇数存入list02
    将list01中所有偶数存入list03
    将list01中所有偶数大于5的数字增加1后存入list04
'''

# 数字的平方存入list01
# list01 = []
# for item in range(2, 10):
#     list01.append(item ** 2)

list01 = [item ** 2 for item in range(1, 11)]

# 将list01中所有奇数存入list02
# list02 = []
# for item01 in list01:
#     if item01 % 2 != 0:
#         list02.append(item01)

list02 = [item01 for item01 in list01 if item01 % 2 != 0]

# 将list01中所有偶数存入list03
list03 = [item02 for item02 in list01 if item02 % 2 == 0]

# 将list01中所有偶数大于5的数字增加1后存入list04
list04 = [item03 + 1 for item03 in list01 if item03 % 2 == 0 and item03 > 5]

print(list01)
print(list02)
print(list03)
print(list04)
