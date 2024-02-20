import flet as ft
import mysql.connector
import sys
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
def reg_user(page: ft.Page):
    page.bgcolor="#c4394d"
    ft.border_radius.all(0)
    def on_click_reg(e):
        def comp(para,metro):
            cursor1=mydb.cursor()
            sql=f"SELECT `{para}` FROM `usuario` WHERE `{para}`='{metro.value}'"
            cursor1.execute(sql)
            myresult = cursor1.fetchone()
            if myresult:
                metro.label="EN USO"
                metro.hint_text="LLENAR CAMPO"
                metro.border_color="#ffffff"
                metro.color="#ffffff"
                metro.bgcolor="#ff0000"
                page.update()
                return False
            else:
                return True
        def contado(contar,long):
            testC=len(long.value)
            if testC<contar:
                long.label=f"MINIMO {contar} CARACTERES"
                long.hint_text=f"MINIMO {contar} CARACTERES"
                long.color="#ffffff"
                long.bgcolor="#ff0000"
                page.update()
                return False
            else: return True
        def char(ctr):
            nums = [caracter.isdigit() for caracter in ctr.value]
            strs= [caracter.isalpha() for caracter in ctr.value]
            mayus= [caracter.isupper() for caracter in ctr.value]
            minus= [caracter.islower() for caracter in ctr.value]
            if any(nums) is False or any(strs) is False or any(mayus) is False or any(minus) is False:
                ctr.label=f"Utilice mayúsculas, minúsculas, números"
                ctr.hint_text=f"Utilice mayúsculas, minúsculas, números"
                ctr.color="#ffffff"
                ctr.bgcolor="#ff0000"
                page.update()
                return False
            else: return True
        def repeat(eat,rep):
            if rep.value==eat.value:
                return True
            else:
                rep.label="LAS CONTRASEÑAS DEBEN SER IGUALES"
                rep.hint_text="LLENAR CAMPO"
                rep.border_color="#ffffff"
                rep.color="#ffffff"
                rep.bgcolor="#ff0000"
                page.update()
                return False
        def verificacion(inpusr,inpnom,inpll,inpmail,inptlf,inpass,inpassword,titulo):
            def adv(var):
                var.label="LLENAR CAMPO"
                var.border_color="#ffffff"
                var.color="#ffffff"
                var.bgcolor="#ff0000"
                var.hint_text="LLENAR CAMPO"
                page.update()
            if inpusr.value=="":
                adv('inpusr')
            elif inpnom.value=="":
                adv('inpnom')
            elif inpll.value=="":
                adv('inpll')
            elif inpmail.value=="":
                adv('inpmail')
            elif inptlf.value=="":
                adv('inptlf')
            elif inpass.value=="":
                adv('inpass')
            elif inpassword.value=="":
                adv('inpassword')
            else: 
                ver1=comp("User_name",inpusr)
                ver2=comp("Email",inpmail)
                ver3=comp("Tlf",inptlf)
                ver4=contado(5,inpusr)
                ver5=contado(8,inptlf)
                ver6=contado(8,inp_pass)
                ver7=char(inpass)
                ver8=repeat(inpass,inpassword)
                verifi=(ver1,ver2,ver3,ver4,ver5,ver6,ver7,ver8)
                ver=all(verifi)
                print(f"Toal:{ver} des{verifi}")
                if ver==True:
                    inpname=inp_usr.value[0]+inp_usr.value[2]+inp_usr.value[4]+"-"+inp_tlf.value[2]+inp_tlf.value[3]+inp_tlf.value[-3]+inp_tlf.value[-2]+inp_tlf.value[-1]
                    inps=(inpname,inp_nombre.value,inp_apellido.value,inp_usr.value,inp_email.value,inp_pass.value,inp_tlf.value)
                    sql="INSERT INTO `usuario`(`UserID`,`Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    crs=mydb.cursor()
                    crs.execute(sql,inps)
                    mydb.commit()
                    mydb.close()
                else: 
                    print("Error")
                    titulo.text="ERRRORR"
        verificacion(inp_usr,inp_nombre,inp_apellido,inp_email,inp_tlf,inp_pass,inp_passrd,titulo)
    cortado=ft.Container(height=80,bgcolor="WHITE")
    titulo=ft.Text(value="REGISTRO DE USUARIO",color="WHITE",font_family="Berlin Sans FB",size=32)
    inp_usr = ft.TextField(hint_text="Usuario",label="Usuario",border_color="#A51C30",bgcolor="#fff2f4",width=300)
    inp_nombre=ft.TextField(hint_text="Nombre",label="Nombre",border_color="#A51C30",bgcolor="#fff2f4",width=150)
    inp_apellido=ft.TextField(hint_text="Apellido",label="Apellido",border_color="#A51C30",bgcolor="#fff2f4",width=150)
    inp_email=ft.TextField(hint_text="Email",label="Email",border_color="#A51C30",bgcolor="#fff2f4",width=150)
    inp_tlf=ft.TextField(hint_text="Telefono",label="Telefono",border_color="#A51C30",bgcolor="#fff2f4",width=150,input_filter=ft.NumbersOnlyInputFilter())
    inp_pass=ft.TextField(hint_text="Contraseña",label="Contraseña",border_color="#A51C30",bgcolor="#fff2f4",width=150,password=True)
    inp_passrd=ft.TextField(hint_text="Repita la contraseña",label="Repetir contraseña",border_color="#A51C30",bgcolor="#fff2f4",width=150,password=True)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    submit=ft.CupertinoButton(content=ft.Text("REGISTRAR",color="WHITE",font_family="Berlin Sans FB"),bgcolor="#ff0025",on_click=on_click_reg)
    page.add(
        ft.Row(
            [
                cortado,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.add(
        ft.Row(
            [
                titulo,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        inp_usr,
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        inp_nombre,
                        inp_apellido
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        inp_email,
                        inp_tlf
                    ],alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        inp_pass, 
                        inp_passrd
                    ],alignment=ft.MainAxisAlignment.CENTER,
                )
                
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    )
    page.add(
        ft.Row(
            [
                submit,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
        

ft.app(reg_user)