import json, csv, requests
from bs4 import BeautifulSoup

page = 1

# Cria arquivo .csv
with open('services-list.csv', 'w', newline='') as fw:
    #usar o dictwriter
    f = csv.writer(fw) # newline='' evita linhas espaçadas
    f.writerow(['List of Services:'])
    while page < 57:
        # verificar como trocar este while por pegar o numero de paginas na estrutura que vem da primeira pagina.
        response = requests.get('http://www.biocatalogue.org/services?page='+str(page))
        print(response.status_code)  # 200 significa requisição OK para cada página
        # 200
        soup = BeautifulSoup(response.text, 'html.parser')

        # Lista de <p class='name'>
        services_list = soup.find_all('p', class_='name')

        # Grava no arquivo .csv o nome do serviço, sua URL
        for service in services_list:
            services = service.a.get_text()
            links = ' http://www.biocatalogue.org' + service.a.get('href')
            f.writerow([services, links])

        page += 1

