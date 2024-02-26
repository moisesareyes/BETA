import flet as ft

def app_bar(page,ft=ft):
    img=ft.Image(
        height=100,
        src=f"/images/banner.png",
        fit=ft.ImageFit.CONTAIN
    )
    ApB = ft.AppBar(
        toolbar_height=65,
        leading_width=40,
        title=img,
        center_title=True,
        bgcolor="#c4394d",
    )
    return ApB