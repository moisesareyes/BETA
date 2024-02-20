import flet as ft
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
user="ZRO-42111"
def transf (page: ft.Page):
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
    dd_pref = ft.Dropdown(
        label="PREFERENCIA DE USUARIO",
        bgcolor="WHITE",
        width=300,
        options=[
            ft.dropdown.Option("USUARIO"),
            ft.dropdown.Option("TELEFONO"),
            ft.dropdown.Option("CORREO")
        ],
    )
    dd_type = ft.Dropdown(
        label="TIPO DE CAMBIO",
        bgcolor="WHITE",
        width=300,
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("Bs. D"),
        ],
    )
    page.bgcolor="#ffe3e8"
    contacto=ft.TextField(label="CONTACTO",hint_text="CONTACTO",bgcolor="#ffe3e8",width=300)
    monto=ft.TextField(label="MONTO",hint_text="MONTO",input_filter=ft.NumbersOnlyInputFilter(),color="#ffe3e8",width=300)
    cambio=ft.CupertinoButton(content=ft.Text("ACEPTAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300)
    maxi=ft.TextField(label="MONTO MAXIMO",hint_text="MONTO MAXIMO",bgcolor="#ffe3e8",width=300,disabled=True,value=200)
    new=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("CONVERSION",color="BLACK",size=32,font_family="Berlin Sans FB")
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            dd_pref
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            dd_type
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            contacto
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            monto
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            maxi
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            cambio
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.Text("MINIMO 5 USD AL CAMBIO",color="BLACK",size=12,font_family="Berlin Sans FB")
                        ],alignment=ft.MainAxisAlignment.CENTER
                    )
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
ft.app(transf)