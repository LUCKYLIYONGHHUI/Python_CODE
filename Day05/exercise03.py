# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/14 16:13
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中录入日期（年月），计算这是这一年的第几天
    例如：3月5日
        1月天数+2月天数+5
'''

# 方法三
month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
input_month = int((input("要计算的月份：")))
input_day = int((input("要计算的天：")))

total_day = sum(month_day[:input_month - 1])

count_day = total_day + input_day

print("%d月%d日是这一年的第%d天" % (input_month, input_day, count_day))


# 方法二
# month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# input_month = int((input("要计算的月份：")))
# input_day = int((input("要计算的天：")))
# total_days = 0
# count_day = 0
#
# for item in range(input_month - 1):
#     total_days += month_day[item]
#
# count_day = total_days + input_day
#
# print("%d月%d日是这一年的第%d天" % (input_month, input_day, count_day))

# 方法一
# input_month = int((input("要计算的月份：")))
# input_day = int((input("要计算的天：")))
# # month_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# count_day = 0
# month_days = []
#
# if input_day > 32 and input_month < 1:
#     print("sorry！你输入的天数有误！")
#
# if input_day > 12 and input_month < 1:
#     print("sorry！你输入的月份有误！")
#
# else:
#     for item in range(1, input_month):
#         if item in (1, 3, 5, 7, 8, 10, 12):
#             month_days.append(31)
#         elif item in (4, 6, 9, 11):
#             month_days.append(30)
#         else:
#             month_days.append(28)
#
# count_day = sum(month_days) + int(input_day)
#
# print("%d月%d日是这一年的第%d天" % (input_month, input_day, count_day))
