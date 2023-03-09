# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 8:38
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中，获取一个开始值，一个结束值，将中间的数字打印出来。
    例如：开始值3，结束值10，打印4,5,6,7,8,9
'''

# while语句

start_val = int(input('请输入开始值：'))
end_val = int(input('请输入结束值：'))

# 方法一
while start_val < end_val:
    print('%d' % start_val)
    start_val += 1
    # print('%d' % start_val)
    if start_val == end_val:
        break

# 方法一
# while start_val < end_val:
#     if start_val == end_val:
#         break
#     print('%d' % start_val)
#     start_val += 1


