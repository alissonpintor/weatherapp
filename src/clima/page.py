from typing import Any, List
import flet as ft


class WeatherView(ft.UserControl):
    def __init__(self):
        super().__init__()
    
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

        temp_row = ft.Row(
            controls=[
                temp
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        return temp_row
    
    def build(self):
        location = self._location()
        temp = self._temperature()
        
        main_column = ft.Column(
            controls=[
                location,
                temp
            ]
        )

        return main_column