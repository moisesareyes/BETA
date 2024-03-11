import flet as ft
import json
from router import router
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar
def main(page:ft.Page):
    normie={
        'maincolor':'#c4394d',
        'fondo':'#f5abb8'
    }
    morado={
        'maincolor':'#7139c4',
        'fondo':'#bba0de',

    }
    azulado={
        'maincolor':'#0438b3',
        'fondo':'#9cb2e6',

    }
    with open ('Diseño/usr.json','r') as file:
        inf=file.read()
    infj=json.loads(inf)
    user=infj['user']
    myRout=router(page,ft)
    page.add(myRout.body)
    page.bgcolor="#f5abb8"
    page.on_route_change = myRout.route_change
    if not user=="PEE-35141":
        page.appbar=app_bar(page)
        page.bottom_appbar=nav_bar(page,ft)
        page.go('/')
    else:
        page.go('/index')
ft.app(main)