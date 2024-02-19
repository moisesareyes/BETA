import flet as ft

def sesion (page:ft.Page):
    page.bgcolor="#c4394d"
    inp_pass=ft.TextField(hint_text="Contraseña",label="Contraseña",border_color="#A51C30",bgcolor="#fff2f4",password=True,icon=ft.icons.PEOPLE_ALT)
    inp_usr=ft.TextField(hint_text="Nombre de usuario",label="Nombre de usuario",border_color="#A51C30",bgcolor="#fff2f4",icon=ft.icons.KEY)
    titt=ft.Text(value="INICIO DE SESION",color="WHITE",size=32,font_family="Berlin Sans FB")
    btn=ft.CupertinoButton(content=ft.Text("INICIAR SESION",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#ff0025")
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
                        titt
                    ],alignment=ft.MainAxisAlignment.CENTER
                )
                ,
                ft.Row(
                    [
                        inp_usr
                    ],alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        inp_pass
                    ],alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        btn
                    ],alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Text(value="¿CONTRASEÑA OLVIDA?",color="WHITE",size=12,font_family="Berlin Sans FB")
                    ],alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )
ft.app(sesion)