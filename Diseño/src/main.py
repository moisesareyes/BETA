import flet as ft
class main(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page=page
    def build (self):
        btn_sesion=ft.CupertinoButton(content=ft.Text("INICIAR SESION",color="BLACK",font_family="Berlin Sans FB"),bgcolor="#ffe3e8",on_click= lambda _:self.page.go('/1'),width=300)
        btn_reg=ft.CupertinoButton(content=ft.Text("REGISTRO",color="BLACK",font_family="Berlin Sans FB"),bgcolor="#ffe3e8",width=300)
        return ft.Column(
            controls=[
                ft.Container(
                    height=1080,
                     width=1920,
                     bgcolor="#c4394d",
                     content=(
                         ft.Column(
                             [
                                 ft.Column(
                                     [
                                         ft.Container(height=150)
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
                )
            ]
        )
