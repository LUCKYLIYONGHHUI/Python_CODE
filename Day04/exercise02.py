# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 11:42
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中录入﹐所有学生的成绩
    输入空字符串﹐打印(一行一个)所有成绩
    打印最高分max(x)，打印最低分min(x)，打印平均分(sum(x)/len(list))
'''

list_grade = []

while True:
    input_grade = input('请输入学生的成绩：')
    if input_grade == "":
        break
    list_grade.append(int(input_grade))

# 打印整个list_grade列表,没有遍历
print(list_grade)

# 通过for函数遍历获取list_role列表中所有的元素
# for index in list_grade:
for index in range(len(list_grade)):
    print("第%d学生的成绩是%d" % (index + 1, list_grade[index]))

# 通过max()函数获取最高分
max_grade = max(list_grade)
print("最高分是：%d" % max_grade)

# 通过min()函数获取最低分
min_grade = min(list_grade)
print("最低分是：%d" % min_grade)

# 通过sum(x)/len(list_grade)获取平均分
average_grade = sum(list_grade) / len(list_grade)
print("平均分分是：%d" % average_grade)
