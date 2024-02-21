import requests 
from bs4 import BeautifulSoup as b
import urllib3
def tasaf():
    urllib3.disable_warnings()
    url = "https://www.bcv.org.ve/"
    html = requests.get(url, verify=False)
    soup= b(html.text, 'html.parser')
    trytasa=soup.find(id="dolar")
    newtasa=trytasa.find("div","col-sm-6 col-xs-6 centrado","strong")
    recorte=newtasa.text
    tasa=f"{recorte[1]}{recorte[2]}.{recorte[4]}{recorte[5]}"
    tasa=float(tasa)
    return tasa
print(tasaf())