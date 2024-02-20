import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"
    btn_sesion=ft.CupertinoButton(content=ft.Text("INICIAR SESION",color="BLACK",font_family="Berlin Sans FB"),bgcolor="#ffe3e8",width=300)
    btn_reg=ft.CupertinoButton(content=ft.Text("REGISTRO",color="BLACK",font_family="Berlin Sans FB"),bgcolor="#ffe3e8",width=300)
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/Prince")),
                    ],
                )
            )
  
        page.update()
        if page.route=="/Prince":
            page.views.append(
                ft.View(
                    "/Prince",
                    [
                        ft.AppBar(title=ft.Text("MARICO"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Column(
                            [
                                ft.Container(height=200,bgcolor="WHITE"),
                                btn_reg,
                                btn_sesion
                            ]
                        ),
                    ]
                )
            )
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)