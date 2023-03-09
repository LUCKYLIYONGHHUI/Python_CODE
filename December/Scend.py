# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/8 15:33
# 名言名句：万般皆下品惟有读书高

# 将文件输出到文件中
fp = open('/December/text.txt', 'a+')
wr = 'lixiang'
print(wr, file=fp)
fp.close()
