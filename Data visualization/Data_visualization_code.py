import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Grid, Liquid
from pyecharts.commons.utils import JsCode

##### Connect to the data base

conn = pymysql.connect(user='root', password='123123', host='127.0.0.1', database='bikerental')
cur = conn.cursor()


##### Create new table for data visulazation

cur.execute("CREATE TABLE bike_info_DV SELECT * FROM bike_info")
cur.execute("CREATE TABLE customer_info_DV SELECT * FROM customer_info")
cur.execute("CREATE TABLE pay_info_DV SELECT * FROM pay_info")


##### check user's history

userID = "1"   # the userID need to be check

cur.execute('select * from pay_info\
            where ID = %s' ,(userID))

for s in cur.fetchall():
  print(s)
conn.commit()
cur.close()
conn.close()



###### prime account percentage

cur.execute('select * from customer_info\
            where usertype = %s' ,("0"))

num_normal = len(cur.fetchall())
conn.commit()

cur.execute('select * from customer_info\
            where usertype = %s' ,("1"))

num_prime = len(cur.fetchall())
conn.commit()
cur.close()
conn.close()

size = [num_prime, num_normal]
explode = (0.05, 0)
colors = ["orange", "green"]
labels = ["Prime customer", "Normal customer"]

plt.pie(size, explode = explode, colors = colors, autopct = '%1.1f%%', shadow = False, startangle= 90, labels= labels)
plt.show()




# Second way for pie chart

cur.execute('select * from customer_info\
            where usertype = %s' ,("0"))

num_normal = len(cur.fetchall())
conn.commit()

cur.execute('select * from customer_info\
            where usertype = %s' ,("1"))

num_prime = len(cur.fetchall())
conn.commit()

cur.execute('select * from customer_info\
            where usertype = %s' ,("2"))

num_operater = len(cur.fetchall())
conn.commit()

cur.execute('select * from customer_info\
            where usertype = %s' ,("3"))

num_manager = len(cur.fetchall())
conn.commit()

cur.close()
conn.close()

Position = ("Prime customer", "Normal customer", "Operater", "Manager")
Num = (num_prime, num_normal, num_operater, num_manager)

c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(Position, Num)],
        radius=["40%", "55%"],
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="User Structure"))
    .render("pie_User_Structure.html")
)


######## bike_status pie chart

# check the number of bike in each area
cur.execute('select * from bike_info\
            where barea = %s' ,("A"))

num_A = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s' ,("B"))

num_B = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s' ,("C"))

num_C = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s' ,("D"))

num_D = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s' ,("E"))

num_E = len(cur.fetchall())

print(num_A)
print(num_B)
print(num_C)
print(num_D)
print(num_E)


cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("A", "0"))

num_A0 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("A", "1"))

num_A1 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("B", "0"))

num_B0 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("B", "1"))

num_B1 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("C", "0"))

num_C0 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("C", "1"))

num_C1 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("D", "0"))

num_D0 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("D", "1"))

num_D1 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("E", "0"))

num_E0 = len(cur.fetchall())

cur.execute('select * from bike_info\
            where barea = %s and bstatus = %s' ,("E", "1"))

num_E1 = len(cur.fetchall())

print(num_A0)
print(num_A1)
print(num_B0)
print(num_B1)
print(num_C0)
print(num_C1)
print(num_D0)
print(num_D1)
print(num_E0)
print(num_E1)



bike_info = pd.read_csv("bike_info_DV.csv")

df_num1 = bike_info["bstatus"]
df_num2 = bike_info["barea"]

print((df_num1 == 0).sum())
print((df_num1 == 1).sum())
A_sum = (df_num2 == "A").sum()
B_sum = (df_num2 == "B").sum()
C_sum = (df_num2 == "C").sum()
D_sum = (df_num2 == "D").sum()
E_sum = (df_num2 == "E").sum()
print(A_sum)
print(B_sum)
print(C_sum)
print(D_sum)
print(E_sum)
print(((bike_info["bstatus"] == 0) & (bike_info["barea"] == "A")).sum())
print(((bike_info["bstatus"] == 1) & (bike_info["barea"] == "A")).sum())
print(((bike_info["bstatus"] == 0) & (bike_info["barea"] == "B")).sum())
print(((bike_info["bstatus"] == 1) & (bike_info["barea"] == "B")).sum())
print(((bike_info["bstatus"] == 0) & (bike_info["barea"] == "C")).sum())
print(((bike_info["bstatus"] == 1) & (bike_info["barea"] == "C")).sum())
print(((bike_info["bstatus"] == 0) & (bike_info["barea"] == "D")).sum())
print(((bike_info["bstatus"] == 1) & (bike_info["barea"] == "D")).sum())
print(((bike_info["bstatus"] == 0) & (bike_info["barea"] == "E")).sum())
print(((bike_info["bstatus"] == 1) & (bike_info["barea"] == "E")).sum())


inner_x_data = ["A", "B", "C", "D", "E"]
inner_y_data = [62, 111, 112, 94, 121]
inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]

outer_x_data = ["A_good", "A_broken", "B_good", "B_broken", "C_good", "C_broken", "D_good", "D_broken", "E_good", "E_broken"]
outer_y_data = [58, 4, 105, 6, 104, 8, 91, 3, 113, 8]
outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]

(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="Area",
        data_pair=inner_data_pair,
        radius=[0, "30%"],
        label_opts=opts.LabelOpts(position="inner"),
    )
    .add(
        series_name="status",
        radius=["40%", "55%"],
        data_pair=outer_data_pair,
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
    .render("pie_bike_status.html")
)




######### Bar plot for rent duration


pay_info = pd.read_csv("pay_info_DV.csv")
customer_info = pd.read_csv("customer_info_DV.csv")
#merge two dataframe
combined_info = pd.merge(pay_info, customer_info)
# normal customer duration
nh_1 = ((combined_info["duration"] <= 60) & (combined_info["usertype"] == 0)).sum()
nh_2 = ((combined_info["duration"] > 60) & (combined_info["duration"] <= 120) & (combined_info["usertype"] == 0)).sum()
nh_3 = ((combined_info["duration"] > 120) & (combined_info["duration"] <= 180) & (combined_info["usertype"] == 0)).sum()
nh_4 = ((combined_info["duration"] > 180) & (combined_info["duration"] <= 240) & (combined_info["usertype"] == 0)).sum()
nh_5 = ((combined_info["duration"] > 240) & (combined_info["duration"] <= 300) & (combined_info["usertype"] == 0)).sum()
nh_6 = ((combined_info["duration"] > 300) & (combined_info["duration"] <= 900) & (combined_info["usertype"] == 0)).sum()
# prime customer duration
ph_1 = ((combined_info["duration"] <= 60) & (combined_info["usertype"] == 1)).sum()
ph_2 = ((combined_info["duration"] > 60) & (combined_info["duration"] <= 120) & (combined_info["usertype"] == 1)).sum()
ph_3 = ((combined_info["duration"] > 120) & (combined_info["duration"] <= 180) & (combined_info["usertype"] == 1)).sum()
ph_4 = ((combined_info["duration"] > 180) & (combined_info["duration"] <= 240) & (combined_info["usertype"] == 1)).sum()
ph_5 = ((combined_info["duration"] > 240) & (combined_info["duration"] <= 300) & (combined_info["usertype"] == 1)).sum()
ph_6 = ((combined_info["duration"] > 300) & (combined_info["duration"] <= 900) & (combined_info["usertype"] == 1)).sum()

print(nh_1)
print(nh_2)
print(nh_3)
print(nh_4)
print(nh_5)
print(nh_6)
print(ph_1)
print(ph_2)
print(ph_3)
print(ph_4)
print(ph_5)
print(ph_6)



x_label = ("Under 1 hour", "1~2 hours", "2~3 hours","3~4 hours", "4~5 hours", "Above 5 hours")
# n_yaxis = [nh_1, nh_2, nh_3, nh_4, nh_5, nh_6]
# p_yaxis = [ph_1, ph_2, ph_3, ph_4, ph_5, ph_6]
# [50, 54, 58, 76, 65, 338]
# [14, 15, 25, 15, 8, 70]
c = (
    Bar()
    .add_xaxis(x_label)
    .add_yaxis("Normal Customer", [294, 25, 21, 17, 25, 127])
    .add_yaxis("Prime Customer", [155, 13, 16, 7, 20, 88])
    .set_global_opts(title_opts=opts.TitleOpts(title="Rent Duration", subtitle="Normal & Prime"))
    .render("bar_Rent_Duration1.html")
)




######### Wordcloud


data = [
    ("BikeRental", "999"),
    ("Low-Carbon", "777"),
    ("environmental protection", "699"),
    ("GREEN", "688"),
    ("Convenient", "588"),
    ("environmental", "516"),
    ("change", "515"),
    ("BIKE", "483"),
    ("breakthrough", "462"),
    ("GREEN", "449"),
    ("EASY", "429"),
    ("Clean", "407"),
    ("Fresh Air", "406"),
    ("Convenient", "406"),
    ("Smart", "386"),
    ("Sustainable", "385"),
    ("Innovation", "375"),
    ("traveling", "355"),
    ("prime", "355"),
    ("Mobile bicycle sharing", "335"),
    ("Eco-friendly", "324"),
    ("cycling infrastructure", "304"),
    ("SHARE", "304"),
    ("earth", "284"),
    ("Bicycle", "284"),
    ("tourist", "284"),
    ("Sustainable", "254"),
    ("save time", "254"),
    ("Glasgow", "253"),
    ("Public", "253"),
    ("Eco-friendly", "223"),
    ("prime", "223"),
    ("GREEN", "223"),
    ("Fresh Air", "223"),
    ("tourist", "223"),
    ("Sustainable", "223"),
    ("cycling infrastructure", "223"),
    ("traffic", "223"),
    ("Renewable", "223"),
    ("Renewable", "152"),
    ("Sustainable", "152"),
    ("Eco-friendly", "152"),
    ("traveling", "152"),
    ("Smart", "152"),
    ("BIKE", "152"),
    ("BIKE", "152"),
    ("Renewable", "152"),
    ("Sustainable", "112"),
    ("Low-Carbon", "112"),
    ("prime", "112"),
    ("traveling", "112"),
    ("GREEN", "112"),
    ("discount", "112"),
    ("Fresh Air", "112"),
    ("Fresh Air", "92"),
    ("Renewable", "92"),
    ("Eco-friendly", "92"),
    ("Glasgow", "92"),
    ("earth", "92"),
    ("traffic", "92"),
    ("prime", "72"),
    ("save time", "72"),
    ("Renewable", "72"),
    ("traveling", "72"),
    ("Low-Carbon", "71"),
    ("BOOMING", "71"),
    ("Smart", "71"),
    ("GREEN", "71"),
    ("safety", "71"),
    ("helpful", "71"),
    ("GREEN", "71"),
    ("tourist", "71"),
    ("Low-Carbon", "71"),
    ("Convenient", "71"),
    ("discount", "71"),
    ("Renewable", "71"),
    ("breakthrough", "71"),
    ("BIKE", "71"),
    ("traffic", "41"),
    ("tourist", "41"),
    ("environmental friendly", "41"),
    ("Convenient", "41"),
    ("Fresh Air", "41"),
    ("Renewable", "41"),
    ("Fresh Air", "41"),
    ("GREEN", "41"),
    ("Mobile bicycle sharing", "41"),
    ("BIKE", "41"),
    ("Fresh Air", "21"),
    ("prime", "21"),
    ("environmental protection", "21"),
    ("BIKE", "21"),
    ("Low-Carbon", "21"),
    ("BIKE", "21"),
    ("NEW", "21"),
    ("Smart", "21"),
    ("GREEN", "11"),
    ("GREEN", "11"),
    ("Low-Carbon", "11"),
    ("GREEN", "11"),
    ("save time", "11"),
    ("Glasgow", "11"),
    ("save time", "11"),
    ("prime", "11"),
    ("tourist", "11"),
    ("BIKE", "11"),
    ("BIKE", "11"),
    ("cycling infrastructure", "11"),
    ("Eco-friendly", "11"),
    ("traffic", "11"),
    ("Eco-friendly", "11"),
    ("breakthrough", "11"),
    ("Low-Carbon", "11"),
    ("cycling infrastructure", "11"),
    ("Low-Carbon", "11"),
    ("Glasgow", "11"),
    ("prime", "11"),
    ("tourist", "11"),
    ("traveling", "11"),
    ("Mobile bicycle sharing", "11"),
    ("traveling", "11"),
    ("BIKE", "11"),
    ("BIKE", "11"),
    ("Smart", "11"),
    ("Mobile bicycle sharing", "11"),
    ("Smart", "11"),
    ("Convenient", "11"),
    ("discount", "11"),
    ("GREEN", "11"),
    ("Convenient", "11"),
    ("discount", "11"),
    ("Low-Carbon", "11"),
    ("Low-Carbon", "11"),
]


(
    WordCloud()
    .add(series_name="BikeRental", data_pair=data, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="BikeRental", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("BikeRental_wordcloud.html")
)



##########   Liquid charts

bike_info = pd.read_csv("bike_info_DV.csv")   #input datatable

bike_usage_num = (bike_info["busage"] == 1).sum()   # count how many bike is being used
bike_usage_rate = bike_usage_num / 500              # usage rate

customer_info = pd.read_csv("customer_info_DV.csv")   #input datatable

customer_prime_num = (customer_info["usertype"] == 1).sum()
customer_total_num = (customer_info["usertype"] == 0).sum() + customer_prime_num
customer_prime_rate = customer_prime_num / customer_total_num


l1 = (
    Liquid()
    .add("Bike ueage Rate", [bike_usage_rate, bike_usage_num], center=["60%", "50%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid Chart"))
)

l2 = Liquid().add(
    "Prime Rate",
    [customer_prime_rate],
    center=["25%", "50%"],
    label_opts=opts.LabelOpts(
        font_size=50,
        formatter=JsCode(
            """function (param) {
                    return (Math.floor(param.value * 10000) / 100) + '%';
                }"""
        ),
        position="inside",
    ),
)

grid = Grid().add(l1, grid_opts=opts.GridOpts()).add(l2, grid_opts=opts.GridOpts())
grid.render("multiple_liquid.html")









