from __future__ import print_function

import json
from bokeh.document import Document
from bokeh.embed import file_html
from bokeh.models.glyphs import Circle
from bokeh.models import (
    GMapPlot, Range1d, ColumnDataSource, PanTool, WheelZoomTool, BoxSelectTool, GMapOptions)
from bokeh.resources import INLINE

x_range = Range1d()
y_range = Range1d()

# JSON style string taken from: https://snazzymaps.com/style/1/pale-dawn
map_options = GMapOptions(lat=51.5356, lng=-0.0789, map_type="roadmap", zoom=10, styles="""
[{"featureType":"administrative","elementType":"all","stylers":[{"visibility":"on"},{"lightness":33}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2e5d4"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#c5dac6"}]},{"featureType":"poi.park","elementType":"labels","stylers":[{"visibility":"on"},{"lightness":20}]},{"featureType":"road","elementType":"all","stylers":[{"lightness":20}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#c5c6c6"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#e4d7c6"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#fbfaf7"}]},{"featureType":"water","elementType":"all","stylers":[{"visibility":"on"},{"color":"#acbcc9"}]}]
""")

# Google Maps requires an API key. You can find out how to get one here:
# https://developers.google.com/maps/documentation/javascript/get-api-key
API_KEY = "XXXXXX"

database = json.load(open("/home/pi/db.json"))
num_results = len(database["pollution"]) + 1

plot = GMapPlot(
    x_range=x_range, y_range=y_range,
    map_options=map_options,
    api_key=API_KEY,
)
plot.title.text = "Elephant Sensor"


def get_the_values(measurement):
    results_list = []
    for i in range(1, num_results):
        results_list.append(database["pollution"][str(i)][measurement])
    return results_list


def feel_the_fear(measurement):
    results_list = []
    for i in range(1, num_results):
        pollution_level = database["pollution"][str(i)][measurement]
        if pollution_level <= 20:
            results_list.append('green')
        elif 20 < pollution_level < 60:
            results_list.append('orange')
        elif pollution_level >= 60:
            results_list.append('red')
    return results_list

source = ColumnDataSource(
    data=dict(
        lat=get_the_values("latitude"),
        lon=get_the_values("longitude"),
        fill=feel_the_fear("pm25")
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="fill", line_color="black")
plot.add_glyph(source, circle)

pan = PanTool()
wheel_zoom = WheelZoomTool()
box_select = BoxSelectTool()

plot.add_tools(pan, wheel_zoom, box_select)

doc = Document()
doc.add_root(plot)

if __name__ == "__main__":
    doc.validate()
    filename = "maps.html"
    with open(filename, "w") as f:
        f.write(file_html(doc, INLINE, "Elephant Sensor Map"))