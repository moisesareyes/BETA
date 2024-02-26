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
class router:
    def __init__(self,page,ft) :
        self.page=page
        self.ft=ft
        self.routes={
            '/':index(page),
            '/transf':transf_main(page),
            '/retiro':main_ret(page),
            '/trasf/converse':converse(page),
            '/transf/recarga':recg(page),
            '/transf/transferencia':transf(page),
            '/retiro/bsd':retiro_bs(page),
            '/config':config(page)
        }
        self.body=ft.Container(content=self.routes['/'])
    def route_change(self,route):
        self.body.content=self.routes[route.route]
        self.body.update()