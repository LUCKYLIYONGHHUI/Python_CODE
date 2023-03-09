# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/10 20:06
# 名言名句：万般皆下品惟有读书高

'''
    在控制台中输入距离（distance），时间（times），初速度（initial_velocity），计算加速度(v)
    匀变速直线运动的位移与时间公式：
    加速度=（距离-初速度×时间）*2/时间平方
'''

distance = float(input('距离是：'))
times = float(input('时间是：'))
initial_velocity = float(input('初速度是：'))

acceleration = (distance - initial_velocity * times) * 2 / times ** 2

print('加速度是%.2f' % (acceleration))
