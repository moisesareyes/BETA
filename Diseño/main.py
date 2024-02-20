import flet as ft
from views import screen
def main(page:ft.Page):
    def route_change(route):
        page.views.clear()
        page.views.append(
            screen(page)[page.route]
        )
    page.on_route_change=route_change
    page.go("/")
ft.app(main)