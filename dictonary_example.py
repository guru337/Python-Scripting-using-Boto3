import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detail=response.json() #Automaticalaly converts json to dictonary


for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])