import folium
from folium import JsCode
from folium.plugins import Realtime

m = folium.Map(location=[40.73, -73.94], zoom_start=12)
source = "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/subway_stations.geojson"

Realtime(
    source,
    get_feature_id=JsCode("(f) => { return f.properties.objectid }"),
    point_to_layer=JsCode("(f, latlng) => { return L.circleMarker(latlng, {radius: 8, fillOpacity: 0.2})}"),
    interval=10000,
).add_to(m)

m