import flet as ft
from router import router
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar

def main(page:ft.Page):

    user="RIN-11111"
    page.appbar=app_bar(page)
    page.bottom_appbar=nav_bar(page,ft)
    myRout=router(page,ft,user)
    page.on_route_change = myRout.route_change
    page.bgcolor="#ffe3e8"
    page.add(
        myRout.body
    )
    page.go('/')
    page.update()
ft.app(port=8550, target=main)