''' Module for Services models and schemas '''
from sqlalchemy import (
    Column, String, Integer, DateTime, func, Sequence)
from labio.database import Base


class Services_Final(Base):
    '''Model class for Services_Final table'''

    __tablename__ = 'services_final'

    svc_id = Column(Integer(), Sequence('service_id_sequence'), primary_key=True)
    svc_name = Column(String(400), nullable=False, index=True)
    svc_entrypoint = Column(String(400), nullable=False, unique=True)
    svc_description = Column(String(4000), nullable=True)
    svc_endpoints = Column(Integer(), nullable=False, index=True)
    svc_status = Column(String(1), nullable=False, index=True)

    def __repr__(self):
        return '<Service %r>' % (self.svc_name)


class Services_Temp(Base):
    '''Model class for Services_Temp table'''

    __tablename__ = 'services_temp'

    tsvc_name = Column(String(400), nullable=False, index=True)
    tsvc_entrypoint = Column(String(400), nullable=False, primary_key=True)
    tsvc_description = Column(String(4000), nullable=True)
    tsvc_endpoints = Column(Integer(), nullable=False, index=True)

    def __repr__(self):
        return '<Service_temp %r>' % (self.svc_name)


class Endpoints_Final(Base):
    '''Model class for Endpoints_Final table'''

    __tablename__ = 'endpoints_final'

    end_id = Column(Integer(), Sequence('service_id_sequence'), primary_key=True)
    svc_id = Column(Integer(), unique=True)
    end_name = Column(String(400), nullable=False, index=True)
    end_url = Column(String(400), nullable=False, unique=True)
    end_description = Column(String(4000), nullable=True)

    def __repr__(self):
        return '<Endpoint %r>' % (self.end_name)


class Endpoints_Temp(Base):
    '''Model class for Endpoints_Temp table'''

    __tablename__ = 'endpoints_temp'

    tsvc_name = Column(String(400), nullable=False, index=True)
    tend_name = Column(String(400), nullable=True, index=True)
    tend_url = Column(String(400), nullable=False, primary_key=True)
    tend_description = Column(String(4000), nullable=True)

    def __repr__(self):
        return '<Endpoint_temp %r>' % (self.end_name)
