from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy_garden.mapview import MapView
from finalproject_class_ver2 import GoogleMap
from kivy_garden.mapview import MapMarkerPopup
from kivy.uix.button import Button
from kivymd.uix.list import MDList,OneLineIconListItem,OneLineListItem,TwoLineListItem
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import Screen


def test(box5, place_name):
    place = OneLineIconListItem(text=place_name, text_color=[1,1,1,1], bg_color=[250/255,240/255,204/255,1])
    return box5.add_widget(place)

def MapBuild(box5,place_name):
    screen = Screen()
    scroll = ScrollView()
    list_view = MDList()
    tp = TabbedPanel()
    ta = TabbedPanelHeader(text='attractions')
    tc = TabbedPanelHeader(text='crime rates')
    tp.default_tab_text = 'restaurants'

    mapview = MapView(zoom=11, lat=37.7749, lon=-122.4194)

    client = GoogleMap(address_or_zip=place_name+', San Francisco', foodkind='restaurants')
    Restaurant_NearBy = client.restaurantList
    marker1 = MapMarkerPopup(lat=client.lat, lon=client.lng, source='map-marker-radius.png')
    item = OneLineListItem(text=place_name, size_hint=(None, None), size=(200, 100), text_color='black',
                           bg_color=[1, 1, 1, 1])
    butt = Button(text=place_name, font_size=15)
    butt.bind(on_press=lambda _, name=place_name: test(box5=box5, place_name=place_name))
    item.add_widget(butt)
    marker1.add_widget(item)

    print(client.lat,client.lng)
    mapview.add_widget(marker1)


    for rest in Restaurant_NearBy:
        name = rest[0]
        star = str(rest[1])
        rest_lat = rest[3]
        rest_lon = rest[4]
        marker = MapMarkerPopup(lat=rest_lat, lon=rest_lon, source='google-maps_red.png')
        item = TwoLineListItem(text=name, secondary_text=star,size_hint=(None,None),size=(200,100), text_color='black', bg_color=[1,1,1,1])
        butt = Button(text=str(name)+'\n rating: '+str(star),font_size=15)
        butt.bind(on_press=lambda _,name=name:test(box5=box5,place_name=str(name)))
        item.add_widget(butt)
        marker.add_widget(item)
        mapview.add_widget(marker)

    tp.default_tab_content = mapview

    mapview2 = MapView(zoom=11, lat=37.7749, lon=-122.4194)
    Attraction_NearBy = client.attractionList
    marker2 = MapMarkerPopup(lat=client.lat, lon=client.lng, source='map-marker-radius.png')
    print(client.lat,client.lng)
    mapview2.add_widget(marker2)


    for rest in Attraction_NearBy:
        name = rest[0]
        star = str(rest[1])
        rest_lat = rest[3]
        rest_lon = rest[4]
        marker = MapMarkerPopup(lat=rest_lat, lon=rest_lon, source='google-maps_blue.png')
        item = TwoLineListItem(text=name, secondary_text=star,size_hint=(None,None),size=(200,100), text_color='black', bg_color=[1,1,1,1])
        butt = Button(text=str(name)+'\n rating: '+str(star),font_size=15)
        butt.bind(on_press=lambda _,name=name:test(box5=box5,place_name=str(name)))
        item.add_widget(butt)
        marker.add_widget(item)
        mapview2.add_widget(marker)

    ta.content = mapview2
    tc.content = Image(source='crime rate.png')

    tp.add_widget(ta)
    tp.add_widget(tc)

    return tp
