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
    def on_click_button(e):
        print("Shaki")
    
    page.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text("LOGOOGOGOO",color="WHITE"),
        center_title=True,
        bgcolor="#c4394d",
    )
    sql=f"SELECT `id`, `poseedor`, `tipo`, `cantidad`, `billeteraID`, `act` FROM `billetera` WHERE`poseedor`='{user}'"
    crs=mydb.cursor()
    crs.execute(sql)
    inf_bill=crs.fetchall()
    sql=f"SELECT `ID`, `UserID`, `Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`, `Reg` FROM `usuario` WHERE `UserID`='{user}'"
    crs.execute(sql)
    inf_usr=crs.fetchone()
    print(f"{inf_bill} {inf_usr}")
    page.bgcolor="#ffe3e8"
    carrousel = ft.Row(expand=1, wrap=False, scroll="always",alignment=ft.MainAxisAlignment.CENTER)
    if inf_bill:
        for bill in inf_bill:
            carrousel.controls.append(
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    border=ft.border.all(3,"BLACK"),
                    bgcolor="#c4394d",
                    height=140,
                    width=300,
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
    carrousel.controls.append(
        ft.Container(
            border_radius=ft.border_radius.all(10),
            border=ft.border.all(3,"BLACK"),
            bgcolor="#c4394d",
            height=140,
            width=300,
            content=(
                ft.IconButton(icon=ft.icons.ADD_BOX_ROUNDED,icon_size=40,icon_color="WHITE")
            )
        )
    )
    page.add(carrousel)
    page.horizontal_alignment = page.vertical_alignment = "center"

    mybar = ft.BottomAppBar(
        bgcolor="#c4394d",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.EXIT_TO_APP, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.HOME, icon_color=ft.colors.WHITE,bgcolor="#ff6178"),
                ft.IconButton(icon=ft.icons.KEYBOARD_DOUBLE_ARROW_UP_OUTLINED, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.TRENDING_UP_OUTLINED,icon_color="WHITE"),
                ft.IconButton(icon=ft.icons.EXIT_TO_APP, icon_color=ft.colors.WHITE),
            ],alignment=ft.MainAxisAlignment.CENTER
        ),
    )
    page.add(mybar)
ft.app(index)