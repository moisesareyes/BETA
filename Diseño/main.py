import flet as ft

def main (page: ft.Page):
    def on_click_main(e):
        def redr(sec):
            page.go="/src/inicio.py"
        redr(1)
    page.bgcolor="#c4394d"
    btn_sesion=ft.CupertinoButton(content=ft.Text("INICIAR SESION",color="BLACK",font_family="Berlin Sans FB"),bgcolor="#ffe3e8",width=300,on_click=on_click_main)
    btn_reg=ft.CupertinoButton(content=ft.Text("REGISTRO",color="BLACK",font_family="Berlin Sans FB"),bgcolor="#ffe3e8",width=300,on_click=on_click_main)
    page.add(
        ft.Column(
            [
                ft.Column(
                    [
                        ft.Container(height=200)
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("LOGO",color="WHITE",size=32,font_family="Berlin Sans FB")
                    ],alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        btn_sesion
                    ],alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        btn_reg
                    ],alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Column(
                    [
                        ft.Container(height=50)
                    ]
                ),
                ft.Row(
                    [
                        ft.IconButton(icon=ft.icons.COLOR_LENS_OUTLINED, icon_color="BLACK",bgcolor="#ffe3e8",icon_size=32)
                    ],alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )
ft.app(main)