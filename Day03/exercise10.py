# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 18:05
# 名言名句：万般皆下品惟有读书高

'''
    练习:在控制台中获取一个字符串
        打印第一个字符
        打印最后一个字符
        打印倒数第三个字符
        打印前两个字符
        倒序打印字符
        如果字符串长度是奇数﹐则打印中间字符.
'''

str_val = input('请输入一个字符串：')

# 打印第一个字符
# chr_1 = str_val[0:1]
chr_1 = str_val[0]
print('一个字符是%s' % chr_1)

# 打印最后一个字符
# chr_2 = str_val[:-2:-1]
chr_2 = str_val[-1]
print('最后一个字符是%s' % chr_2)

# 打印倒数第三个字符
# chr_3 = str_val[-3:-4:-1]
chr_3 = str_val[-3]
print('倒数第三个字符是%s' % chr_3)

# 打印前两个字符
chr_4 = str_val[:2]
print('前两个字符是%s' % chr_4)

# 倒序打印字符
chr_5 = str_val[::-1]
print('倒序打印字符是%s' % chr_5)

# 如果字符串长度是奇数﹐则打印中间字符
if len(str_val) % 2 != 0:
    chr_6 = str_val[len(str_val) // 2]
    print('中间字符是%s' % chr_6)
else:
    print('该字符串长度不是基数！')
