# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/10 20:28
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中输入一个四位数整数：1234
    计算每一位相加和
    显示结果
'''

int_num = int(input('请输入一个四位数整数：'))

# 方法一

# 个位数
single_digit = int_num % 10
# 十位数
tens = int_num % 100 // 10
# 百位数
hundreds = int_num % 1000 // 100
# 千位数
thousands = int_num // 1000
# 求位数相加总和
total = single_digit + tens + hundreds + thousands

print('%d+%d+%d+%d=%d' % (single_digit, tens, hundreds, thousands, total))

# 方法二

total = int_num % 10
total += int_num % 100 // 10
total += int_num % 1000 // 100
total += int_num // 1000

print('位数相加和是%d' % (total))
