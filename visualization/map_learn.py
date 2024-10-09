from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
from pyecharts.options import TitleOpts
map = Map()
data =[
    ("北京",1),
    ("上海",9),
    ("台湾",39),
    ("山东",200)

]
map.add("test map",data,"china")
map.set_global_opts(
    title_opts=TitleOpts(title="jay map title"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9, "lable":"1-9","color":"#CCFFFF"},
            {"min":10,"max":100, "lable":"10-100","color":"#FFFF99"},
            {"min":100,"max":1000, "lable":"100-1000","color":"#FF9966"},
        ]
    )
)
map.render()