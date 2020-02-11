from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import json

#Class that uses OSMpython tools to generate an overpass query and sends it over to the overpass API to get back requested data in JSON


def query(Key, Value, Location):
        nominatim = Nominatim()
        areaId = nominatim.query(f'{Location}').areaId()
        overpass = Overpass()    
        query = overpassQueryBuilder(area=areaId, elementType=['node','way','relation'], selector= f'"{Key}"="{Value}"', includeGeometry=True)
        print("querying OSM")
        result = overpass.query(query, timeout = 250)
        result = result.toJSON()
        return result

def boundbox(Key, Value, box):
        #nominatim = Nominatim()
        print(box)
        overpass = Overpass()    
        query = overpassQueryBuilder(bbox= box, elementType=['node','way','relation'], selector= f'"{Key}"="{Value}"', includeGeometry=True)
        print(query)
        result = overpass.query(query, timeout = 250)
        result = result.toJSON()
        return result




