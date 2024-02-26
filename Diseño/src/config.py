import flet as ft
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
user="ZRO-42111"
def config (page,ft=ft):
    page.scroll='always'
    usr_c=ft.Container(
        border_radius=0,
        border=ft.border.all(3,"BLACK"),
        width=300,
        height=100,
        content=(
            ft.Column(
                [
                    ft.Column(
                        [
                            ft.Container(height=10)
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Text("USUARIO",color="WHITE",size=32,font_family="Berlin Sans FB")
                        ]
                    )
                ]
            )
        )
    )
    new=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("CONFIGURACIONES",color="WHITE",size=32,font_family="Berlin Sans FB")
                        ]
                    ),
                    ft.Row(
                        [
                            usr_c
                        ]
                    )
                ]
            )
        )
    )