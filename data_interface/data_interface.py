import pandas as pd
from data_interface.gain_data_excel import to_download_data_path, to_download_today, to_download_category
import datetime
app_path = "data/"


def gain_code_data_excel(code, refresh=False):
    if refresh:
        to_download_data_path(code, app_path + "data/")
        data = pd.read_excel(app_path + "data/code" + code + ".xlsx")
        return data

    try:
        data = pd.read_excel(app_path + "data/code" + code + ".xlsx")
    except FileNotFoundError:
        to_download_data_path(code, app_path + "data/")
        data = pd.read_excel(app_path + "data/code" + code + ".xlsx")
    return data


def gain_daily_data_excel(refresh=False):
    if refresh:
        to_download_today(app_path + "daily/")
        data = pd.read_excel(app_path+"daily/" + "daily" + ".xlsx", dtype={"code": str})
        return data
    try:
        data = pd.read_excel(app_path+ "daily/" + "daily" + ".xlsx", dtype={"code": str})
    except FileNotFoundError:
        to_download_today(app_path + "daily/")
        data = pd.read_excel(app_path+ "daily/" + "daily" + ".xlsx", dtype={"code": str})
    return data


def gain_category_data_excel(refresh=False):
    if refresh:
        to_download_category(app_path)
        data = pd.read_excel(app_path + "category" + ".xlsx", dtype={"code": str})
        return data
    try:
        data = pd.read_excel(app_path + "category" + ".xlsx", dtype={"code": str})
    except FileNotFoundError:
        to_download_category(app_path)
        data = pd.read_excel(app_path + "category" + ".xlsx", dtype={"code": str})
    return data

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
