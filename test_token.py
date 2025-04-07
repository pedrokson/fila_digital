import jwt
import time  # Para comparar o tempo de expiração com o atual

# Seu token gerado (substitua com o token que você obteve após login)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c3VhcmlvX2lkIjoxLCJleHAiOjE3NDM5MDk3MDR9.b0OWvUYqSXS8ey6URpIsZamRXF_4YNGtYe0xw-Oqe8M"
SECRET_KEY = "meu_segredo_supersecreto"  # Certifique-se de que seja o mesmo segredo usado no backend

# Decodificar o token sem validar a assinatura para ver o payload
payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"], options={"verify_signature": False})

# Verificar se o token expirou
exp_time = payload["exp"]
current_time = int(time.time())  # Tempo atual em Unix timestamp

if exp_time < current_time:
    print("O token expirou.")
else:
    print("O token é válido até:", exp_time)

# Mostrar o payload
print("Payload:", payload)
