import flet as ft
import json
from router import router
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar
from user_controls.themes import *
def main(page:ft.Page):
    def running(user,theme):
        myRout=router(page,ft,theme)
        page.add(myRout.body)
        page.on_route_change = myRout.route_change
        page.bgcolor=f"{theme['fondo']}"
        if not user=="PEE-35141":
            page.appbar=app_bar(page,theme)
            page.bottom_appbar=nav_bar(page,theme)
            page.go('/')
        else:
            page.go('/index')
    with open ('Diseño/usr.json','r') as file:
        inf=file.read()
    infj=json.loads(inf)
    user=infj['user']
    theme=infj['theme']
    if theme=='normie':running(user,normie)
    elif theme=='morado':running(user,morado)
    elif theme=='azulado':running(user,azulado)
    elif theme=='verde':running(user,verde)
    elif theme=='cyan':running(user,cyan)
    elif theme=='veceleste':running(user,veceleste)
    elif theme=='anaranjado':running(user,anaranjado)
    elif theme=='naranja':running(user,naranja)
    elif theme=='dorado':running(user,dorado)
    elif theme=='dark':running(user,dark)

ft.app(main)