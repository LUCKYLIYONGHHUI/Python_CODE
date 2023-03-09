# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 14:31
# 名言名句：万般皆下品惟有读书高

'''
    练习1：
    在控制台中录入5个数字
    打印最大值（不使用max()函数）
'''

# 定一个空列表
list_num = []

# 在控制台中录入5个数字
count = 0
while count < 5:
    count += 1
    input_num = input('请输入%d个数字：' % count)
    list_num.append(int(input_num))

# 打印最大值
max_val = list_num[0]
for index in range(1, len(list_num)):
    if max_val < list_num[index]:
        max_val = list_num[index]
print("最大值是：%d" % max_val)
