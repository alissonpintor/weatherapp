import flet as ft
import requests

from src.components.cards import CityCard

# http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=yvSpjAIC63tntGY3qqHlIAHwGXXAEYUN&language=pt-br&q=Cuiabá
APIKEY: str = ''
LANG: str = 'pt-br'
URL = 'http://dataservice.accuweather.com/locations/v1/cities/autocomplete'


def app(page: ft.Page):

    def _serach_cities(search):
        r: requests.Request = requests.get(f'{URL}/?apikey={APIKEY}&language={LANG}&q={search}', timeout=500)
        if r.status_code == 200:
            return r.json()
        return None
        
    def _set_list(e):
        search = e.control.value
        cities = _serach_cities(search)

        if search:
            item_list.clean()
            for city in cities:
                city_id = int(city['Key'])
                city_name = city['LocalizedName']
                state_name = city['AdministrativeArea']['LocalizedName']
                country_name = city['Country']['LocalizedName']

                item = CityCard(city_id, city_name, state_name, country_name)
                item_list.controls.append(item)
            item_list.update()

    page.fonts = {
        'Roboto': 'fonts/Roboto-Regular.ttf',
        'RobotoBold': 'fonts/Roboto-Bold.ttf'
    }

    page.window_width = 360
    page.window_height = 640
    page.padding = 0


    # Logo da aplicação ---------------------------------
    logo_bgimage = ft.Image(
        src='images/logo_bg.png',
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

    logo_container = ft.Container(
        alignment=ft.alignment.center,
        content=logo_stack
    )


    # Campo de busca da aplicação -----------------------------
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
        on_submit=_set_list
    )

    search_row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            search_input
        ]
    )


    # Lista das cidades -------------------------------------
    item_list = ft.ListView(
        spacing=10,
        expand=True
    )

    main_row = ft.Column(
        controls=[
            logo_container,
            search_row,
            item_list
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    page.add(ft.Container(
        expand=True,
        content=main_row,
        padding=ft.padding.only(top=50, bottom=20),
        gradient=ft.LinearGradient(
            colors=[ft.colors.PURPLE_100, ft.colors.PURPLE_600],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right
        ),
        alignment=ft.alignment.top_center
    ))


if __name__ == '__main__':
    ft.app(target=app, assets_dir='assets')
