# Exemplos de Uso da Blockchain

## Exemplos via Terminal (curl)

### 1. Consultar a blockchain completa
```bash
curl -X GET http://localhost:5000/blockchain
```

### 2. Consultar um bloco específico
```bash
curl -X GET http://localhost:5000/blocks/0
```

### 3. Adicionar uma transação
```bash
curl -X POST http://localhost:5000/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "sender": "Alice",
    "recipient": "Bob", 
    "amount": 50.0
  }'
```

### 4. Minerar um bloco
```bash
curl -X POST http://localhost:5000/mine \
  -H "Content-Type: application/json" \
  -d '{
    "miner_address": "Minerador1"
  }'
```

### 5. Consultar saldo de um endereço
```bash
curl -X GET http://localhost:5000/balance/Alice
```

### 6. Validar a blockchain
```bash
curl -X GET http://localhost:5000/validate
```

### 7. Consultar estatísticas
```bash
curl -X GET http://localhost:5000/stats
```

## Exemplo Completo de Uso

```bash
# 1. Adicionar algumas transações
curl -X POST http://localhost:5000/transactions -H "Content-Type: application/json" -d '{"sender": "Alice", "recipient": "Bob", "amount": 50.0}'

curl -X POST http://localhost:5000/transactions -H "Content-Type: application/json" -d '{"sender": "Bob", "recipient": "Charlie", "amount": 25.0}'

# 2. Minerar um bloco
curl -X POST http://localhost:5000/mine -H "Content-Type: application/json" -d '{"miner_address": "Minerador1"}'

# 3. Verificar saldos
curl -X GET http://localhost:5000/balance/Alice
curl -X GET http://localhost:5000/balance/Bob
curl -X GET http://localhost:5000/balance/Charlie
curl -X GET http://localhost:5000/balance/Minerador1

# 4. Validar a blockchain
curl -X GET http://localhost:5000/validate
```

## Exemplos em Python

```python
import requests
import json

# URL base da API
BASE_URL = "http://localhost:5000"

# Adicionar transação
def add_transaction(sender, recipient, amount):
    data = {
        "sender": sender,
        "recipient": recipient,
        "amount": amount
    }
    response = requests.post(f"{BASE_URL}/transactions", json=data)
    return response.json()

# Minerar bloco
def mine_block(miner_address):
    data = {"miner_address": miner_address}
    response = requests.post(f"{BASE_URL}/mine", json=data)
    return response.json()

# Consultar saldo
def get_balance(address):
    response = requests.get(f"{BASE_URL}/balance/{address}")
    return response.json()

# Exemplo de uso
if __name__ == "__main__":
    # Adicionar transações
    print(add_transaction("Alice", "Bob", 50.0))
    print(add_transaction("Bob", "Charlie", 25.0))
    
    # Minerar bloco
    print(mine_block("Minerador1"))
    
    # Consultar saldos
    print(get_balance("Alice"))
    print(get_balance("Bob"))
    print(get_balance("Charlie"))
    print(get_balance("Minerador1"))
```
