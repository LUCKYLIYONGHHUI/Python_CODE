# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 11:40
# 名言名句：万般皆下品惟有读书高

'''
    根据成绩判断等级，如果录入空字符串则退出程序
    如果成绩录入错误次数达到3，则退出成绩并提示’成绩错误过多‘
'''

# 方法一

# 计数器记录错误次数
count = 0
while True:
    seconds = input('请输入一个成绩：')
    if seconds == '':
        print('你输入的是空字符串！')
        break
    seconds = int(seconds)
    if seconds < 0 or seconds > 100:
        print('输入有误！')
        count += 1
        if count == 3:
            print('成绩错误过多!')
            break
    elif 90 <= seconds:
        print('优秀！')
    elif 75 <= seconds:
        print('良好！')
    elif 60 <= seconds:
        print('及格！')
    else:
        print('不及格！')

# 方法二

# count = 0
# while count < 3:
#     seconds = input('请输入一个成绩：')
#     if seconds == '':
#         print('你输入的是空字符串！')
#         break
#     seconds = int(seconds)
#     if seconds < 0 or seconds > 100:
#         print('输入有误！')
#         count += 1
#     elif 90 <= seconds:
#         print('优秀！')
#     elif 75 <= seconds:
#         print('良好！')
#     elif 60 <= seconds:
#         print('及格！')
#     else:
#         print('不及格！')
# else:
#     print('成绩错误过多!')
