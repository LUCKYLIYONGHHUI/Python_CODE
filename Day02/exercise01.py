# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/11 13:42
# 名言名句：万般皆下品惟有读书高

'''
    当钱不够时，提示“金额不足”，
    钱够时，提示“应找回”
'''

# 控制台输入数据，并储存数据
price = float(input('请输入商品单价：'))
num = int(input('请输入购买的商品数量：'))
buy_money = int(input('请输入购买商品的金额：'))

# 逻辑层
gave_money = buy_money - (price * num)
buy_total_money = price * num
if gave_money >= 0:
    print('你所购买商品一共要付%d钱，应该找回%d钱' % (buy_total_money, gave_money))
else:
    gave_money_aginst = (price * num) - buy_money
    print('金额不足！你所购买商品一共要付%d钱，你还应给我%d钱，谢谢！' % (buy_total_money, gave_money_aginst))

# 打印输出数据
# print('应该找回' + str(gave_money) + '钱')
# print('应该找回%d' % (gave_money) + '钱')
