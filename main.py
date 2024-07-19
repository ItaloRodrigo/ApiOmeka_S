from src.ExtractDataOmeka import ExtractDataOmeka
from src.helper.Helper import Helper
import json


endpoint = 'http://repositorio.itegam.org.br/api'
outputfile = 'output.csv'



if __name__ == '__main__':
    extractomekaobj = ExtractDataOmeka(endpoint,outputfile)
    msg = extractomekaobj.extract()
    print(msg)
    ##
    response, content = extractomekaobj.request()   
    print(json.dumps(str(content), indent=4)) 
    # print(Helper.showJSON(response))
    # print(Helper.showJSON(content))
    