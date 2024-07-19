from src.ExtractDataOmeka import ExtractDataOmeka
from src.helper.Helper import Helper

endpoint = 'http://xxxxxx/api'
outputfile = 'output.csv'



if __name__ == '__main__':
    extractomekaobj = ExtractDataOmeka(endpoint,outputfile)
    msg = extractomekaobj.extract()
    print(msg)
    ##
    response, content = extractomekaobj.request()   
    # print(Helper.showJSON(response))
    print(Helper.showJSON(content))
    
