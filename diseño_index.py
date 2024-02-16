import flet as ft
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
user="ZRO-42111"
def index (page: ft.Page):
    def on_click_button_containter(e):
        print("Shaki")
    sql="SELECT `id`, `poseedor`, `tipo`, `cantidad`, `billeteraID`, `act` FROM `billetera` WHERE`poseedor`='ZRO-42111'"
    crs=mydb.cursor()
    crs.execute(sql)
    inf_bill=crs.fetchall()
    sql=f"SELECT `ID`, `UserID`, `Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`, `Reg` FROM `usuario` WHERE `UserID`='{user}'"
    crs.execute(sql)
    inf_usr=crs.fetchone()
    print(f"{inf_bill} {inf_usr}")
    page.bgcolor="#ffe3e8"
    page.add(ft.Container(height=20,bgcolor="#ffe3e8"))
    for bill in inf_bill:
        ind=ft.Container(
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(3,"BLACK"),
            bgcolor="#c4394d",
            height=140,
            width=1280,
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
                                ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_NEW_SHARP,icon_color="WHITE"),
                                ft.Icon(ft.icons.HORIZONTAL_RULE_SHARP,color="WHITE"),
                                ft.IconButton(icon=ft.icons.NAVIGATE_NEXT,icon_color="WHITE"),
                            ],alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ]
                )
            )
        )
        page.add(ind)
    ops=ft.Container(
        border_radius=ft.border_radius.all(80),
        bgcolor="#c4394d",
        height=48,
        width=1280,
        content=(
            ft.Row(
                [
                    ft.IconButton(icon=ft.icons.EXIT_TO_APP_SHARP,icon_color="WHITE"),
                    ft.IconButton(icon=ft.icons.ADD_BOX_ROUNDED,icon_color="WHITE"),
                    ft.IconButton(icon=ft.icons.UPDATE,icon_color="WHITE")
                ],alignment=ft.MainAxisAlignment.CENTER
            )
        )
    )
    page.add(ops)
ft.app(index)