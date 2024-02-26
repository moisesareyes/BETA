import flet as ft
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
user="ZRO-42111"
def config (page:ft.Page):
    page.scroll='always'
    userbtn=ft.CupertinoButton(content=ft.Text("USUARIO",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300,border_radius=0)
    logout=ft.CupertinoButton(content=ft.Text("CERRAR SESIÓN",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300,border_radius=0)
    theme=ft.CupertinoButton(content=ft.Text("TEMA",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300,border_radius=0)
    privacidad=ft.CupertinoButton(content=ft.Text("PRIVACIDAD",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300,border_radius=0)
    segbtn=ft.CupertinoButton(content=ft.Text("SEGURIDAD",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300,border_radius=0)
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
    return new