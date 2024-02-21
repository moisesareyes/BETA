import flet as ft
import mysql.connector
import datetime
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
user="ZRO-42111"
def recg (page: ft.Page):
    crs=mydb.cursor()
    def on_click_reg(e):
        def comp(fecha,type,datebtn,method,doc,ref,usuario,tlf,cant,tit):
            ver=list()
            if not fecha.value:
                print(datebtn)
                datebtn.bgcolor="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not type.value:
                print(type)
                type.hint_text="OBLIGATORIO"
                type.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not method.value:
                method.hint_text="OBLIGATORIO"
                method.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not doc.value:
                doc.hint_text="OBLIGATORIO"
                doc.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not ref.value:
                ref.hint_text="OBLIGATORIO"
                ref.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not cant.value:
                cant.hint_text="OBLIGATORIO"
                cant.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if tlf.disabled==False:
                if not tlf.value:
                    tlf.hint_text="OBLIGATORIO"
                    tlf.border_color="#ff0000"
                    page.update()
                    telef=tlf.value
                    ver.append(False)
                else:
                    ver.append(True)
            else:telef="Predeterminado"
            verificacion=all(ver)
            print(verificacion)
            if verificacion==True:
                if tlf.disabled==False:
                    new=(usuario,type.value,doc.value,method.value,tlf.value,cant.value,ref.value,"Pendiente",fecha.value)
                    sql="INSERT INTO `recarga`(`usuario`, `tipo`, `doc`, `formato`, `telefono`, `cantidad`,  `operacion`, `status`, `fecha_tra`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    crs.execute(sql,new)
                    mydb.commit()
                else:
                    new=(usuario,type.value,doc.value,method.value,cant.value,ref.value,"Pendiente",fecha.value)
                    sql="INSERT INTO `recarga`(`usuario`, `tipo`, `doc`, `formato`, `cantidad`,`operacion`, `status`, `fecha_tra`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    crs.execute(sql,new)
                    mydb.commit()
            type.value=""
            doc.value=""
            method.value=""
            cant.value=""
            ref.value=""
            fecha.value=""
            tit.value="RECARGA REGISTRADA"
            tit.color="#60d147"
            page.update()
        comp(date_picker,dd_type,date_button,dd_method,doc,ref,user,tlf,cant,tit)
    def date_picker_dismissed(e):
        print(f"Date picker dismissed, value is {date_picker.value}")
    def change_date(e):
        print(f"Date picker changed, value is {date_picker.value}")
    def on_change_dis(e):
        def dis(type,method,tlf):
            if type.value=="USD":
                method.disabled=False
                method.options=[
                    ft.dropdown.Option("PAYPAL")
                ]
                page.update()
            if type.value=="Bs.D":
                method.disabled=False
                method.options=[
                    ft.dropdown.Option("TRANSFERENCIA"),
                    ft.dropdown.Option("PAGO MOVIL")
                ]
                page.update()
            if not type.value:
                method.disabled=True
            if method.value=='PAGO MOVIL':
                tlf.disabled=False
                page.update()
            if not method.value=='PAGO MOVIL':
                tlf.disabled=True
                page.update()
            print(method)
        dis(dd_type,dd_method,tlf)
    date_picker = ft.DatePicker(
        on_change=change_date,
        on_dismiss=date_picker_dismissed,
        first_date=datetime.datetime.today()
    )

    page.overlay.append(date_picker)

    date_button = ft.IconButton(
        bgcolor="#c4394d",
        icon_color="WHITE",
        icon_size=32,
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )

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
    page.bgcolor="#ffe3e8"
    rec=ft.CupertinoButton(content=ft.Text("REGISTRAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#c4394d",width=300,on_click=on_click_reg)
    doc=ft.TextField(label="Cedula",hint_text="Cedula",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
    ref=ft.TextField(label="Referencia",hint_text="Referencia",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
    cant=ft.TextField(label="Cantidad",hint_text="Cantidad",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300)
    tlf=ft.TextField(label="Telefono",hint_text="Telefono",input_filter=ft.NumbersOnlyInputFilter(),color="BLACK",width=300,disabled=True)
    tit=ft.Text("REGISTRO DE RECARGA",color="BLACK",font_family="Berlin Sans FB",size=32)
    dd_type = ft.Dropdown(
        on_change=on_change_dis,
        label="TIPO DE RECARGA",
        bgcolor="#c4394d",
        width=300,
        options=[
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("Bs.D")
        ],
    )
    dd_method = ft.Dropdown(
        on_change=on_change_dis,
        disabled=True,
        label="METODO DE RECARGA",
        bgcolor="WHITE",
        width=300,
    )
    new=ft.Container(
        content=(
            ft.Column(
                [
                    ft.Row(
                        [
                            tit
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            dd_type
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            dd_method
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            doc
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ref
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            tlf
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            cant
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            date_button
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            rec
                        ],alignment=ft.MainAxisAlignment.CENTER
                    ),
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
ft.app(recg)