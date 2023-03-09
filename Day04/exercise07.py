# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 20:56
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中循环输入字符串，如果输入空则停止。
    最后打印所有内容（拼接后的字符串）
'''

list_str = []

while True:
    input_str = input('请你输入字符串：')
    if input_str == "":
        break
    list_str.append(input_str)

str_result = "".join(list_str)
print("拼接后的字符串:%s" % str_result)
