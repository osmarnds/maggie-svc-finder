import labio

labio.db.init()


from models.models import Services_Temp


svc_record = Services_Temp()

svc_record.svc_name = 'Test4'
svc_record.svc_description = 'Test service3'
svc_record.svc_endpoints = 'dasdsadadsads adsdas ds d2'
svc_record.svc_entrypoint = 'https://sdkfjdskfjsdkjfkdsfsd4'

svc_record.add()

svc_record.session.commit()



svcs = Services_Temp.query.filter(Services_Temp.svc_name == 'Test2').all()

for item in svcs:
    print(item)