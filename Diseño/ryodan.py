import flet as ft
from ryodan_router import routeryo
def mainryo(page:ft.Page):
    myRout=routeryo(page,ft)
    page.on_route_change = myRout.route_change
    page.bgcolor="#f5abb8"
    page.add(
        myRout.body
    )
    page.go('/index/index')
    page.update
ft.app(mainryo)
