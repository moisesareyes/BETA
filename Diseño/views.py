import flet as ft
from src.main import main
from src.inicio import sesion
def screen(page):
    return{
        '/':ft.View(
            route="/",
            controls=[
                main(page)
            ]
        ),
        '/1':ft.View(
            route="/1",
            controls=[
                sesion(page)
            ]   
        )
    }