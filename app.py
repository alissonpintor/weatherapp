import flet as ft
from src.pages.home import HomeView
from src.pages.weather import WeatherView


def app(page: ft.Page):
    page.fonts = {
        'Roboto': 'fonts/Roboto-Regular.ttf',
        'RobotoBold': 'fonts/Roboto-Bold.ttf'
    }

    page.window_width = 360
    page.window_height = 640
    page.padding = 0

    home = HomeView(page)

    def route_change(e):
        page.views.clear()
        troute = ft.TemplateRoute(page.route)

        page.views.append(ft.View(
            route='/',
            padding=0,
            appbar=ft.AppBar(
                bgcolor=ft.colors.PURPLE_400
            ),
            controls=[
                ft.Container(
                    expand=True,
                    content=home,
                    padding=ft.padding.only(top=50, bottom=20),
                    gradient=ft.LinearGradient(
                        colors=[ft.colors.PURPLE_100, ft.colors.PURPLE_600],
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right
                    ),
                    alignment=ft.alignment.top_center
                )
            ]
            )
        )

        if troute.match('/weather/:location_id'):
            weather = WeatherView(troute.location_id)
      
            page.views.append(
                ft.View(
                    route=f'/weather/{troute.location_id}',
                    padding=0,
                    appbar=ft.AppBar(
                        bgcolor=ft.colors.PURPLE_400
                    ),
                    controls=[
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
                    ]
                )
            )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=app, assets_dir='assets')
