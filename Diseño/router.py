import flet as ft
from src.index import index
from src.transf_main import transf_main
from src.main_retiro import main_ret
from src.config import config
from src.transf.converse import converse
from src.transf.recargas import recg
from src.transf.trasnf import transf
from src.retiro.retiro_Bs import retiro_bs
from src.config import config
from src.history import history
from main_index import indexforusr
from diseño_reg import reg_user
from inicio import loginp
class router:
    def __init__(self,page,ft,user) :
        self.page=page
        self.ft=ft
        self.routes={
            '/':index(page,user),
            '/transf':transf_main(page,user),
            '/retiro':main_ret(page,user),
            '/trasf/converse':converse(page,user),
            '/transf/recarga':recg(page,user),
            '/transf/transferencia':transf(page,user),
            '/retiro/bsd':retiro_bs(page,user),
            '/config':config(page,user),
            '/history':history(page,user),
            '/index/index':indexforusr(page),
            '/index/reg':reg_user(page),
            '/index/login':loginp(page),

        }
        self.body=ft.Container(content=self.routes['/'])
    def route_change(self,route):
        self.body.content=self.routes[route.route]
        self.body.update()
        self.page.update()