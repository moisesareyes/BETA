import flet as ft

def nav_bar(page,ft=ft):
    navbar = ft.BottomAppBar(
        bgcolor="#c4394d",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.WORK_HISTORY, icon_color=ft.colors.WHITE,on_click=lambda _: page.go('/history')),
                ft.IconButton(icon=ft.icons.HOME,on_click=lambda _: page.go('/')),
                ft.IconButton(icon=ft.icons.KEYBOARD_DOUBLE_ARROW_UP_OUTLINED, icon_color=ft.colors.WHITE,on_click=lambda _: page.go('/transf')),
                ft.IconButton(icon=ft.icons.TRENDING_UP_OUTLINED,icon_color="WHITE",on_click=lambda _: page.go('/retiro')),
                ft.IconButton(icon=ft.icons.MENU_OPEN_SHARP,icon_color="WHITE",on_click=lambda _: page.go('/config'))
            ],alignment=ft.MainAxisAlignment.CENTER
        )
    )
    return navbar