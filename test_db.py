import labio

labio.db.init()

from models.models import Services_Temp

svc_record = Services_Temp()

''' Exemplo de item
svc_record.svc_name = 'Test4'
svc_record.svc_description = 'Test service4'
svc_record.svc_endpoints = 'test4'
svc_record.svc_entrypoint = 'https://test4'
'''
# adicionar item na tabela (os dados foram atribuidos acima) #
#svc_record.add()

# deletar um item da tabela #
#svc_record.session.delete(item)

# sempre que modificar a tabela, precisa dar commit (adicionar ou deletar) #
#svc_record.session.commit()

svcs = Services_Temp.query.filter(Services_Temp.tsvc_name == 'Test4').all()
#svcs = Services_Temp.query.filter(Services_Temp.tsvc_entrypoint != 'a').all()

for item in svcs:
    print(item)
