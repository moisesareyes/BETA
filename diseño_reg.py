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
    page.bgcolor="WHITE"
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
            if inpusr.value=="":
                inpusr.label="LLENAR CAMPO"
                inpusr.border_color="#ffffff"
                inpusr.color="#ffffff"
                inpusr.bgcolor="#ff0000"
                inpusr.hint_text="LLENAR CAMPO"
                page.update()
            elif inpnom.value=="":
                inpnom.label="LLENAR CAMPO"
                inpnom.border_color="#ffffff"
                inpnom.color="#ffffff"
                inpnom.bgcolor="#ff0000"
                inpnom.hint_text="LLENAR CAMPO"
                page.update()
            elif inpll.value=="":
                inpll.label="LLENAR CAMPO"
                inpll.border_color="#ffffff"
                inpll.color="#ffffff"
                inpll.bgcolor="#ff0000"
                inpll.hint_text="LLENAR CAMPO"
                page.update()
            elif inpmail.value=="":
                inpmail.label="LLENAR CAMPO"
                inpmail.hint_text="LLENAR CAMPO"
                inpmail.border_color="#ffffff"
                inpmail.color="#ffffff"
                inpmail.bgcolor="#ff0000"
                page.update()
            elif inptlf.value=="":
                inptlf.label="LLENAR CAMPO"
                inptlf.hint_text="LLENAR CAMPO"
                inptlf.border_color="#ffffff"
                inptlf.color="#ffffff"
                inptlf.bgcolor="#ff0000"
                page.update()
            elif inpass.value=="":
                inpass.label="LLENAR CAMPO"
                inpass.hint_text="LLENAR CAMPO"
                inpass.border_color="#ffffff"
                inpass.color="#ffffff"
                inpass.bgcolor="#ff0000"
                page.update()
            elif inpassword.value=="":
                inpassword.label="LLENAR CAMPO"
                inpassword.hint_text="LLENAR CAMPO"
                inpassword.border_color="#ffffff"
                inpassword.color="#ffffff"
                inpassword.bgcolor="#ff0000"
                page.update()
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
    cortado=ft.Container(height=20,bgcolor="WHITE")
    titulo=ft.Text(value="REGISTRO DE USUARIO",color="#A51C30",font_family="Impact",size=28)
    inp_usr = ft.TextField(hint_text="Usuario",label="Usuario",border_color="#A51C30",bgcolor="#fff2f4")
    inp_nombre=ft.TextField(hint_text="Nombre",label="Nombre",border_color="#A51C30",bgcolor="#fff2f4")
    inp_apellido=ft.TextField(hint_text="Apellido",label="Apellido",border_color="#A51C30",bgcolor="#fff2f4")
    inp_email=ft.TextField(hint_text="Email",label="Email",border_color="#A51C30",bgcolor="#fff2f4")
    inp_tlf=ft.TextField(hint_text="Telefono",label="Telefono",border_color="#A51C30",bgcolor="#fff2f4",input_filter=ft.NumbersOnlyInputFilter())
    inp_pass=ft.TextField(hint_text="Contraseña",label="Contraseña",border_color="#A51C30",bgcolor="#fff2f4",password=True)
    inp_passrd=ft.TextField(hint_text="Repita la contraseña",label="Repetir contraseña",border_color="#A51C30",bgcolor="#fff2f4",password=True)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    submit=ft.ElevatedButton(text="REGISTRAR",bgcolor="#A51C30",color="WHITE",height=50,width=250,on_click=on_click_reg)
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
                inp_usr,
                inp_nombre,
                inp_apellido,
                inp_email,
                inp_tlf,
                inp_pass, 
                inp_passrd,
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