data = """
云南白药|000538,               苏宁电器|002024,    中联重科|000157,               格力电器|000651,               福耀玻璃|600660,               包钢稀土|600111,               贵州茅台|600519,               青岛海尔|600690,               大北农|002385,               国电南瑞|600406,               古井贡酒|000596,               三一重工|600031,               山西汾酒|600809,               阳光照明|600261,               青松建化|600425,               上海家化|600315,               巨化股份|600160,               峨眉山A|000888,悦达投资|600805,               上海电气|601727,               四维图新|002405,               川大智胜|002253,               海康威视|002415,               超图软件|300036,               华力创通|300045,               科大讯飞|002230,               新北洋|002376,               碧水源|300070,               双鹭药业|002038,               万科A|000002,               中国太保|601601,               中国平安|601318,               天士力|600535,               工商银行|601398,               中国银行|601988,               同仁堂|600085,               博瑞传播|600880,               天源迪科|300047,               武汉凡谷|002194,               中国神华|601088,               天津港|600717,               上汽集团|600104,               宝钢股份|600019,               建设银行|601939,               苏宁电器|002024, 中联重科|000157,               格力电器|000651,               福耀玻璃|600660,               包钢稀土|600111,               贵州茅台|600519,               青岛海尔|600690,               大北农|002385,               国电南瑞|600406,               古井贡酒|000596,               三一重工|600031,               山西汾酒|600809,               阳光照明|600261,               青松建化|600425,               上海家化|600315,               巨化股份|600160,               峨眉山A|000888,               悦达投资|600805,               上海电气|601727,               四维图新|002405,               川大智胜|002253,               海康威视|002415,               超图软件|300036,               华力创通300045,               科大讯飞|002230,               新北洋|002376,               碧水源|300070,               双鹭药业|002038,               万科A|000002,               中国太保|601601,               中国平安|601318,               天士力|600535,               工商银行|601398,               中国银行|601988,               同仁堂|600085,               博瑞传播|600880,               天源迪科|300047,               武汉凡谷|002194,               中国神华|601088,               天津港|600717,               上汽集团|600104,               宝钢股份|600019,               建设银行|601939,               中煤能源|601898,               潍柴动力|000338,               中泰化学|002092,               民生银行|600016,               青岛啤酒|600600

"""
data = data.replace(" ", "")
data = data.replace("\n", "")
data = data.split(",")

import pandas as pd

all_code = []
for i in data:
    inter = i.split("|")
    if len(inter) > 1:
        all_code.append({"code": inter[1], "name": inter[0]})

yangshi_50 = pd.DataFrame(all_code).drop_duplicates()
# print(yangshi_50)