#set PYTHONPATH=.

''' Module for Services models and schemas '''
from sqlalchemy import (
    Column, String, Integer, DateTime, func, Sequence, ForeignKey)
from labio.database import Base
from sqlalchemy.orm import relationship


class Services_Final(Base):
    '''Model class for Services_Final table'''

    __tablename__ = 'services_final'

    svc_id = Column(Integer, primary_key=True, autoincrement=True)
    svc_name = Column(String(500))
    svc_entrypoint = Column(String(500), primary_key=True)
    svc_description = Column(String(9999))
    svc_endpoints = Column(Integer)
    svc_status = Column(String(500))

    def __repr__(self):
        return '<Service %r>' % (self.svc_name)


class Services_Temp(Base):
    '''Model class for Services_Temp table'''

    __tablename__ = 'services_temp'

    tsvc_name = Column(String(500))
    tsvc_entrypoint = Column(String(500), primary_key=True)
    tsvc_description = Column(String(9999))
    tsvc_endpoints = Column(Integer)

    def __repr__(self):
        return '<Service_temp %r>' % (self.tsvc_entrypoint)


class Endpoints_Final(Base):
    '''Model class for Endpoints_Final table'''

    __tablename__ = 'endpoints_final'

    end_id = Column(Integer, primary_key=True, autoincrement=True)
    svc_id = Column(Integer, ForeignKey(Services_Final.svc_id))
    end_name = Column(String(500))
    end_url = Column(String(500), primary_key=True)
    end_description = Column(String(9999))

    def __repr__(self):
        return '<Endpoint %r>' % (self.end_name)


class Endpoints_Temp(Base):
    '''Model class for Endpoints_Temp table'''

    __tablename__ = 'endpoints_temp'

    svc_name = Column(String(500))
    end_name = Column(String(500))
    end_url = Column(String(500), primary_key=True)
    end_description = Column(String(9999))

    def __repr__(self):
        return '<Endpoint_temp %r>' % (self.end_name)
