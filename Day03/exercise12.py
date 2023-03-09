# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 19:08
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中录入一个字符串，判断是否为回文
    判断规则：正向与反向相同
    上海自来水来自海上
'''

str_chr = input('请输入一个字符串：')

if str_chr[:len(str_chr) // 2] == str_chr[:-1 - len(str_chr) // 2:-1]:
    print('%s--该字符串是回文！' % str_chr)
    # print(str_chr[:(len(str_chr) // 2)])
    # print(str_chr[: -1 - (len(str_chr)) // 2:-1])
else:
    print('%s--该字符串不是回文！' % str_chr)
    # print(str_chr[:(len(str_chr) // 2)])
    # print(str_chr[: (len(str_chr)) // 2:-1])

# if len(str_chr) % 2 != 0:
#     if str_chr[:len(str_chr) // 2] == str_chr[:len(str_chr) // 2:-1]:
#         print('%s--该字符串是回文！' % str_chr)
#         print(str_chr[:(len(str_chr) // 2)])
#         print(str_chr[: (len(str_chr)) // 2:-1])
#     else:
#         print('%s--该字符串不是回文！' % str_chr)
#         print(str_chr[:(len(str_chr) // 2)])
#         print(str_chr[: (len(str_chr)) // 2:-1])
# else:
#     if str_chr[:len(str_chr) // 2] == str_chr[:-1 - len(str_chr) // 2:-1]:
#         print('%s--该字符串是回文！' % str_chr)
#         print(str_chr[:(len(str_chr) // 2)])
#         print(str_chr[:-1 - (len(str_chr)) // 2:-1])
#     else:
#         print('%s--该字符串不是回文！' % str_chr)
#         print(str_chr[:(len(str_chr) // 2)])
#         print(str_chr[:-1 - (len(str_chr)) // 2:-1])
