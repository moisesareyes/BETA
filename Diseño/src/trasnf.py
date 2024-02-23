import flet as ft
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
user="Eai-47325"
def transf (page: ft.Page):
    crs=mydb.cursor()
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='USD'"
    crs.execute(sql)
    inf=crs.fetchone()
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='Bs.D'"
    crs.execute(sql)
    inf_bs=crs.fetchone()
    def on_change_tranf(e):
        def comp(pref,type,contacto,monto,maxi):
            if pref.value=="USUARIO":
                contacto.input_filter=ft.InputFilter(allow=False, regex_string="[ ]" , replacement_string="")
                contacto.disabled=False
                page.update()
            if pref.value=="TELEFONO":
                contacto.value=""
                contacto.input_filter=ft.InputFilter(allow=True, regex_string="[0-9]", replacement_string="")
                contacto.disabled=False
                page.update()
            if pref.value=="CORREO":
                contacto.input_filter=ft.InputFilter(allow=False, regex_string="[ ]" , replacement_string="")
                contacto.disabled=False
                page.update()
            if not pref.value:
                contacto.disabled=True
                page.update()
            if type.value=="Bs.D":
                maxi.value=inf_bs[3]
                monto.disabled=False
                page.update()
            if type.value=="USD":
                maxi.value=inf[3]
                monto.disabled=False
                page.update()
        comp(dd_pref,dd_type,contacto,monto,maxi)
    def on_click_tranf(e):
        def comp(pref,type,contacto,monto,maxi,error,titl):
            ver=list()
            if not pref.value:
                pref.hint_text="OBLIGATORIO"
                pref.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not type.value:
                type.hint_text="OBLIGATORIO"
                type.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not contacto.value:
                contacto.hint_text="OBLIGATORIO"
                contacto.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not monto.value:
                monto.hint_text="OBLIGATORIO"
                monto.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            verificacion=all(ver)
            if verificacion==True:
                sql=f"SELECT `UserID` FROM `usuario` WHERE `User_name`='{contacto.value}' OR `Email`='{contacto.value}' OR `Tlf`='{contacto.value}'"
                crs.execute(sql)
                id=crs.fetchone()
                print(id)
                if not id:
                    contacto.label=f"{pref.value} NO EXISTE"
                    contacto.hint_text=f"{pref.value} NO EXISTE"
                    contacto.border_color="#ff0000"
                    page.update()
                elif id:
                    if int(monto.value)>int(maxi.value):
                        error.color="#ff0000"
                        page.update()
                    elif 5>int(monto.value):
                        error.color="#ff0000"
                        page.update()
                    else:
                        sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{id[0]}' AND `tipo`='{type.value}'"
                        crs.execute(sql)
                        inf_rcp=crs.fetchone()
                        sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{user}' AND `tipo`='{type.value}'"
                        crs.execute(sql)
                        inf_usr=crs.fetchone()
                        new_to_rcp=inf_rcp[3]+int(monto.value)
                        new_to_usr=inf_usr[3]-int(monto.value)
                        sql=f"UPDATE `billetera` SET `cantidad`={new_to_rcp},`act`=CURRENT_TIMESTAMP WHERE `billeteraID`='{inf_rcp[4]}' "
                        sql2=f"UPDATE `billetera` SET `cantidad`={new_to_usr},`act`=CURRENT_TIMESTAMP WHERE `billeteraID`='{inf_usr[4]}' "
                        crs.execute(sql)
                        crs.execute(sql2)
                        monto.disabled=True
                        contacto.disabled=True
                        type.disabled=True
                        pref.disabled=True
                        titl.value="TRANSACCION COMPLETA"
                        titl.color="#60d147"
                        page.update()
                        mydb.commit()
            else: print("ERROR")
        comp(dd_pref,dd_type,contacto,monto,maxi,error,titl)
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
    dd_pref = ft.Dropdown(
        on_change=on_change_tranf,
        label="PREFERENCIA DE USUARIO",
        bgcolor="WHITE",
        width=300,
        options=[
            ft.dropdown.Option("USUARIO"),
            ft.dropdown.Option("TELEFONO"),
            ft.dropdown.Option("CORREO")
        ],
    )
    dd_type = ft.Dropdown(
        on_change=on_change_tranf,
        label="TIPO DE CAMBIO",
        bgcolor="WHITE",
        width=300,
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("Bs.D"),
        ],
    )
    page.bgcolor="#ffe3e8"
    contacto=ft.TextField(label="CONTACTO",hint_text="CONTACTO",bgcolor="#ffe3e8",width=300,disabled=True)
    monto=ft.TextField(label="MONTO",hint_text="MONTO",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,disabled=True)
    cambio=ft.CupertinoButton(content=ft.Text("ACEPTAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300,on_click=on_click_tranf)
    maxi=ft.TextField(label="MONTO MAXIMO",hint_text="MONTO MAXIMO",bgcolor="#ffe3e8",width=300,disabled=True)
    error=ft.Text("MINIMO 5 USD AL CAMBIO",color="BLACK",size=12,font_family="Berlin Sans FB")
    titl=ft.Text("TRANSFERENCIA",color="BLACK",size=32,font_family="Berlin Sans FB")
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
                            dd_pref
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            dd_type
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            contacto
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
                            error
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
ft.app(transf)