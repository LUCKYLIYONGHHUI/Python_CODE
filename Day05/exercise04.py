# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/15 12:30
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中循环录入商品信息（名称，单价）
    如果名称输入空字符，则停止录入
    将所有信息逐行打印出来
'''

dict01 = {}

while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = int(input("请输入商品单价："))
    dict01[name] = price
print(dict01)

for key, value in dict01.items():
    print("'%s'：%d" % (key, value))
