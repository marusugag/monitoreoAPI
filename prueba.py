import requests

dato = {"lugar":"Girardota", "temperatura": 25, "humedad": 67}

res = requests.post("http://localhost:8000/monitoreo", json=dato)

print(res.text)

