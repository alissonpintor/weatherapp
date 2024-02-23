import flet as ft


class CityCard(ft.UserControl):

    def __init__(self, city_id: int, city: str, state: str, country: str):
        super().__init__()

        self._city_id: int = city_id
        self._city: str = city
        self._state: str = state
        self._country: str = country
        self._letter: str = str(city[0]).upper()

    def build(self):
        text_icon = ft.Container(
            border_radius=50,
            width=40,
            height=40,
            bgcolor=ft.colors.PINK_100,
            alignment=ft.alignment.center,
            content=ft.Text(
                self._letter,
                color=ft.colors.PURPLE,
                size=24,
                font_family='RobotoBold'
            )
        )

        item_city_name = ft.Text(
            self._city,
            color=ft.colors.PURPLE_100,
            size=18,
            font_family='Roboto'
        )

        item_state_country_name = ft.Text(
            f'{self._country.capitalize()}, {self._state.capitalize()}',
            color=ft.colors.PURPLE_100,
            size=12,
            font_family='Roboto',
            italic=True
        )

        column_city_name = ft.Column(
            spacing=0,
            horizontal_alignment=ft.MainAxisAlignment.START,
            controls=[
                item_city_name,
                item_state_country_name
            ]
        )

        item_card = ft.Row(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                text_icon,
                column_city_name
            ]
        )

        item_container = ft.Container(
            content=item_card,
            width=300,
            height=60,
            padding=ft.padding.all(10),
            margin=0,
            border_radius=25,
            gradient=ft.LinearGradient(
                colors=[ft.colors.PURPLE, ft.colors.PINK]
            )
        )

        item_row = ft.Row(
            controls=[item_container],
            alignment=ft.MainAxisAlignment.CENTER
        )

        return item_row