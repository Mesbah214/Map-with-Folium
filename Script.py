# Tour Fixer.py
#   by: Mesbah Uddin
#       A simple app to visualize tourist spots with pictures, ratings and link to detailed information.
#       Thus helping enthusiatic tourists to plan for their trip easily and efficiently.

import folium
import pandas

url = 'https://raw.githubusercontent.com/Mesbah214/Map-with-Folium/master/Data'
state_geo = f'{url}/BD%20Admin%20Level%20-02%20Boundary%20GeoJson%20Polygon.txt'
tourist_ratings = f'{url}/Imaginary%20tourist%20attraction%20rate.csv'
state_data = pandas.read_csv(tourist_ratings)
sites = f'{url}/Ancient%20archeological%20sites%20in%20Bangladesh.csv'
marker_data = pandas.read_csv(sites)


names = list(marker_data['Name'])
lats = list(marker_data['Lat'])
lons = list(marker_data['Lon'])
rating = list(marker_data['Ratings'])
wikis = list(marker_data['Wiki'])
pics = list(marker_data['Link'])


map = folium.Map(
    location=[23.898166, 90.411074],
    zoom_start=7,
)


def color_producer(number):
    if ratings >= 4.5:
        return 'green'
    else:
        return 'blue'


folium.Choropleth(
    geo_data=state_geo,
    data=state_data,
    columns=['District', 'Ratings'],
    key_on='feature.id',
    fill_color='RdYlGn',
    fill_opacity=0.6,
    line_opacity=0.2,
    name='Choropleth',
    legend_name='Tourist Ratings (0-5)',
).add_to(map)

fgm = folium.FeatureGroup(name='places')
for name, lat, lon, ratings, wiki, pic in zip(names, lats, lons, rating, wikis, pics):
    fgm.add_child(folium.CircleMarker(
        location=[lat, lon],
        radius=9,
        tooltip='Click for more info',
        popup=f"<b>Name:</b> {name}<br><b>Ratings:</b> {ratings}<br><b>Details:</b><a href='{wiki}'> Click Here</a><br><img src='{pic}' height=142 width=290 ",
        fill_color=color_producer(ratings),
        fill_opacity=0.9,
        color='grey',
    ))

map.add_child(fgm)

map.save('Tour Fixer.html')
