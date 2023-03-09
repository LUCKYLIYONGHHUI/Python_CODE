# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 15:25
# 名言名句：万般皆下品惟有读书高

'''
    在列表中[9,25,12,8]，删除大于10的数字
'''

list_num = [9, 25, 12, 8]

# 测试
# for i in range(-1, -len(list_num) - 1, -1):
# for i in range(len(list_num)-1, -1, -1):
#     print(list_num[i])
# list_num = [9, 25, 12, 8]

for index in range(len(list_num) - 1, -1, -1):
# for index in range(- 1, -len(list_num) - 1, -1):  # 测试（运行不了）
    if list_num[index] > 10:
        list_num.remove(list_num[index])
print(list_num)
