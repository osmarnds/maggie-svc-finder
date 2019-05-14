from models.models import Services_Temp
from models.models import Services_Final
from models.models import Endpoints_Temp
from models.models import Endpoints_Final
import labio

labio.db.init()

svcs_temp = Services_Temp.query.all()
svcs_final = Services_Final.query.all()

ends_temp = Endpoints_Temp.query.all()

'''
e = 0
c = 0
for item in svcs_final:
    record = Services_Final() 
    exists = Services_Final.query.filter(item.svc_id <= item.query.count()).first()
    if exists:
        e = 1
        c+=1
        print(exists)
        break
'''
regs = Services_Final.query.count()

for item in svcs_temp:
    regs += 1
    exist = 0
    record = Services_Final()
    #if record.svc_entrypoint == item.tsvc_entrypoint:
    #    exist = 1
    #if exist == 0:    
    record.svc_id = regs
    record.svc_name = item.tsvc_name
    record.svc_entrypoint = item.tsvc_entrypoint
    record.svc_description = item.tsvc_description
    record.svc_endpoints = item.tsvc_endpoints
        #if a: 
    record.svc_status = 'Ativo'
        #else if b:
            #record.svc_status = 'Inativo'
    record.merge()
        #record.session.delete(item) # depois de adicionar na final remove da temporária
record.session.commit()

'''
c = 0
for item in ends_temp:
    c += 1
    rec_end = Endpoints_Final()
    rec_end.svc_id = c
    rec_end.end_name = item.tend_name
    rec_end.end_url = item.tend_url 
    rec_end.end_description = item.tend_description
    rec_end.add()
    #rec_end.session.delete(item) # depois de adicionar na final remove da temporária
Endpoints_Final.session.commit()
'''
