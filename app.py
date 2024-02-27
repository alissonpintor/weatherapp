import flet as ft
from src.home.page import HomeView
from src.clima.page import WeatherView


def app(page: ft.Page):
    page.fonts = {
        'Roboto': 'fonts/Roboto-Regular.ttf',
        'RobotoBold': 'fonts/Roboto-Bold.ttf'
    }

    page.window_width = 360
    page.window_height = 640
    page.padding = 0

    home = HomeView()
    weather = WeatherView()
    
    page.add(
        ft.Container(
            expand=True,
            content=weather,
            padding=ft.padding.only(top=50, bottom=20),
            gradient=ft.LinearGradient(
                colors=[ft.colors.PURPLE_100, ft.colors.PURPLE_600],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right
            ),
            alignment=ft.alignment.top_center
        )
    )


if __name__ == '__main__':
    ft.app(target=app, assets_dir='assets')
