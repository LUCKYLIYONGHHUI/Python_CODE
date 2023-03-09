# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 14:02
# 名言名句：万般皆下品惟有读书高

'''
    随机加法考试
    随机产生两个数字（1~10）
    在控制台中获取两个数相加的结果
    如果用户输入正确得10分
    总共3道题，最后输出得分
'''

import random

total = 0
for item in range(3):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    sum_12 = num1 + num2
    sum_3 = int(input('请输入%d+%d=：' % (num1, num2)))
    if sum_3 == sum_12:
        total += 10
    else:
        total += 0
print('最后总分是%d' % total)
