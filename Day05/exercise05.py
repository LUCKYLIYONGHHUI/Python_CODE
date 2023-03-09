# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/15 13:56
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中循环录入学生信息（姓名，年龄，成绩，性别）
    如果名称输入空字符，则停止录入
    将所有信息逐行打印出来
'''

dict_student_massage = {}
# list_student_massage = []

# 字典内嵌列表
# while True:
#     input_name = input("请输入学生姓名：")
#     if input_name == "":
#         break
#     input_age = int(input("请输入学生年龄："))
#     input_second = int(input("请输入学生成绩："))
#     input_sex = input("请输入学生性别：")
#     # list_student_massage.append(input_age)
#     # list_student_massage.append(input_second)
#     # list_student_massage.append(input_sex)
#     dict_student_massage[input_name] = [input_age, input_second, input_sex]
#
# print(dict_student_massage)
#
# for key, value in dict_student_massage.items():
#     print("%s:%s" % (key, value))

# # 字典内嵌字典
# while True:
#     input_name = input("请输入学生姓名：")
#     if input_name == "":
#         break
#     input_age = int(input("请输入学生年龄："))
#     input_second = int(input("请输入学生成绩："))
#     input_sex = input("请输入学生性别：")
#     dict_student_massage[input_name] = {"age": input_age, "second": input_second, "sex": input_sex}
#
# print(dict_student_massage)
#
# for key, value in dict_student_massage.items():
#     print("%s:%s" % (key, value))

list_student_detail_massage = []
# 列表内嵌字典
while True:
    input_name = input("请输入学生姓名：")
    if input_name == "":
        break
    input_age = int(input("请输入学生年龄："))
    input_second = int(input("请输入学生成绩："))
    input_sex = input("请输入学生性别：")
    dict_student_detail_massage = {"name": input_name, "age": input_age, "second": input_second, "sex": input_sex}
    list_student_detail_massage.append(dict_student_detail_massage)

print(list_student_detail_massage)

for item in list_student_detail_massage:
    print(item)
