import requests, json, time

#inicio = time.time()

response = requests.get('https://www.biocatalogue.org/services.json')
services = response.json()
print(response.status_code)

pages = services['services']['pages'] + 1

with open('services-list.json', 'w') as json_file:
    for x in range(1, pages):
        response = requests.get('https://www.biocatalogue.org/services.json?page='+str(x))
        services = response.json()
        if response.status_code != 200:
            print("Erro na requisição! Página",x)
        results = services['services']['results']
        for service in results:
            details = {
                'name': service['name'],
                'resource': service['resource'],
                'description': service['description']
            }
            json.dump(details, json_file)

#fim = time.time()
#print("Tempo de Execução: ",int(fim - inicio))