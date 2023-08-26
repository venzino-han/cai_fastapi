# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey, Float, JSON, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from db import Base, ENGINE
class ConstructionStatTable(Base):
    __tablename__ = 'construction_stat'
    id = Column(Integer, primary_key=True, autoincrement=True)
    construction_id = Column(Integer, ForeignKey('Construction.id'))
    construction = relationship('ConstructionTable', back_populates='stats')
    avg_land_area = Column(Float, nullable=True)
    freq_purpose_area_1 = Column(JSON, nullable=True)
    freq_purpose_area_2 = Column(JSON, nullable=True)
    freq_land_use_situation = Column(JSON, nullable=True)
    freq_topography_height = Column(JSON, nullable=True)
    freq_topography_form = Column(JSON, nullable=True)
    freq_road_side_type = Column(JSON, nullable=True)
    cnt_lot = Column(Integer, nullable=True)
    avg_price_by_year = Column(JSON)

class ConstructionTable(Base):
    __tablename__ = 'Construction'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    news: Mapped[List["NewsTable"]] = relationship(
        back_populates="construction")  # 부모(construction)을 참조하는 참조변수(news)
    lots: Mapped[List["LotTable"]] = relationship(
        back_populates="construction")
    stats: Mapped[List["ConstructionStatTable"]] = relationship(
        back_populates="construction")
    preprice_simulations: Mapped[List["PrePriceSimulTable"]] = relationship(
        back_populates="construction")
    sale_informations: Mapped[List["SaleInfoTable"]] = relationship(
        back_populates="construction")
    reprsnt_coord_lat = Column(String(20), nullable=True) # for exact number
    reprsnt_coord_lng = Column(String(20), nullable=True)
    gis_data = Column(String(50), nullable=True)
    keywords = Column(String(100), nullable=True)
    pyeong_cost = Column(Integer, nullable=True)
    donation_land_ratio = Column(Float, nullable=True)
    BSNS_PK = Column(String(50), nullable=False) #사업번호
    GU_NM = Column(String(30), nullable=False) #자치구 이름
    BJDON_NM = Column(String(30), nullable=False) #법정동
    BTYP_NM = Column(String(30), nullable=False) #사업구분
    STEP_SE_NM = Column(String(30), nullable=False) #운영구분
    CAFE_NM = Column(String(100), nullable=False) #추진위원회/조합명
    REPRSNT_JIBUN = Column(String(30), nullable=False) #대표지번
    PROGRS_STTUS = Column(String(30), nullable=False) #진행단계
    CAFE_STTUS = Column(String(30), nullable=False) #상태
    ZONE_NM = Column(String(100), nullable=True) #정비구역명칭
    ZONE_ADRES = Column(String(100), nullable=True) #정비구역위치
    ZONE_AR = Column(Float, nullable=True) #정비구역면적
    TOTAR = Column(Float, nullable=True) # 건축연면적
    CTY_PLAN_SPFC_NM = Column(String(200), nullable=True) # 용도지역
    CTY_PLAN_SPCFC_NM =  Column(String(200), nullable=True) #용도지구
    LAD_BLDLND_AR = Column(Float, nullable=True) #택지면적
    LAD_PBSPCE_AR = Column(Float, nullable=True) #공공면적
    LAD_ROAD_AR = Column(Float, nullable=True) # 도로면적
    LAD_PARK_AR = Column(Float, nullable=True) #공원면적
    LAD_GREENS_AR = Column(Float, nullable=True) #녹지면적
    LAD_SCHUL_AR = Column(Float, nullable=True) #학교면적
    LAD_ETC_AR = Column(Float, nullable=True) #기타면적
    BILDNG_PRPOS_NM = Column(String(100), nullable=True) #주용도
    BILDNG_BDTLDR  = Column(Float, nullable=True) # 건폐율
    BILDNG_FLRSPCER = Column(Float, nullable=True) # 용적률
    BILDNG_HG = Column(Float, nullable=True) # 높이
    BILDNG_GROUND_FLOOR_CO = Column(Integer, nullable=True) # 지상층수 
    BILDNG_UNDGRND_FLOOR_CO = Column(Integer, nullable=True) # 지하층수
    SUM_BILDNG_CO = Column(Integer, nullable=True) # 건설세대총수
    BILDNG_60_CO = Column(Integer, nullable=True) # 60미만 건설세대수
    BILDNG_60_85_CO = Column(Integer, nullable=True) # 60이상 85이하 건설세대수
    BILDNG_85_CO = Column(Integer, nullable=True) # 85초과 건설세대수
    BILDNG_RM =  Column(String(200), nullable=True) #건축계획비고
    LOCIMG01 = Column(String(200), nullable=True) #위치도
    LOCIMG02 = Column(String(200), nullable=True) #조감도
    LOCIMG03 = Column(String(200), nullable=True) #배치도

class NewsTable(Base):
    __tablename__ = 'News'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    construction_id: Mapped[int] = mapped_column(ForeignKey("Construction.id"))
    construction: Mapped["ConstructionTable"] = relationship(back_populates="news")
    thumnl_url = Column(String(50), nullable=False)
    url = Column(String(200), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    keywords = Column(String(1000), nullable=True)
    ks_graph = Column(String(50), nullable=True)
    pubdate = Column(String(50), nullable=True)
    media = Column(String(50), nullable=True)
    
class LotPriceTable(Base):
    __tablename__ = 'lot_price'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lot_id = Column(Integer, ForeignKey('lot.id'), nullable=False)
    lot = relationship('LotTable', back_populates='prices')
    year = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)

class LotTable(Base):
    __tablename__ = 'lot'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    construction_id: Mapped[int] = mapped_column(ForeignKey("Construction.id"))
    construction: Mapped["ConstructionTable"] = relationship(
        back_populates="lots")
    pnu = Column(Integer, nullable=False)
    coordinates = Column(String(1024))
    land_use_type = Column(String(10))
    land_area = Column(Integer)
    purpose_area_1 = Column(String(30))
    purpose_area_2 = Column(String(30))
    land_use_situation = Column(String(10))
    topography_height = Column(String(10))
    topography_form = Column(String(10))
    road_side_type = Column(String(10))
    prices = relationship('LotPriceTable', back_populates='lot')


class PrePriceSimulTable(Base):
    __tablename__ = 'preprice_simulation'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    construction_id: Mapped[int] = mapped_column(ForeignKey("Construction.id"))
    construction: Mapped["ConstructionTable"] = relationship(
        back_populates="preprice_simulations")
    pre_simul_date = Column(Integer, nullable=False)
    pre_predicted_prc = Column(Integer, nullable=False)
    building_number = Column(Integer, nullable=False)
    room_number = Column(Integer, nullable=False)
    
class PostPriceSimulTable(Base):
    __tablename__ = 'postprice_simulation'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sale_id = Column(Integer, ForeignKey('sale_information.id'), nullable=False)
    sale = relationship('SaleInfoTable', back_populates='postprices')
    #pyeong_type = Column(Integer, nullable=False)
    post_simul_date = Column(Integer, nullable=False)
    post_predicted_prc = Column(Integer, nullable=False)

class SaleInfoTable(Base):
    __tablename__ = 'sale_information'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    construction_id: Mapped[int] = mapped_column(ForeignKey("Construction.id"))
    construction: Mapped["ConstructionTable"] = relationship(
        back_populates="sale_informations")
    pyeong_type = Column(Integer, nullable=False)
    request_land = Column(Float, nullable=False)
    num_copartner_building = Column(Integer, nullable=False)
    num_general_building = Column(Integer, nullable=False)
    postprices = relationship('PostPriceSimulTable', back_populates='sale')


def create_tbl():
    Base.metadata.create_all(bind=ENGINE)


def drop_tbl():
    Base.metadata.drop_all(bind=ENGINE)


if __name__ == "__main__":
    # for development only
    # drop_tbl()

    create_tbl()

    # for development only
    # from main import *
