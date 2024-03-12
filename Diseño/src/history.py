import flet as ft
import mysql.connector 
from user_controls.navbar import nav_bar
from user_controls.appbar import app_bar
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
def history(page:ft.Page,user,theme):
    crs=mydb.cursor()
    sql=f"SELECT * FROM `historial` WHERE `servidor`='{user}' OR `recep`='{user}'"
    crs.execute(sql)
    inf_history=crs.fetchall()
    page.scroll='always'
    recargas = ft.Row(expand=1, wrap=False, scroll="always",alignment=ft.MainAxisAlignment.CENTER)
    converse = ft.Row(expand=1, wrap=False, scroll="always",alignment=ft.MainAxisAlignment.CENTER)
    transf = ft.Row(expand=1, wrap=False, scroll="always",alignment=ft.MainAxisAlignment.CENTER)
    transftousr = ft.Row(expand=1, wrap=False, scroll="always",alignment=ft.MainAxisAlignment.CENTER)
    print(inf_history)
    for hist in inf_history:
        print(hist)
        if hist[3]=="converse":
            converse.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.PRICE_CHANGE,color="WHITE"),
                                    title=ft.Text(f"CONVERSION {hist[4]}",color="WHITE",size=18,font_family="Berlin Sans FB"),
                                    subtitle=ft.Text(f"F: {hist[9]} Cantidad: {hist[6]}",color="WHITE",size=12,font_family="Berlin Sans FB"),
                                ),
                                ft.Row(
                                    [ft.TextButton(content=ft.Text("Ocultar",color="WHITE"))],alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                    width=325,
                    padding=10,
                    bgcolor=f"{theme['maincolor']}"
                    )
                )
            )
        elif hist[3]=="Recarga":
            recargas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.KEYBOARD_DOUBLE_ARROW_UP_OUTLINED,color="WHITE"),
                                    title=ft.Text(f"RECARGA",color="WHITE",size=18,font_family="Berlin Sans FB"),
                                    subtitle=ft.Text(f"F:{hist[9]} Cantidad: {hist[6]}",color="WHITE",size=12,font_family="Berlin Sans FB"),
                                ),
                                ft.Row(
                                    [ft.TextButton(content=ft.Text("Ocultar",color="WHITE"))],alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                    width=325,
                    padding=10,
                    bgcolor=f"{theme['maincolor']}"
                    )
                )
            )
        elif hist[3]=="transferencia" and hist[2]==user:
            sql=f"SELECT `User_name` FROM `usuario` WHERE `UserID`='{user}'"
            crs.execute(sql)
            infusr=crs.fetchone()
            transftousr.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.COMPARE_ARROWS,color="WHITE"),
                                    title=ft.Text(f"TRANSFERENCIA A USUARIO",color="WHITE",size=18,font_family="Berlin Sans FB"),
                                    subtitle=ft.Text(f"F:{hist[9]} - Cantidad: {hist[6]} - De: {infusr[0][0]}",color="WHITE",size=12,font_family="Berlin Sans FB"),
                                ),
                                ft.Row(
                                    [ft.TextButton(content=ft.Text("Ocultar",color="WHITE"))],alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                    width=325,
                    padding=10,
                    bgcolor=f"{theme['maincolor']}"
                    )
                )
            )
        elif hist[3]=="transferencia":
            sql=f"SELECT `User_name` FROM `usuario` WHERE `UserID`='{hist[2]}'"
            crs.execute(sql)
            infusr=crs.fetchall()
            transf.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.COMPARE_ARROWS,color="WHITE"),
                                    title=ft.Text(f"TRANSFERENCIA DEL USUARIO",color="WHITE",size=18,font_family="Berlin Sans FB"),
                                    subtitle=ft.Text(f"F:{hist[9]} - Cantidad: {hist[6]} - Para: {infusr[0][0]}",color="WHITE",size=12,font_family="Berlin Sans FB"),
                                ),
                                ft.Row(
                                    [ft.TextButton(content=ft.Text("Ocultar",color="WHITE"))],alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                    width=325,
                    padding=10,
                    bgcolor=f"{theme['maincolor']}"
                    )
                )
            )
    new=(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Recargas",color="BLACK",size=21,font_family="Berlin Sans FB")
                    ]
                ),
                ft.Row(
                    [
                        recargas
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("Conversiones",color="BLACK",size=21,font_family="Berlin Sans FB")
                    ]
                ),
                ft.Row(
                    [
                        converse
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("Transferencia del usuario",color="BLACK",size=21,font_family="Berlin Sans FB")
                    ]
                ),
                ft.Row(
                    [
                        transf
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("Tansferencia al usuario",color="BLACK",size=21,font_family="Berlin Sans FB")
                    ]
                ),
                ft.Row(
                    [
                        transftousr
                    ]
                )
            ]
        )
    )
    if not user=="PEE-35141":
        return new
    else:pass