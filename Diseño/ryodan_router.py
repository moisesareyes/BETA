import flet as ft
from main_index import indexforusr
from diseño_reg import reg_user
from inicio import loginp
class routeryo:
    def __init__(self,page,ft) :
        self.page=page
        self.ft=ft
        self.routes={
            '/index/index':indexforusr(page),
            '/index/reg':reg_user(page),
            '/index/login':loginp(page)
        }
            
        self.body=ft.Container(content=self.routes['/index/index'])
    def route_change(self,route):
        self.body.content=self.routes[route.route]
        self.body.update()
        self.page.update()