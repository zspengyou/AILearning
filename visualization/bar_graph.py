from pyecharts.charts import Bar
bar = Bar()

bar.add_xaxis(["china","us","uk"])
bar.add_yaxis("gdp",[1,2,3])
# bar.reversal_axis()
bar.render()