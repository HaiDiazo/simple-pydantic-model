from pydantic import BaseModel, validator, Field, root_validator
from typing import List

DataDict = dict[str, object]

class AtributeProperties(BaseModel): 
    id: str = Field(..., alias="id")
    name: str = Field(..., alias="name")
    category: str = Field(..., alias="category")
    category_en: str = Field(..., alias="category_en")
    sub_category: str = Field(..., alias="sub_category")
    sub_category_en: str = Field(..., alias="sub_category_en")
    country: str = Field(..., alias="country")
    country_code: str = Field(..., alias="country_code")
    province: str = Field(..., alias="province")
    city: str = Field(..., alias="city")
    kecamatan_name: str = Field(..., alias="kecamatan_name")
    village: str = Field(alias="village", default=None)
    vital_object: bool = Field(..., alias="vital_object")

    @validator("village", pre=True)
    def emptry_string(cls, value: str): 
        if value != "": 
            return value 
        return None

    @validator("vital_object")
    def fixing_vital_object(cls, value: str): 
        if value == "TRUE": 
            return True
        return False


class PoiObj(BaseModel): 
    geometry: List[float]
    properties: AtributeProperties

    @root_validator(pre=True)
    def properties_nested(cls, values: DataDict) -> DataDict: 
        atribute = AtributeProperties.parse_obj(values)
        values['properties'] = atribute.dict()
        return values


    @validator("geometry", pre=True)
    def geometry_list(cls, value) -> List[float]: 
        if value != '':
            geo_point = []
            split_geo = value.split(", ")
            
            for geo in split_geo: 
                geo_point.append(float(geo))
                    
            return split_geo
        return []
    