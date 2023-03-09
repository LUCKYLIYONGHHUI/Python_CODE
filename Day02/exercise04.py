# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 15:26
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中分别输入4个数字，打印出最大的数字
'''

num1 = float(input('请输入第一个数字：'))
num2 = float(input('请输入第二个数字：'))
num3 = float(input('请输入第三个数字：'))
num4 = float(input('请输入第四个数字：'))

# 方法一：两两相比判断最大的，再拿两个最大的相比，最好得到最大的数

# if num1 > num2:
#     num_max1 = num1
# else:
#     num_max1 = num2
#
# if num3 > num4:
#     num_max2 = num3
# else:
#     num_max2 = num4
#
# if num_max1 > num_max2:
#     max_final = num_max1
# else:
#     max_final = num_max2

# 方法二：假设最大数是第一个，然后依次与后面的数相比

max_final = num1
if max_final < num2:
    max_final = num2

if max_final < num3:
    max_final = num3

if max_final < num4:
    max_final = num4

print('%.f、%.f、%.f、%.f中最大的数是：%.f' % (num1, num2, num3, num4, max_final))
