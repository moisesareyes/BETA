import flet as ft
from src.fixes.findex import indexforuser
from src.fixes.fixindex2 import indexforbilletera
def index (page:ft.Page,user,theme):
    inf_bill=indexforbilletera(user)
    inf_usr=indexforuser(user)
    carrousel = ft.Row(expand=1, wrap=False, scroll="always",alignment=ft.MainAxisAlignment.CENTER)
    page.scroll='always'
    for bill in inf_bill:
            carrousel.controls.append(
                ft.Container(
                    border_radius=ft.border_radius.all(10),
                    border=ft.border.all(3,"BLACK"),
                    bgcolor=f"{theme['maincolor']}",
                    height=140,
                    width=325,
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
    new=ft.Container(
          content=(
                ft.Row(
                      [
                            carrousel
                      ],alignment=ft.MainAxisAlignment.CENTER
                )
          )
    )
    page.horizontal_alignment =  "center"
    if not user=="PEE-35141":
        return new
    else:pass