# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/12 10:51
# 名言名句：万般皆下品惟有读书高

'''
    猜数字游戏
    游戏运行产生一个1-100之间的随机数。
    让玩家重复猜测，直到猜对为止
    提示：大了、小了、猜对了，总共猜了多少次
'''

# 随机数工具（只在开头写一次）
import random

# 产生一个随机数
random_num = random.randint(1, 100)
# guess_num = int(input('请输入你要猜测的数字：'))

# 设置一个计数器
count = 0
while True:
    guess_num = int(input('请输入你要猜测的数字：'))
    count += 1
    if guess_num > random_num:
        print('sorry!你猜大了！')
    elif guess_num < random_num:
        print('sorry!你猜小了！')
    else:
        print('you are right!你猜对了！总共猜了%d次' % count)
        break
