import flet as ft
from src.index import index
from src.transf_main import transf_main
from src.main_retiro import main_ret
from src.config import config
from src.transf.converse import converse
from src.transf.recargas import recg
from src.transf.trasnf import transf
from src.retiro.retiro_Bs import retiro_bs
from src.history import history
from main_index import indexforusr
from diseño_reg import reg_user
from inicio import loginp
from src.retiro.retirousd import retirousd
from src.config01.themes import newthemes
import json
class router:
    def __init__(self,page,ft,theme) :
        global nopage
        nopage=page
        global notheme
        notheme=theme
        with open ('Diseño/usr.json','r') as file:
            inf=file.read()
        infj=json.loads(inf)
        user=infj['user']
        self.page=page
        self.ft=ft
        self.routes={
            '/':index(page,user,notheme),
            '/transf':transf_main(page,user,notheme),
            '/retiro':main_ret(page,user,notheme),
            '/trasf/converse':converse(page,user,notheme),
            '/transf/recarga':recg(page,user,notheme),
            '/transf/transferencia':transf(page,user,notheme),
            '/retiro/bsd':retiro_bs(page,user,notheme),
            '/retiro/usd':retirousd(page,user,notheme),
            '/config':config(page,user,notheme),
            '/config/theme':newthemes(nopage,user),
            '/history':history(page,user,notheme),
            '/index':indexforusr(page,notheme),
            '/index/reg':reg_user(page,notheme),
            '/index/login':loginp(page,notheme)}
        self.body=ft.Container(content=self.routes['/'])
    def route_change(self,route):
        with open ('Diseño/usr.json','r') as file:
            inf=file.read()
        infj=json.loads(inf)
        user=infj['user']
        self.body.content=self.routes[route.route]
        self.body.update()
        self.page.update()
        self.routes={
            '/':index(nopage,user,notheme),
            '/transf':transf_main(nopage,user,notheme),
            '/retiro':main_ret(nopage,user,notheme),
            '/trasf/converse':converse(nopage,user,notheme),
            '/transf/recarga':recg(nopage,user,notheme),
            '/transf/transferencia':transf(nopage,user,notheme),
            '/retiro/usd':retirousd(nopage,user,notheme),
            '/retiro/bsd':retiro_bs(nopage,user,notheme),
            '/config':config(nopage,user,notheme),
            '/config/theme':newthemes(nopage,user),
            '/history':history(nopage,user,notheme),
            '/index':indexforusr(nopage,notheme),
            '/index/reg':reg_user(nopage,notheme),
            '/index/login':loginp(nopage,notheme)}