# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/13 21:50
# 名言名句：万般皆下品惟有读书高

'''
    彩票 双色球
    红球：6个，1--33之间的整数 不能重复
    蓝球：1个，1--16之间的整数
    （1）随机产生一注彩票[7个红球 1个蓝球]。
    （2）在控制台中购买一注彩票
    提示：
    “请输入第1个红球号码：”
    “请输入第2个红球号码：”
    “号码不在范围内”
    “号码已经重复”
    “请输入蓝球号码：”
'''

import random

print("随机产生一注彩票[6个红球 1个蓝球]:")

# 随机产生一注彩票[7个红球 1个蓝球]
# 获取红球
red_ball01 = []
while len(red_ball01) < 6:
    random_num_red = random.randint(1, 33)
    if random_num_red not in red_ball01:
        red_ball01.append(random_num_red)

# 获取蓝球
blue_ball01 = []
random_num_blue = random.randint(1, 16)
blue_ball01.append(random_num_blue)

print("红球：" + str(red_ball01))
print("蓝球：" + str(blue_ball01))

print("在控制台中购买一注彩票:")

# 在控制台中购买一注彩票
# 控制台中获取红球号码
buy_red_number = []
while len(buy_red_number) < 6:
    red_ball_number01 = int(input("请输入第%d个红球号码：" % (len(buy_red_number) + 1)))
    if red_ball_number01 > 33 or red_ball_number01 < 1:
        print("号码不在范围内!请重新输入!")
    elif red_ball_number01 in buy_red_number:
        print("号码已经重复!请重新输入!")
    else:
        buy_red_number.append(red_ball_number01)

print("你购买的红球号码是：" + str(buy_red_number))

# 控制台中获取蓝球号码
buy_blue_number = []
while len(buy_blue_number) < 1:
    buy_ball_number01 = int(input("请输入蓝球号码："))
    if buy_ball_number01 > 16 or buy_ball_number01 < 1:
        print("号码不在范围内!请重新输入!")
        continue
    buy_blue_number.append(buy_ball_number01)

print("你购买的蓝球号码是：" + str(buy_blue_number))

# 购买判断是否中奖
# 成功次数
count01 = 0
# 失败次数
count02 = 0
for item in range(len(buy_red_number)):
    for item01 in range(len(red_ball01)):
        if buy_red_number[item] == red_ball01[item01]:
            count01 += 1
            count02 = len(buy_red_number) - count01
print("你一共猜对了%d个红球！" % count01)

if count02 == 0:
    print("真遗憾！你没有猜对一个红球！")
else:
    print("你一共猜错了%d个红球！" % count02)

if buy_blue_number[0] in blue_ball01:
    print("恭喜你！猜中了一个蓝球！：" + str(buy_blue_number))
else:
    print("真遗憾！你没有猜对一个蓝球！")
