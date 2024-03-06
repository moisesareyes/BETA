import flet as ft
import mysql.connector 

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
def loginp(page:ft.Page):
    crs=mydb.cursor()
    def on_click_lgoin(e):
        def comp(user,passw,titt):
            ver=list()
            if not user.value:
                user.bgcolor="#ff0000"
                user.hint_text="OBLIGATORIO"
                page.update()
                ver.append(False)
            else:ver.append(True)
            if not passw.value:
                passw.hint_text="OBLIGATORIO"
                passw.border_color="#ff0000"
                page.update()
                ver.append(False)
            else:ver.append(True)
            verificacion=all(ver)
            return verificacion
        varr=comp(inp_usr,inp_pass,titt)
        if varr==True:
            sql=f"SELECT `UserID`,`User_name`, `Email`, `Pass`, `Tlf` FROM `usuario` WHERE `User_name`='{inp_usr.value}' OR `Email`='{inp_usr.value}' OR `Tlf`='{inp_usr.value}'"
            crs.execute(sql)
            newval=crs.fetchone()
            print(newval)
            if newval[3]==inp_pass.value:
                titt.color="#32a852"
                page.update()
                global user
                user=newval[0]
            else:
                inp_usr.label="CONTRASEÑA INCORRECTA"
                inp_usr.hint_text="CONTRASEÑA INCORRECTA"
                inp_usr.border_color="#ff0000"
                page.update()
        else:
            titt.value="ERROR"
            page.update()
    inp_pass=ft.TextField(hint_text="Contraseña",label="Contraseña",border_color="#A51C30",bgcolor="#fff2f4",password=True,icon=ft.icons.PEOPLE_ALT)
    inp_usr=ft.TextField(hint_text="Nombre de usuario",label="Nombre de usuario",border_color="#A51C30",bgcolor="#fff2f4",icon=ft.icons.KEY)
    titt=ft.Text(value="INICIO DE SESION",color="WHITE",size=32,font_family="Berlin Sans FB")
    btn=ft.ElevatedButton(content=ft.Text("INICIAR SESION",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#ff0025",width=300,on_click=on_click_lgoin)
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
        )
    )
    page.add(new)
ft.app(loginp)