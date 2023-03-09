# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/15 20:41
# 名言名句：万般皆下品惟有读书高

"""
    将1970年到2050年中的闰年，存入列表中
"""
# isLeapYear = []
# for item in range(1970, 2051):
#     if item % 4 == 0 and item % 100 != 0 or item % 400 == 0:
#         isLeapYear.append(item)

# 列表推导式：
isLeapYear = [item for item in range(1970, 2051) if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]
print(isLeapYear)
