#set PYTHONPATH=.

''' Module for Services models and schemas '''
from sqlalchemy import (Column, String, Integer, DateTime, func, Sequence, ForeignKey, Table)
from labio.database import Base
from sqlalchemy.orm import relationship


class Services_List(Base):
    __tablename__ = 'service_list'
    id = Column(Integer, primary_key=True)
    url = Column(String)

class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    entrypoint = Column(String)
    base_url = Column(String)
    doc_url = Column(String)
    svc_end = relationship("Endpoint") 
    svc_sim = relationship("Similar")
    svc_tag = relationship("Tag")
   
class Endpoints_List(Base):
    __tablename__ = 'endpoints_list'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    service_name = Column(String)
    service_id = Column(Integer,ForeignKey('service.id'))

class Endpoint(Base):
    __tablename__ = 'endpoint'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    name = Column(String)
    label = Column(String)
    template = Column(String)
    description = Column(String)
    parameters = Column(String)
    service_name = Column(String)
    service_id = Column(Integer,ForeignKey('service.id'))

class Similar(Base):
    __tablename__ = 'similar'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    service_id = Column(Integer,ForeignKey('service.id'))

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    service_id = Column(Integer,ForeignKey('service.id'))

class Logs(Base):
    __tablename__ = 'log'
    log_id = Column(Integer, Sequence('log_id_seq'), primary_key=True)
    log_name = Column(String(500))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    log_status = Column(String(500)) # nao iniciado, rodando, finalizado com sucesso, finalizado com erro

class Details(Base):
    __tablename__ = 'detail'
    detail_id = Column(Integer, Sequence('detail_id_seq'), primary_key=True)
    detail_name = Column(String(500), primary_key=True)
    detail_description = Column(String(9999))
    log_id = Column(Integer,ForeignKey('log.log_id'))



'''
class Services_Final(Base):
   
    __tablename__ = 'services_final'

    svc_id = Column(Integer, Sequence('svc_id_seq'), primary_key=True, unique=True)
    svc_name = Column(String(500))
    svc_entrypoint = Column(String(500), primary_key=True, unique=True)
    svc_description = Column(String(9999))
    svc_endpoints = Column(Integer)
    svc_status = Column(String(500))

    def __repr__(self):
        return '<Service %r>' % (self.svc_name)


class Services_Temp(Base):
    
    __tablename__ = 'services_temp'

    tsvc_name = Column(String(500))
    tsvc_entrypoint = Column(String(500), primary_key=True)
    tsvc_description = Column(String(9999))
    tsvc_endpoints = Column(Integer)

    def __repr__(self):
        return '<Service_temp %r>' % (self.tsvc_entrypoint)


class Endpoints_Final(Base):
   
    __tablename__ = 'endpoints_final'

    end_id = Column(Integer, Sequence('end_id_seq'), primary_key=True)
    svc_id = Column(Integer) #ForeignKey('services_final.svc_id'))
    end_name = Column(String(500))
    end_url = Column(String(500), primary_key=True)
    end_description = Column(String(9999))

    def __repr__(self):
        return '<Endpoint %r>' % (self.end_name)


class Endpoints_Temp(Base):
   
    __tablename__ = 'endpoints_temp'

    svc_name = Column(String(500))
    end_name = Column(String(500))
    end_url = Column(String(500), primary_key=True)
    end_description = Column(String(9999))

    def __repr__(self):
        return '<Endpoint_temp %r>' % (self.end_name)


class Tag(Base):
    __tablename__ = 'tag'

    #tag_id = Column(Integer, Sequence('tag_id_seq'), primary_key=True)
    tag_name = Column(String(500), primary_key=True)

    def __repr__(self):
        return '<tag %r>' % (self.tag_name)


class Similar(Base):
    __tablename__ = 'similar'

    #similar_id = Column(Integer, Sequence('similar_id_seq'), primary_key=True)
    similar_name = Column(String(500), primary_key=True)

    def __repr__(self):
        return '<Similar %r>' % (self.similar_name)
'''
'''
class Logs(Base):
    ''Model class for Logs table''

    __tablename__ = 'logs'

    log_id = Column(Integer, Sequence('log_id_seq'), primary_key=True)
    log_name = Column(String(500))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    log_status = Column(String(500)) # nao iniciado, rodando, finalizado com sucesso, finalinado com erro

    def __repr__(self):
        return '<Log %r>' % (self.log_name)

class Details(Base):
    'Model class for Details table''

    __tablename__ = 'details'

    detail_id = Column(Integer, Sequence('detail_id_seq'), primary_key=True)
    detail_name = Column(String(500), primary_key=True)
    detail_description = Column(String(9999))

    def __repr__(self):
        return '<Detail %r>' % (self.detail_name)
'''

