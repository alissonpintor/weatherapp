import flet as ft
import time
import requests

from src.components.cards import CityCard

# http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=yvSpjAIC63tntGY3qqHlIAHwGXXAEYUN&language=pt-br&q=Cuiabá
APIKEY: str = 'yvSpjAIC63tntGY3qqHlIAHwGXXAEYUN'
LANG: str = 'pt-br'
URL = 'http://dataservice.accuweather.com/locations/v1/cities/autocomplete'


class HomeView(ft.UserControl):
    def __init__(self):
        super().__init__()
        self._item_list = ft.ListView(
            spacing=10,
            expand=True
        )

    def _search_cities(self, search):
        r: requests.Request = requests.get(f'{URL}/?apikey={APIKEY}&language={LANG}&q={search}', timeout=500)
        if r.status_code == 200:
            return r.json()
        return None

    def _set_list(self, e):
        search = e.control.value

        self._item_list.clean()
        self._item_list.controls.append(
            ft.Row(
                controls=[ft.ProgressRing(
                    width=25,
                    height=25,
                    expand=False,
                    expand_loose=False
                )],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        self._item_list.update()
        
        cities = self._search_cities(search)

        if cities:
            self._item_list.clean()
            for city in cities:
                city_id = int(city['Key'])
                city_name = city['LocalizedName']
                state_name = city['AdministrativeArea']['LocalizedName']
                country_name = city['Country']['LocalizedName']

                item = CityCard(city_id, city_name, state_name, country_name)
                self._item_list.controls.append(item)
            self._item_list.update()
        else:
            self._item_list.clean()
            self._item_list.controls.append(
                ft.Row(
                    controls=[ft.Text('Cidade não econtrada')],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            )
            self._item_list.update()

    def _generete_logo(self):
        # Logo da aplicação ---------------------------------
        logo_bgimage = ft.Image(
            #src='images/logo_bg.png',
            src='https://cdn-icons-png.flaticon.com/512/4724/4724562.png',
            fit=ft.ImageFit.CONTAIN,
            width=80,
        )

        logo_title = ft.Text(
            'Clima Brasil',
            color=ft.colors.PURPLE,
            font_family='RobotoBold',
            theme_style=ft.TextThemeStyle.TITLE_LARGE
        )
        logo_subtitle = ft.Text(
            'Saiba o clima da sua cidade',
            color=ft.colors.PURPLE_100
        )

        logo_column = ft.Column(
            controls=[
                logo_title,
                logo_subtitle
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.START,
            left=60
        )

        logo_stack = ft.Stack(
            controls=[
                logo_bgimage,
                logo_column
            ],
            height=70,
            width=240
        )

        return ft.Container(
            alignment=ft.alignment.center,
            content=logo_stack
        )
    
    def _generate_input_search(self):
        search_input = ft.TextField(
            width=300,
            height=50,
            bgcolor=ft.colors.PURPLE_100,
            border_radius=50,
            border_width=0,
            label='Digite a sua cidade',
            color=ft.colors.PURPLE,
            label_style=ft.TextStyle(
                color=ft.colors.PURPLE_300,
                size=14
            ),
            suffix_icon=ft.icons.SEARCH,
            suffix_style=ft.TextStyle(color=ft.colors.AMBER, bgcolor=ft.colors.AMBER),
            on_submit=self._set_list
        )

        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                search_input
            ]
        )

    def build(self):
        logo_container = self._generete_logo()
        search_container = self._generate_input_search()

        main_row = ft.Column(
            controls=[
                logo_container,
                search_container,
                self._item_list
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )

        return main_row
