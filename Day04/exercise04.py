# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 14:23
# 名言名句：万般皆下品惟有读书高

'''
    练习1：
    将列表[54,25,78,35,17,3,19]中
    大于30的数字存入另一个列表中，并画出内存图
'''

list_yuan = [54, 25, 78, 35, 17, 3, 19]
list_end = []

for index in range(len(list_yuan)):
    if list_yuan[index] > 30:
        list_end.append(list_yuan[index])
print("大于30的数字是" + str(list_end))
