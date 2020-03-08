import tushare as ts
import copy
import datetime

def gain_data(code):
    """

    :param code: stock code # 600030
    :return: pd.DataFrame
    """
    data = ts.get_hist_data(code)  # 一次性获取全部日k线数据
    data["date"] = copy.deepcopy(data.index)  # [i for i in data.index]
    data.index = range(len(data))
    data = data.sort_values("date")
    data.index = range(len(data))
    return data


def to_download_data(code):
    data = gain_data(code)
    data.to_excel("code" + code + ".xlsx", index=False)


def to_download_data_path(code, path):
    data = gain_data(code)
    data.to_excel(path + "code" + code + ".xlsx", index=False)


def to_download_today(path):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    daily = ts.get_today_all()
    daily['date'] = now_time
    daily.to_excel(path +  str(now_time) + ".xlsx", index=False)
    daily.to_excel(path +  "daily" + ".xlsx", index=False)


def to_download_category(path):
    now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    category = ts.get_stock_basics()
    category['date'] = now_time
    category['code'] = category.index
    category.to_excel(path + "category.xlsx", index=False)

#
# def gain_data(db, indus = None):
#     now_time = datetime.datetime.now().strftime('%Y-%m-%d')
#
#     have_data = db['daily'].find_one({"date":now_time})
#     if have_data is None:
#         daily = ts.get_today_all()
#         category = ts.get_stock_basics()
#
#         daily['date'] = now_time
#         category['date'] = now_time
#         category['code'] = category.index
#
#         db['daily'].insert_many(daily.to_dict(orient="records"))
#         db['category'].insert_many(category.to_dict(orient="records"))
#     else:
#         daily = mogoIn.get_data_df(db['daily'].find({"date":now_time}))
#         category = mogoIn.get_data_df(db['category'].find({"date":now_time}))
#
#     if indus is not None and indus != "":
#         category = category[category["industry"] == indus]
#
#     return daily, category
