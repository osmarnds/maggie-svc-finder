''' Module for Services models and schemas '''
from sqlalchemy import (
    Column, String, Integer, DateTime, func, Sequence)
from labio.database import Base

i = 0
def mydefault():
    global i
    i += 1
    return i
class Services_Final(Base):
    '''Model class for Services_Final table'''

    __tablename__ = 'services_final'

    svc_id = Column(Integer, Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    svc_name = Column(String)
    svc_entrypoint = Column(String, primary_key=True)
    svc_description = Column(String)
    svc_endpoints = Column(Integer)
    svc_status = Column(String)

    def __repr__(self):
        return '<Service %r>' % (self.svc_name)


class Services_Temp(Base):
    '''Model class for Services_Temp table'''

    __tablename__ = 'services_temp'

    tsvc_name = Column(String)
    tsvc_entrypoint = Column(String, primary_key=True)
    tsvc_description = Column(String)
    tsvc_endpoints = Column(Integer)

    def __repr__(self):
        return '<Service_temp %r>' % (self.tsvc_entrypoint)


class Endpoints_Final(Base):
    '''Model class for Endpoints_Final table'''

    __tablename__ = 'endpoints_final'

    end_id = Column(Integer, Sequence('service_id_sequence'), primary_key=True)
    svc_id = Column(Integer, foreign_key(Services_Final.svc_id))
    end_name = Column(String)
    end_url = Column(String, primary_key=True)
    end_description = Column(String)

    def __repr__(self):
        return '<Endpoint %r>' % (self.end_name)


class Endpoints_Temp(Base):
    '''Model class for Endpoints_Temp table'''

    __tablename__ = 'endpoints_temp'

    svc_name = Column(String)
    end_name = Column(String)
    end_url = Column(String, primary_key=True)
    end_description = Column(String)

    def __repr__(self):
        return '<Endpoint_temp %r>' % (self.end_name)
