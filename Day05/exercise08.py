# 个人开发&学习
# 开发人员：lucky
# 开发时间：2022/12/15 20:42
# 名言名句：万般皆下品惟有读书高

"""
    存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
    北京∶
        景区∶故宫,天安门，天坛.
        美食:烤鸭,炸酱面，豆汁，卤煮.
    四川:
        景区︰九寨沟,峨眉山,春熙路﹒
        美食:火锅，串串香，兔头．
"""

# 不在控制台中录入
# list_place = []
# dict_place = {}
#
# dict_place["北京"] = {"景区": ["故宫", "天安门", "天坛"], "美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]}
# dict_place["四川"] = {"景区": ["九寨沟", "峨眉山", "春熙路"], "美食": ["火锅", "串串香", "兔头"]}
#
# for key, value in dict_place.items():
#     print("%s有%s" % (key, value))

# 在控制台中录入
dict_place = {}
dict_select = {}
scenic_area_name = "景区"
cate_name = "美食"

while True:
    input_place = input("请输入旅游地址：")
    if input_place == "":
        break

    list_cate = []
    list_place = []
    dict_place = {scenic_area_name: list_place, cate_name: list_cate}
    dict_select[input_place] = dict_place

    while True:
        input_scenic_area = input("请输入景区名字：")
        if input_scenic_area == "":
            break
        list_place.append(input_scenic_area)

    while True:
        input_cate = input("请输入美食名字：")
        if input_cate == "":
            break
        list_cate.append(input_cate)
print(dict_select)

# for item in list_select:
#     for key, value in dict_select.items():
#         print("%s有%s" % (list_select[dict_select[key]], list_select[dict_select[value]]))
#         # print("%s有%s" % (list_select[dict_select[key]], list_select[dict_select[value]]))
