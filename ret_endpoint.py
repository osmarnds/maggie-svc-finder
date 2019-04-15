from models.models import Services_Temp
from models.models import Endpoints_Temp
import requests, labio
import re    # para pegar apenas os números de uma url (id)
from bs4 import BeautifulSoup

labio.db.init()
end_record = Endpoints_Temp()
svcs = Services_Temp.query.all()

# varre a tabela de serviços e pega o id de cada serviço para acessar seus endpoints
for item in svcs:
    id = item.tsvc_entrypoint
    id = re.sub('[^0-9]', '', id)
    response = requests.get('https://www.biocatalogue.org/services/'+str(id)+'/service_endpoint')
    print(response.status_code)
    # utiliza o soup para encontrar no html a classe 'entry', onde ficam os endpoints
    soup = BeautifulSoup(response.text, 'html.parser')
    services_list = soup.find_all(class_='entry')
    print('serviço:',id,'-',item.tsvc_name)
    for service in services_list:
        end_record = Endpoints_Temp()
        end_record.tend_name = service.a.get_text()
        end_record.tend_url = 'http://www.biocatalogue.org' + service.a.get('href')
        end_record.tsvc_name = item.tsvc_name
        end_record.tend_description = ''
        end_record.add()
end_record.session.commit()