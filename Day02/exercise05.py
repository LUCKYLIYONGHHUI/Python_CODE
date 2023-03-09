# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 15:55
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中输入一个成绩，
    判断等级（优秀、良好、及格、不及格、输入有误）
'''

seconds = float(input('请输入一个成绩：'))

# 方法一：

# if seconds < 60:
#     print('不及格！')
# elif seconds >= 60 and seconds < 75:
#     print('及格！')
# elif seconds >= 75 and seconds < 85:
#     print('良好！')
# elif seconds >= 85 and seconds <= 100:
#     print('优秀！')
# else:
#     print('输入有误！')

# 方法二：

# if 0 <= seconds < 60:
#     print('不及格！')
# elif 60 <= seconds < 75:
#     print('及格！')
# elif 75 <= seconds < 85:
#     print('良好！')
# elif 85 <= seconds <= 100:
#     print('优秀！')
# else:
#     print('输入有误！')

# 方法三：

if seconds < 0 or seconds > 100:
    print('输入有误！')
elif 90 <= seconds:
    print('优秀！')
elif 75 <= seconds:
    print('良好！')
elif 60 <= seconds:
    print('及格！')
else:
    print('不及格！')
