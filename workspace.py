from data_interface.data_interface import gain_daily_data_excel, gain_category_data_excel
from heatmap.algorithm import gain_run_gain_pic

gain_daily_data_excel()
# gain_category_data_excel()

a = gain_run_gain_pic()
# a = gain_run_gain_pic("钢加工")
print(a)