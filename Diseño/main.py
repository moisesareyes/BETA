import flet as ft
from router import router
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar
def fromhere(user):
    def main(page:ft.Page):
        myRout=router(page,ft,user)
        page.on_route_change = myRout.route_change
        page.bgcolor="#f5abb8"
        page.add(
            myRout.body
        )
        if user=="PEE-35141":page.go('/index/index')
        else:
            page.appbar=app_bar(page)
            page.bottom_appbar=nav_bar(page,ft)
            page.go('/')
    ft.app(main)