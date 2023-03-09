# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/16 19:25
# 名言名句：万般皆下品惟有读书高

"""
    练习1：[“无忌”，“赵敏”，“周芷若”]
    {“无忌”：2，“赵敏”：2，“周芷若”：3}

    练习2：["无忌","赵敏","周芷若"] [101,102,103]
    {"无忌":101,"赵敏":102,"周芷若":103}
"""

# 练习1

# 常见方法：
# dict_personality = {}
#
# list_name = ["无忌", "赵敏", "周芷若"]
#
# for item in list_name:
#     dict_personality[item] = len(item)
#
# print(dict_personality)

# 字典推导式
list_name = ["无忌", "赵敏", "周芷若"]
dict_personality = {item: len(item) for item in list_name}

print(dict_personality)

# 练习2

list_name01 = ["无忌", "赵敏", "周芷若"]
list_name02 = [101, 102, 103]

dict_personality01 = {}
list_name02_long = len(list_name02)
list_name01_long = len(list_name01)

count = 0
for i in range(count, list_name01_long):
    for j in range(count, list_name02_long):
        dict_personality01[list_name01[count]] = list_name02[count]
    count += 1

print(dict_personality01)
