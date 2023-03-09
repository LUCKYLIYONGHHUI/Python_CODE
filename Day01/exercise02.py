# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/10 18:28
# 名言名句：万般皆下品惟有读书高
'''
在控制台中，输入一个商品单价。再输入一个数量，最后获取金额，计算应该找回多少钱？
'''

price = float(input('请输入商品单价：'))
num = int(input('请输入购买的商品数量：'))
buy_money = int(input('请输入购买商品的金额：'))

gave_money = buy_money - (price * num)

# print('应该找回' + str(gave_money) + '钱')
print('应该找回%d' % (gave_money) + '钱')
