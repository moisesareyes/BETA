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
def index (page:ft.Page,user):
    sql=f"SELECT `id`, `poseedor`, `tipo`, `cantidad`, `billeteraID`, `act` FROM `billetera` WHERE`poseedor`='{user}'"
    crs=mydb.cursor()
    crs.execute(sql)
    inf_bill=crs.fetchall()
    sql=f"SELECT `ID`, `UserID`, `Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`, `Reg` FROM `usuario` WHERE `UserID`='{user}'"
    crs.execute(sql)
    inf_usr=crs.fetchone()
    print(f"{inf_bill} {inf_usr}")
    carrousel = ft.Row(expand=1, wrap=False, scroll="always",alignment=ft.MainAxisAlignment.CENTER)
    page.scroll='always'
    for bill in inf_bill:
            carrousel.controls.append(
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    border=ft.border.all(3,"BLACK"),
                    bgcolor="#c4394d",
                    height=140,
                    width=325,
                    content=(
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Row(
                                            [
                                                ft.Text(value=f"{inf_usr[4]}",color="WHITE",size=20,font_family="Berlin Sans FB"),
                                            ],alignment=ft.MainAxisAlignment.START
                                            ),
                                    ]
                                ),
                                ft.Row(
                                    [
                                        ft.Text(value=f"{bill[3]} {bill[2]}",color="WHITE",size=24,font_family="Berlin Sans FB"),
                                    ],alignment=ft.MainAxisAlignment.CENTER
                                ),
                                ft.Row(
                                    [
                                        ft.Text(value=f"Ultima Actualización: {bill[5]}",color="WHITE",size=12,font_family="Berlin Sans FB")
                                    ],alignment=ft.MainAxisAlignment.CENTER
                                )
                            ]
                        )
                    )
                )
            )
    new=ft.Container(
          content=(
                ft.Row(
                      [
                            carrousel
                      ],alignment=ft.MainAxisAlignment.CENTER
                )
          )
    )
    page.horizontal_alignment =  "center"
    if not user=="PEE-35141":
        return new
    else:pass