# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 8:31
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中录入﹐西游记中你喜欢的人物
    输入空字符串﹐打印(一行一个)所有人物.
'''

# 创建一个空列表
list_role = []

while True:
    input_str = input('请输入西游记中你喜欢的人物：')
    # 通过append()函数从控制台中添加数据
    if input_str == "":
        # 通过for函数遍历获取list_role列表中所有的元素
        for index in range(len(list_role)):
            print("西游记中你喜欢的人物有" + list_role[index])
        break
    list_role.append(input_str)

# for index in range(len(list_role)):
#     print("西游记中你喜欢的人物有" + list_role[index])
