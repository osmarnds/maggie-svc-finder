from models.models import Services_List
from models.models import Details
from models.models import Logs
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
    response = requests.get('https://www.biocatalogue.org/services.json?page='+str(x))
    services = response.json()
    if response.status_code != 200:
        print("Erro na requisição! Página", x)
    # results contém os serviços
    results = services['services']['results']
    for service in results:
        # novo registro na tabela
        svc_record = Services_List()
        # atribui os campos e adiciona
        svc_record.url = service['resource']
        id = svc_record.url
        id = re.sub('[^0-9]', '', id)
        svc_record.id = id
        svc_record.merge()
        detail = Details()
        detail.detail_id = detail.query.count()+1
        detail.detail_name = 'added service'+svc_record.name
svc_record.session.commit()
