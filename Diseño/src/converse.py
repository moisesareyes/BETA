import flet as ft
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
bcv=36.29
user="ZRO-42111"
def converse (page: ft.Page):
    crs=mydb.cursor()
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='USD'"
    crs.execute(sql)
    inf=crs.fetchone()
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
    crs.execute(sql)
    inf_bs=crs.fetchone()
    print(inf)
    def on_change_converse(e):
        def op(method,new_cono,old_cono,show):
            if method.value=="USD to Bs.D":
                old_max=inf[3]
                old_cono.value=f"{old_max}"
                if new_cono.value:
                    temp=int(new_cono.value)*bcv
                    show.value=f"Cambio: {temp} Bs. D"
                else: show.value=f"Cambio: "
            page.update()
            if method.value=="Bs.D to USD":
                old_max=inf_bs[3]/bcv
                old_cono.value=f"{old_max}"
                if new_cono.value:
                    temp=int(new_cono.value)
                    show.value=f"Cambio: {temp} $"
                else: show.value=f"Cambio: "
            page.update()
        op(dd_method,monto,maxi,newcambio)
    def on_click_converse(e):
        def comp(method,monto,maxi):
            ver=list()
            if not method.value:
                method.hint_text="OBLIGATORIO"
                method.border_color="#ff0000"
                page.update()
                ver.append(False)
            if not monto.value:
                monto.hint_text="OBLIGATORIO"
                monto.border_color="#ff0000"
                page.update()
                ver.append(False)
            if monto.value:
                if int(monto.value)>float(maxi.value) or 5>int(monto.value):
                    ver.append(False)
                else:ver.append(True)
            return ver
        def converse(method,cambio):
            if method.value=="USD to Bs.D":
                new_old=inf[3]-int(cambio.value)
                new=inf_bs[3]+int(cambio.value)*bcv
                sql=f"UPDATE `billetera` SET `cantidad`={new_old},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{user}' AND `tipo`='USD'"
                sql2=f"UPDATE `billetera` SET `cantidad`={new},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
                crs.execute(sql)
                crs.execute(sql2)
                mydb.commit()
            if method.value=="Bs.D to USD":
                new_old=inf_bs[3]-int(cambio.value)/bcv
                new=inf[3]+int(cambio.value)
                sql=f"UPDATE `billetera` SET `cantidad`={new_old},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{user}' AND `tipo`='USD'"
                sql2=f"UPDATE `billetera` SET `cantidad`={new},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
                crs.execute(sql)
                crs.execute(sql2)
                mydb.commit()
        ver=comp(dd_method,monto,maxi)
        verificacion=all(ver)
        if verificacion==True:
            converse(dd_method,monto)
            monto.value=""
            titl.value="Cambio Exitoso"
            titl.color="#60d147"
            page.update()
        else: pass
        print(ver)
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
    dd_method = ft.Dropdown(
        on_change=on_change_converse,
        bgcolor="WHITE",
        width=300,
        options=[
            ft.dropdown.Option("USD to Bs.D"),
            ft.dropdown.Option("Bs.D to USD")
        ],
    )
    page.bgcolor="#ffe3e8"
    monto=ft.TextField(label="MONTO $",hint_text="MONTO$$$",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,on_change=on_change_converse)
    cambio=ft.CupertinoButton(content=ft.Text("CAMBIAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300,on_click=on_click_converse)
    maxi=ft.TextField(label="MONTO MAXIMO",hint_text="MONTO MAXIMO",bgcolor="#ffe3e8",color="BLACK",width=300,disabled=True)
    titl=ft.Text("CONVERSION",color="BLACK",size=32,font_family="Berlin Sans FB")
    newcambio=ft.Text("Cambio: ",color="BLACK",size=16,font_family="Berlin Sans FB")
    new=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Row(
                        [
                            titl
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            newcambio
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            dd_method
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
ft.app(converse)