# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/9 17:21
# 名言名句：万般皆下品惟有读书高
'''
    汇率转换器
    1人民币 = 0.1439美元
    1美元 ≈ 6.9479人民币
'''

# #单个换算
#
# # 获取数据
# str_usd = input('请输入美元：')
# int_usd = int(str_usd)
#
# # 逻辑运算
# result = int_usd * 6.9
#
# # 显示结果
# print(int(result))


# 双向换算(方法一)

# 先选择要换算美元还是人民币，并且获取数据
num = int(input('请选择换算的方式：1、美元\t2、人民币\n'))
if num == 1 or num == 2:
    if num == 1:
        print('欢迎使用美元换算！')
        str_usd = input('请输入想要换算的美元金额：')
        int_usd = int(str_usd)
        result = int_usd * 6.9479  # 逻辑运算
        print('%d美元的最终结果是：%.2f' % (int_usd, result) + '人民币')  # 显示结果
        print('感谢使用，欢迎下次使用！')
    elif num == 2:
        print('欢迎使用人民币换算！')
        str_rmb = input('请输入想要换算的人民币金额：')
        int_rmb = int(str_rmb)
        result = int_rmb * 0.1439  # 逻辑运算
        print('%d人民币的最终结果是：%.2f' % (int_rmb, result) + '美元')  # 显示结果
        print('感谢使用，欢迎下次使用！')
else:
    print('对不起！请重新输入！')
    num = int(input('请选择换算的方式：1、美元\t2、人民币\n'))
    if num == 1:
        print('欢迎使用美元换算！')
        str_usd = input('请输入想要换算的美元金额：')
        int_usd = int(str_usd)
        result = int_usd * 6.9479  # 逻辑运算
        print('%d美元的最终结果是：%.2f' % (int_usd, result) + '人民币')  # 显示结果
        print('感谢使用，欢迎下次使用！')
    elif num == 2:
        print('欢迎使用人民币换算！')
        str_rmb = input('请输入想要换算的人民币金额：')
        int_rmb = int(str_rmb)
        result = int_rmb * 0.1439  # 逻辑运算
        print('%d人民币的最终结果是：%.2f' % (int_rmb, result) + '美元')  # 显示结果
        print('感谢使用，欢迎下次使用！')

# 双向换算（方法二&有问题待解决）

# 先选择要换算美元还是人民币，并且获取数据
# num = int(input('请选择换算的方式：1、美元\t2、人民币\n'))
# if num == 1 or num == 2:
#     if num == 1:
#         print('欢迎使用美元换算！')
#         str_usd = input('请输入想要换算的美元金额：')
#         int_usd = int(str_usd)
#         result = int_usd * 6.9479  # 逻辑运算
#         print('%d美元的最终结果是：%.2f' % (int_usd, result) + '人民币')  # 显示结果
#         print('感谢使用，欢迎下次使用！')
#     elif num == 2:
#         print('欢迎使用人民币换算！')
#         str_rmb = input('请输入想要换算的人民币金额：')
#         int_rmb = int(str_rmb)
#         result = int_rmb * 0.1439  # 逻辑运算
#         print('%d人民币的最终结果是：%.2f' % (int_rmb, result) + '美元')  # 显示结果
#         print('感谢使用，欢迎下次使用！')
# else:
#     for i in range(0.4):
#         print('对不起！请重新输入！')
#         num = int(input('请选择换算的方式：1、美元\t2、人民币\n'))
#         if num == 1:
#             print('欢迎使用美元换算！')
#             str_usd = input('请输入想要换算的美元金额：')
#             int_usd = int(str_usd)
#             result = int_usd * 6.9479  # 逻辑运算
#             print('%d美元的最终结果是：%.2f' % (int_usd, result) + '人民币')  # 显示结果
#             print('感谢使用，欢迎下次使用！')
#         elif num == 2:
#             print('欢迎使用人民币换算！')
#             str_rmb = input('请输入想要换算的人民币金额：')
#             int_rmb = int(str_rmb)
#             result = int_rmb * 0.1439  # 逻辑运算
#             print('%d人民币的最终结果是：%.2f' % (int_rmb, result) + '美元')  # 显示结果
#             print('感谢使用，欢迎下次使用！')
#         print('对不起！你还有' + (3 - i) + '次机会！')

