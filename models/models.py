''' Module for Automation models and schemas '''
from sqlalchemy import (
    Column, String, Integer, DateTime, func, Sequence)
from app.database import Base

class Automation(Base):
    '''Model class for Automation table'''

    __tablename__ = 'automation'

    automation_id = Column(Integer(), Sequence('automation_id_seq'), primary_key=True)
    group_name = Column(String(400), nullable=False, index=True, unique=True)
    description = Column(String(4000), nullable=True)
    filter = Column(String(4000), nullable=False)
    status = Column(String(1), nullable=False, index=True)
    snow_request = Column(String(400), nullable=True, index=True)
    last_execution_date = Column(DateTime(), nullable=True, index=True)
    created_by = Column(String(400), nullable=False, index=True)
    created_date = Column(DateTime(), server_default=func.now(), index=True)
    modified_by = Column(String(400), nullable=False, index=True)
    modified_date = Column(DateTime(), server_default=func.now(), onupdate=func.now(), index=True)
