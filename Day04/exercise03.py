# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 12:31
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中录入﹐所有学生的姓名
    如果姓名重复，则提示“姓名已经存在”，不在添加到列表中
    如果输入空字符串﹐则倒序打印所有学生姓名
'''

list_name = []

while True:
    input_name = input("请输入学生的姓名：")

    # 方法一
    # for index in range(len(list_name)):
    #     if input_name == list_name[index]:
    #         print("姓名已经存在!请重新输入！")
    #         continue

    # 方法二(成员运算符)
    if input_name in list_name:
        print("姓名已经存在!请重新输入！")
        continue

    if input_name == "":
        # for index in range(-1, -len(list_name), -1):
        #     print("倒序打印所有学生姓名:" + list_name[index])
        break
    list_name.append(input_name)

for index in range(-1, -len(list_name) - 1, -1):
    print("倒序打印所有学生姓名:" + list_name[index])
