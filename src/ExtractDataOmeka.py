import json
from src.OmekaClient import OmekaClient


class ExtractDataOmeka:
    
    def __init__(self,endpoint,outputfile):
        self.endpoint = endpoint
        self.outputfile = outputfile
    
    @classmethod
    def extract(self):
        return "extraindo..."
    
    def request(self):
        response, content = OmekaClient(self.endpoint).get('media')
        if (response.status != 200):
            print (response.status, response.reason)
            exit()
        else:
            return response, content
        