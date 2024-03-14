import flet as ft
import json

def secure(page:ft.Page):
    with open ('Diseño/usr.json','r') as file:
        inf=file.read()
    infj=json.loads(inf)
    user=infj['user']
    theme=infj['theme']
    