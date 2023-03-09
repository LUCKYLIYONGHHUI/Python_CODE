# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/15 16:42
# 名言名句：万般皆下品惟有读书高

"""
    在控制台中录入多个人的多个喜好，输入空字符停止
    最后在控制台打印所有人的所有喜好
"""

"""
    [
        {"小明"：["看电视","玩游戏","玩泥巴"]}
    ]
"""

list_student_like = []
dict_student = {}

count = 0
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_student = {name: []}
    list_student_like.append(dict_student)
    while True:
        count += 1
        like = input("请输入第%d个喜好：" % count)
        if like == "":
            count = 0
            break
        dict_student[name].append(like)

for item in list_student_like:
    print(item)

"""
    {
        "小明"：["看电视","玩游戏","玩泥巴"]
    }
"""

count = 0
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    dict_student[name] = []
    while True:
        count += 1
        like = input("请输入第%d个喜好：" % count)
        if like == "":
            count = 0
            break
        dict_student[name].append(like)

for item in dict_student.items():
    print(item)
