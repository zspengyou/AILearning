from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

sale_by_month = {1: 10, 2: 25, 3: 0, 4: 20, 10: 8, 7: 3}
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT));
bar.add_xaxis(list(sale_by_month.keys()))
bar.add_yaxis("sales", list(sale_by_month.values()))
bar.set_global_opts(
    title_opts=TitleOpts(title="month sale")
)
bar.render("jaytest.html")

if __name__ == "__main__":
    print(sale_by_month.keys())
    print(sale_by_month.values())


