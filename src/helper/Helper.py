import json

from pprint import pprint

class Helper:
    
    def showJSON(data):
        return (json.dumps(data, indent=4))
    
    def showPrint(data):
        return pprint(data, width=40)