# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 14:27
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中获取一个整数，判断是否为素数。
    一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数（素数）
'''

int_num = int(input('请输入一个整数：'))

if int_num > 1:
    for item in range(2, int_num):
        if int_num % item == 0:
            print('%d不是素数！' % int_num)
            break
        # else:
        #     print('%d是素数！' % int_num)
    else:
        print('%d是素数！' % int_num)
else:
    print('%d不是素数！' % int_num)
