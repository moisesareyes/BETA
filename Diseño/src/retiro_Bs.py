import flet as ft
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
user="ZRO-42111"
def retiro_bs (page: ft.Page):
    crs=mydb.cursor()
    img=ft.Image(
        width=256,
        src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b2a0d1ca-699a-4c14-8a0f-f7c09f0804fb/dgx3mr5-c424fb06-c476-4e14-b90c-3f9dfecf3a78.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2IyYTBkMWNhLTY5OWEtNGMxNC04YTBmLWY3YzA5ZjA4MDRmYlwvZGd4M21yNS1jNDI0ZmIwNi1jNDc2LTRlMTQtYjkwYy0zZjlkZmVjZjNhNzgucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.0R8sHJFh-v6fG5187eWWUt0QGkE4lPTdtBWwuhcuPD4",
        fit=ft.ImageFit.CONTAIN
    )
    page.appbar = ft.AppBar(
        leading_width=40,
        title=img,
        center_title=True,
        bgcolor="#c4394d",
    )
    page.bgcolor="#ffe3e8"
    rec=ft.CupertinoButton(content=ft.Text("REGISTRAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300)
    doc=ft.TextField(label="Cedula",hint_text="Cedula",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
    cant=ft.TextField(label="Cantidad",hint_text="Cantidad",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
    tlf=ft.TextField(label="Telefono",hint_text="Telefono",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,disabled=True)
    tit=ft.Text("DATOS DE RETIRO",color="BLACK",font_family="Berlin Sans FB",size=32)
    dd_banco = ft.Dropdown(
        label="BANCO",
        bgcolor="#c4394d",
        width=300,
        options=[
            
            ft.dropdown.Option("0102 Banco de Venezuela, S.A.C.A."),
            ft.dropdown.Option("0104 Venezolano de Crédito"),
            ft.dropdown.Option("0105 Mercantil"),
            ft.dropdown.Option("0108 Provincial"),
            ft.dropdown.Option("0114 Bancaribe"),
            ft.dropdown.Option("0115 Exterior"),
            ft.dropdown.Option("0116 Occidental de Descuento"),
            ft.dropdown.Option("0128 Banco Caroní"),
            ft.dropdown.Option("0134 Banesco"),
            ft.dropdown.Option("0138 Banco Plaza"),
            ft.dropdown.Option("0151 BFC Banco Fondo Común"),
            ft.dropdown.Option("0156 100% Banco"),
            ft.dropdown.Option("0157 Del Sur."),
            ft.dropdown.Option("0166 Banco Agrícola de Venezuela "),
            ft.dropdown.Option("0168 Bancrecer"),
            ft.dropdown.Option("0169 Mi Banco"),
            ft.dropdown.Option("0171 Banco Activo"),
            ft.dropdown.Option("0172 Bancamiga"),
            ft.dropdown.Option("0174 Banplus"),
            ft.dropdown.Option("0175 Bicentenario del Pueblo"),
            ft.dropdown.Option("0177 Banfanb"),
            ft.dropdown.Option("0191 BNC Nacional de Crédito")
        ],
    )
    new=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Row(
                        [
                            tit
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            dd_banco
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            doc
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            tlf
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            cant
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            rec
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                ]
            )
        )
    )
    page.add(new)
    mybar = ft.BottomAppBar(
        bgcolor="#c4394d",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.REFRESH, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.HOME, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.KEYBOARD_DOUBLE_ARROW_UP_OUTLINED, icon_color=ft.colors.WHITE,bgcolor="#ff6178"),
                ft.IconButton(icon=ft.icons.TRENDING_UP_OUTLINED,icon_color="WHITE"),
                ft.IconButton(icon=ft.icons.MENU_OPEN_SHARP,icon_color="WHITE"),
                ft.IconButton(icon=ft.icons.EXIT_TO_APP, icon_color=ft.colors.WHITE)
            ],alignment=ft.MainAxisAlignment.CENTER
        ),
    )
    page.add(mybar)
ft.app(retiro_bs)