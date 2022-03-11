from kivymd.app import MDApp
from kivy_garden.mapview import MapView
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from TripAdvisorScraping import restaurant_name,pic_URL,attraction_name,attraction_URL
from downloadmap import MapBuild
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

Config.set('graphics','maxfps',30)
Config.set('modules','touchring2','')


def test1(box5,place_name):
    place = OneLineIconListItem(text=place_name,text_color=[1,1,1,1],bg_color=[250/255,240/255,204/255,1])
    return box5.add_widget(place)


def AddtoMap(box4,box5,place_name):
    mapview = MapBuild(box5=box5, place_name=place_name)
    box4.clear_widgets()
    box4.add_widget(mapview)


class Mainpage(MDApp):

    def on_save(self, box6,instance, value, date_range):
        mdlabel = MDLabel(text=str(value),pos_hint={'center_x': .5, 'center_y': .8})
        box6.add_widget(mdlabel)

    # click cancel
    def on_cancel(self, box6,instance, value):
        mdlabel = MDLabel(text="you clicked cancel ",pos_hint={'center_x': .5, 'center_y': .8})
        box6.add_widget(mdlabel)

    def show_date_picker(self,box6):
        date_dialog = MDDatePicker(year=2021, month=10, day=1)
        date_dialog.bind(on_save=lambda instance,value,date_range,box=box6: self.on_save(box,instance,value,date_range), on_cancel=lambda instance,value,box=box6 : self.on_cancel(box,instance, value))
        date_dialog.open()


    def build(self):

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'BlueGray'
       # self.theme_cls.primary_hue = "200"

        box1 = BoxLayout()
        box2 = BoxLayout(orientation='vertical')
        box6 = BoxLayout(size_hint=(1, .1))
        box7 = BoxLayout(size_hint=(1, .9))
        button = MDRaisedButton(text= '[b]'+"Open Date Picker"+'[/b]',pos_hint= {'center_x': .1, 'center_y': .9},on_release = lambda _,box=box6: self.show_date_picker(box6=box))
        box6.add_widget(button)
        box2.add_widget(box6)
        box2.add_widget(box7)


        box3 = BoxLayout(orientation='vertical')
        box4 = BoxLayout()
        box5 = GridLayout(cols=1,spacing=[0,10],padding=10)
        mapview = MapView(zoom=11, lat=37.7749, lon=-122.4194)
        box4.add_widget(mapview)

        box3.add_widget(box4)
        box3.add_widget(box5)
        box1.add_widget(box2)
        box1.add_widget(box3)

        restaurantName_grid = GridLayout(rows=20)
        for restaurant in restaurant_name():
            txt = '[ref={:s}]{:s}[/ref]'.format(restaurant,restaurant)
            restaurant_label = Label(text='[b]'+ txt +'[/b]', color='black', markup=True)
            restaurant_label.bind(on_ref_press=lambda _,name=restaurant:test1(box5=box5,place_name=name) )
            restaurant_label.bind(on_ref_press=lambda _,name=restaurant: AddtoMap(box4=box4,box5=box5, place_name=name))
            restaurantName_grid.add_widget(restaurant_label)

        rest_Pic_Grid = GridLayout(rows=20)
        for url in pic_URL():
            img = AsyncImage(source=url)

            rest_Pic_Grid.add_widget(img)

        Attraction_Name_grid = GridLayout(rows=20)
        for attraction in attraction_name():
            txt = '[ref={:s}]{:s}[/ref]'.format(attraction,attraction)
            attraction_label = Label(text='[b]'+ txt+'[/b]', color='black', markup=True)
            attraction_label.bind(on_ref_press=lambda _,name=attraction:test1(box5=box5,place_name=name) )
            attraction_label.bind(on_ref_press=lambda _,name=attraction: AddtoMap(box4=box4,box5=box5, place_name=name))
            Attraction_Name_grid.add_widget(attraction_label)

        Attraction_Pic_grid = GridLayout(rows=20)
        for url in attraction_URL():
            img = AsyncImage(source=url)
            Attraction_Pic_grid.add_widget(img)

        box7.add_widget(restaurantName_grid)
        box7.add_widget(rest_Pic_Grid)
        box7.add_widget(Attraction_Name_grid)
        box7.add_widget(Attraction_Pic_grid)

        return box1



if __name__ == '__main__':
    Mainpage().run()
