import flet as ft
from router import router
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar

def main(page:ft.Page):
    page.appbar=app_bar(page,ft)
    page.bottom_appbar=nav_bar(page,ft)
    myRout=router(page,ft)
    page.on_route_change = myRout.route_change
    page.add(
        myRout.body
    )
    page.go('/')
    
ft.app(target=main,assets_dir="assets")