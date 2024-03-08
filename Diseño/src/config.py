import flet as ft
import mysql.connector
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

def config (page:ft.Page,user):
    page.scroll='always'
    userbtn=ft.ElevatedButton(content=ft.Text("USUARIO",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300)
    logout=ft.ElevatedButton(content=ft.Text("CERRAR SESIÓN",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300)
    theme=ft.ElevatedButton(content=ft.Text("TEMA",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300)
    privacidad=ft.ElevatedButton(content=ft.Text("PRIVACIDAD",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300)
    segbtn=ft.ElevatedButton(content=ft.Text("SEGURIDAD",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300)
    new=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("CONFIGURACIONES",color="BLACK",size=32,font_family="Berlin Sans FB")
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            userbtn
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            privacidad
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            segbtn
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            theme
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            logout
                        ],alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
        )
    )
    if not user=="PEE-35141":
        return new
    else:pass