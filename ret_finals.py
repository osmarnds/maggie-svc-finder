from models.models import Services_Temp
from models.models import Services_Final
from models.models import Endpoints_Temp
from models.models import Endpoints_Final
import labio

labio.db.init()

svcs_temp = Services_Temp.query.all()
svcs_final = Services_Final.query.all()

ends_temp = Endpoints_Temp.query.all()

#regs = Services_Final.query.count()
regs = 0

# Merge dss Serviços (Tempórário -> Final)
for item in svcs_temp:
    record = Services_Final()
    regs += 1
    record.svc_id = regs
    record.svc_name = item.tsvc_name
    record.svc_entrypoint = item.tsvc_entrypoint
    record.svc_description = item.tsvc_description
    record.svc_endpoints = item.tsvc_endpoints
    record.svc_status = 'Ativo'
    record.merge()
    #record.session.delete(item) # depois de adicionar na final remove da temporária
record.session.commit()

''' 
# Merge dos Endpoints (Tempórário -> Final)
for item in ends_temp:
    rec_end = Endpoints_Final()
    rec_end.end_name = item.tend_name
    rec_end.end_url = item.tend_url 
    rec_end.end_description = item.tend_description
    rec_end.merge()
    #rec_end.session.delete(item) # depois de adicionar na final remove da temporária
Endpoints_Final.session.commit()
'''
