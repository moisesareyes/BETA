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
def transf_main (page:ft.Page,user,theme):
    page.scroll='always'
    rec=ft.ElevatedButton(content=ft.Text("RECARGAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _: page.go("/transf/recarga"))
    conv=ft.ElevatedButton(content=ft.Text("CONVERTIR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _: page.go("/trasf/converse"))
    transf=ft.ElevatedButton(content=ft.Text("TRASNFERIR",color="WHITE",font_family="Berlin Sans FB"),bgcolor=f"{theme['maincolor']}",width=300,on_click=lambda _:page.go("/transf/transferencia"))
    new=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("TRANSFERENCIAS",color="BLACK",size=32,font_family="Berlin Sans FB")
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            rec
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            conv
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            transf
                        ],alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
        )
    )
    if not user=="PEE-35141":
        return new
    else:pass