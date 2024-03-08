import flet as ft
def indexforusr(page:ft.Page):
    titt=ft.Text(value="OPCION DE USUARIO",color="BLACK",size=32,font_family="Berlin Sans FB")
    btnop2=ft.ElevatedButton(content=ft.Text("REGISTRO DE USUARIO",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#ff0025",width=300,on_click=lambda _: page.go("/index/reg"))
    btn=ft.ElevatedButton(content=ft.Text("INICIAR SESION",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#ff0025",width=300,on_click=lambda _: page.go("/index/login"))
    new=( 
        ft.Container(
            content=(
                ft.Column([
                    ft.Row([ft.Image(height=100,src=f"/images/banner.png",fit=ft.ImageFit.CONTAIN)],alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row(
                        [
                            titt
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            btn
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            btnop2
                        ],alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
                )
            )
        )
    )
    return new