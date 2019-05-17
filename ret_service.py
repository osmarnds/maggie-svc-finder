from models.models import Services_Temp
import requests, json, labio, re
from bs4 import BeautifulSoup

labio.db.init()

# request de api em objeto json
response = requests.get('https://www.biocatalogue.org/services.json')
services = response.json()
# 200 = ok
print(response.status_code)

pages = services['services']['pages'] + 1

for x in range(1, pages):
    response = requests.get(
        'https://www.biocatalogue.org/services.json?page='+str(x))
    services = response.json()
    if response.status_code != 200:
        print("Erro na requisição! Página",x)
    # results contém os serviços
    results = services['services']['results']
    for service in results:
        # novo registro na tabela
        svc_record = Services_Temp()
        # atribui os campos e adiciona
        svc_record.tsvc_name = service['name']
        svc_record.tsvc_description = service['description']
        if svc_record.tsvc_description == None or svc_record.tsvc_description == '':
            svc_record.tsvc_description = 'No Description'
        svc_record.tsvc_endpoints = 0
        svc_record.tsvc_entrypoint = service['resource']
        svc_record.add()       
svc_record.session.commit()

''' Execução demora!
# Pega o número de endpoints de cada serviço e adiciona na temporária de serviços
svcs_list = Services_Temp.query.all()
for svc in svcs_list:
    resp = requests.get(svc.tsvc_entrypoint) 
    soup = BeautifulSoup(resp.text, 'html.parser')
    id = svc.tsvc_entrypoint
    id = re.sub('[^0-9]', '', id)
    num_end = soup.find(href="/services/"+id+"/service_endpoint")
    for num in num_end:
        num = re.sub('[^0-9]', '', num)
        svc.tsvc_endpoints = num
Services_Temp.session.commit()
'''