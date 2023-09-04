from config.base import settings
from elasticsearch import Elasticsearch
from schemas.poi import PoiObj
from elasticsearch.helpers import streaming_bulk
from pprint import pprint


class ElasticUpdate: 

    def __init__(self) -> None:
        self.__host = settings.ELASTIC_HOST
        self.__index = settings.ELASTIC_INDEX
        self.__timeout = 3600

    def fetch(self, datas: list):
         for data in datas: 
            if data['status'] == "UPDATE": 
                model_poi = PoiObj.parse_obj(data)
                clean = model_poi.dict(exclude_none=True)
                
                yield {
                    '_op_type': 'update',
                    '_id': clean['properties']['id'],
                    '_index': self.__index,
                    'doc': clean
                }
            
            elif data['status'] == "DELETE": 
                
                yield {
                    '_op_type': 'delete',
                    '_id': data['id'],
                    '_index': self.__index
                }


    def run(self, datas: list):
        with Elasticsearch(
            hosts=self.__host,
            timeout=self.__timeout
        ) as es: 
            for ok, info in streaming_bulk(client=es, actions=self.fetch(datas), chunk_size=10): 
                if not ok: 
                    raise Exception(info)
                print(info)

client_elastic = ElasticUpdate()
