import requests

url = "http://127.0.0.1:5000/listar_fila"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:", response.text)  # Exibe a resposta do servidor