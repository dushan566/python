import urllib.request
import json

def json_data(response):
    json_response = json.loads(response)
    if "total" in json_response["MRData"]:
        print(json_response["MRData"]["total"])
    season = json_response["MRData"]["RaceTable"]["season"]
    print(str(season))
    

def get_status(url):
    appurl = urllib.request.urlopen(url)
    status_code = appurl.getcode()
    print(status_code)
    response = appurl.read()
    if status_code == 200:
        print(url + " is accessible")
        #print(response)
        json_data(response)
    else:
        print(url + " is unreachable")
        print(response)

if __name__ == "__main__":
    get_status("http://ergast.com/api/f1/2004/1/results.json") 