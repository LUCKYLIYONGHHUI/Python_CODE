# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 16:01
# 名言名句：万般皆下品惟有读书高

'''
    练习1：在控制台中，获取一个字符串，打印每个字符的编码值
    练习2：在控制台中，重复录入一个编码值，然后打印字符，
        如果输入空字符串，则退出程序
'''

# 练习1

# str_num = input('请输入一个字符串：')
#
# for item in str_num:
#     if str_num == '':
#         break
#     str_val = ord(item)
#     print('%s的编码值是：%s' % (item, str_val))

# 练习2

while True:
    str_num = input('请输入一个编码值：')
    if str_num == '':
        break
    str_val = chr(int(str_num))
    print('%s对应的字符串是：%s' % (str_num, str_val))
