# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/15 20:42
# 名言名句：万般皆下品惟有读书高

"""
    5．计算一个字符串中的字符以及出现的次数．
    #思想∶
    #逐一判断字符出现的次数．
    #如果统计过则增加1，如果没统计过则等于1 .
    abcdefce
    a 1
    b 1
    c 2
    d 1
    e 2
    f 1
"""

# 方法一
# str_num = "abcdefce"
# str_num = input("请输入字符串：")
# list_num = []
# dict_result = {}
#
# for i in str_num:
#     count = 1
#     if i not in list_num:
#         dict_result[i] = 1
#     else:
#         for j in list_num:
#             if i == j:
#                 count += 1
#                 dict_result[i] = count
#     list_num.append(i)
#
# print(dict_result)
#
# for key, value in dict_result.items():
#     print("%s:%d" % (key, value))

# 方法一
dict_result = {}
str_num = "abcdefce"

for item in str_num:
    if item not in dict_result:
        dict_result[item] = 1
    else:
        dict_result[item] += 1
print(dict_result)
