import flet as ft
import requests


# http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=yvSpjAIC63tntGY3qqHlIAHwGXXAEYUN&language=pt-br&q=Cuiabá
APIKEY: str = 'yvSpjAIC63tntGY3qqHlIAHwGXXAEYUN'
LANG: str = 'pt-br'
URL = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day'


class WeatherView(ft.UserControl):
    def __init__(self, location_id):
        super().__init__()
        self._location_id = location_id

    def _get_location(self):
        r = requests.get(f'{URL}/{self._location_id}/?apikey={APIKEY}&language={LANG}', timeout=500)
        if r.status_code == 200:
            return r.json()
        return None

    def _set_data_city(self):
        data = self._get_location()
  
    def _location(self):
        city = 'Várzea Grande'
        state = 'Mato Grosso'
        country = 'Brasil'

        city_text = ft.Row(
            controls=[
                ft.Text(
                    value=city,
                    size=26,
                    font_family='RobotoBold'
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        state_country_text = ft.Row(
            controls=[
                ft.Text(
                    value=f'{state} - {country}',
                    size=18
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        return ft.Column(
            controls=[
                city_text,
                state_country_text
            ],
            spacing=0,
            height=50,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    
    def _temperature(self):
        temp = ft.Text(
            value='35°',
            size=72,
            color=ft.colors.PURPLE_500,
            font_family='RobotoBold'
        )

        image = ft.Image(
            src='https://www.accuweather.com/images/weathericons/35.svg',
            width=50
        )

        temp_row = ft.Row(
            controls=[
                temp,
                image
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        return temp_row
    
    def build(self):
        location = self._location()
        temp = self._temperature()

        city = self._get_location()
        
        main_column = ft.Column(
            controls=[
                location,
                temp
            ]
        )

        return main_column