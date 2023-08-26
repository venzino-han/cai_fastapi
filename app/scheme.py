from typing import Optional

from pydantic import BaseModel


class ConstructionBase(BaseModel):
    # id: Optional[int]
    gis_data: Optional[str]
    keywords: Optional[str]
    pyeong_cost: Optional[int]
    donation_land_ratio: Optional[float]
    BSNS_PK : str #사업번호
    GU_NM : str #자치구 이름
    BJDON_NM : str #법정동
    BTYP_NM : str #사업구분
    STEP_SE_NM : str #운영구분
    CAFE_NM : str #추진위원회/조합명
    REPRSNT_JIBUN : str #대표지번
    PROGRS_STTUS : str #진행단계
    CAFE_STTUS : str #상태
    ZONE_NM : Optional[str] #정비구역명칭
    ZONE_ADRES : Optional[str] #정비구역위치
    ZONE_AR : Optional[float] #정비구역면적
    TOTAR : Optional[float] # 건축연면적
    CTY_PLAN_SPFC_NM : Optional[str] # 용도지역
    CTY_PLAN_SPCFC_NM :  Optional[str] #용도지구
    LAD_BLDLND_AR : Optional[float] #택지면적
    LAD_PBSPCE_AR : Optional[float] #공공면적
    LAD_ROAD_AR : Optional[float] # 도로면적
    LAD_PARK_AR : Optional[float] #공원면적
    LAD_GREENS_AR : Optional[float] #녹지면적
    LAD_SCHUL_AR : Optional[float] #학교면적
    LAD_ETC_AR : Optional[float] #기타면적
    BILDNG_PRPOS_NM : Optional[str] #주용도
    BILDNG_BDTLDR  : Optional[float] # 건폐율
    BILDNG_FLRSPCER : Optional[float] # 용적률
    BILDNG_HG : Optional[float] # 높이
    BILDNG_GROUND_FLOOR_CO : Optional[int] # 지상층수
    BILDNG_UNDGRND_FLOOR_CO : Optional[int] # 지하층수
    SUM_BILDNG_CO : Optional[int] # 건설세대총수
    BILDNG_60_CO : Optional[int] # 60미만 건설세대수
    BILDNG_60_85_CO : Optional[int] # 60이상 85이하 건설세대수
    BILDNG_85_CO : Optional[int] # 85초과 건설세대수
    BILDNG_RM :  Optional[str] #건축계획비고
    LOCIMG01 : Optional[str] #위치도
    LOCIMG02 : Optional[str] #조감도
    LOCIMG03 : Optional[str] #배치도 

class ConstructionCreate(ConstructionBase):
    class Config:
        orm_mode = True

class Construction(ConstructionBase):
    id : int
    reprsnt_coord_lng : Optional[float]
    reprsnt_coord_lat : Optional[float]
    class Config:
        orm_mode = True


class News(BaseModel):
    id : Optional[int]
    construction_id : int
    thumnl_url : str
    url : str
    title : str
    description : str
    pubdate : str
    keywords : str
    media :str
    ks_graph : Optional[str]

    class Config:
        orm_mode = True



class LotPrice(BaseModel):
    id: int
    lot_id: int
    year: int
    price: int

    class Config:
        orm_mode = True



class Lot(BaseModel):
    id: int
    construction_id: int
    pnu: int
    coordinates: str
    land_use_type: str
    land_area: int
    purpose_area_1: str
    purpose_area_2: str
    land_use_situation: str
    topography_height: str
    topography_form: str
    road_side_type: str

    class Config:
        orm_mode = True


 
class PrePriceSimul(BaseModel):
    id: int
    construction_id: int
    pre_simul_date: int
    pre_predicted_prc: int
    building_number: int
    room_number: int

    class Config:
        orm_mode = True

   
class PostPriceSimul(BaseModel):
    id: int
    sale_id: int
    #pyeong_type: int
    post_simul_date: int
    post_predicted_prc: int

    class Config:
        orm_mode = True



class SaleInfo(BaseModel):
    id: int
    construction_id: int
    pyeong_type: int
    request_land: float
    num_copartner_building: int
    num_general_building: int

    class Config:
        orm_mode = True


class UserBasemodel(BaseModel):
    id: int
    email: str
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True

class UserCreate(UserBasemodel):
    password: str

class User(UserBasemodel):
    pass