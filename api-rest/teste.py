import requests
import json

id = 110
body = {"_id":110, "nome": "python3"}
headers = {"content-type":"application/json"}

pessoas = requests.put("http://127.0.0.1:5000/pessoas/"+str(id), data=json.dumps(body), headers=headers)

print(pessoas.json())
print(pessoas.status_code)