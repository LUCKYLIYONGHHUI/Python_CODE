# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 21:19
# 名言名句：万般皆下品惟有读书高

'''
    英文单词反转
    “How are you” -->"you are How"
'''

list_num = "How are you"
list_num2 = []

list_str = list_num.split(" ")
print(list_str)

for item in range(len(list_str) - 1, -1, -1):
    list_num2.append(list_str[item])

list_result = " ".join(list_num2)
print(list_result)
