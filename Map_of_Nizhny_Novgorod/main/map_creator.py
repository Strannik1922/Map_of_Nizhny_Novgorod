import folium
from .models import Markers


def map_create(path):
    city_map = folium.Map(location=[56.326722, 44.006479], zoom_start=12)

    city_map.height = (97, 'vh')

    city_map.get_root().html.add_child(folium.Element('''
    <div>
        <a href="/">На главную</a>
    </div>
    '''))

    group_attractions = folium.FeatureGroup(name='Достопримечательности', show=True)
    group_parks_and_museums = folium.FeatureGroup(name='Парки и музеи', show=True)

    markers = Markers.objects.all()

    for marker in markers:
        if marker.group == 'attractions':
            mark = folium.Marker(location=[marker.latitude, marker.longitude],
                                 tooltip=marker.header,
                                 popup=marker.description,
                                 icon=folium.Icon(color='red'))
            group_attractions.add_child(mark)

        if marker.group == 'parks_and_museums':
            mark = folium.Marker(location=[marker.latitude, marker.longitude],
                                 tooltip=marker.header,
                                 popup=marker.description,
                                 icon=folium.Icon(color='blue'))
            group_parks_and_museums.add_child(mark)

    group_attractions.add_to(city_map)
    group_parks_and_museums.add_to(city_map)

    folium.LayerControl(collapsed=False).add_to(city_map)

    city_map.save(path)
