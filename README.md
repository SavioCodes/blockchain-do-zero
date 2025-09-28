# Blockchain do Zero 🔗

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> Uma implementação educativa de blockchain em Python, desenvolvida para ensinar os conceitos fundamentais da tecnologia blockchain.

**Desenvolvido por [Sávio](https://github.com/SavioCodes) 👨‍💻**

## 📚 O que é Blockchain?

Blockchain é uma tecnologia de registro distribuído que mantém uma lista crescente de registros (blocos) que são vinculados e protegidos usando criptografia. Cada bloco contém:

- **Timestamp**: Momento em que o bloco foi criado
- **Transações**: Dados das transferências realizadas
- **Hash Anterior**: Referência criptográfica ao bloco anterior
- **Hash Atual**: Identificador único do bloco atual
- **Nonce**: Número usado no processo de mineração

### Como Funciona?

1. **Transações** são criadas e ficam pendentes
2. **Mineradores** coletam essas transações e tentam criar um novo bloco
3. **Proof of Work** é usado para "minerar" o bloco (encontrar um hash específico)
4. O **bloco minerado** é adicionado à cadeia
5. A **rede valida** a integridade da blockchain

## 🚀 Funcionalidades

- ✅ **Blocos**: Estrutura completa com timestamp, hash e transações
- ⛏️ **Mineração**: Algoritmo Proof of Work configurável
- 🔒 **Validação**: Verificação de integridade da cadeia
- 💰 **Transações**: Sistema de transferência entre endereços
- 💎 **Saldos**: Cálculo automático de saldos por endereço
- 🌐 **API REST**: Interface completa para interação
- 🧪 **Testes**: Cobertura completa com pytest

## 📁 Estrutura do Projeto

```
blockchain-do-zero/
├── src/
│   ├── __init__.py
│   ├── blockchain.py      # Classe principal da blockchain
│   ├── block.py          # Representação de blocos
│   ├── transaction.py    # Sistema de transações
│   └── api.py           # API Flask
├── tests/
│   ├── __init__.py
│   ├── test_blockchain.py
│   ├── test_block.py
│   ├── test_transaction.py
│   └── test_api.py
├── docs/
│   └── examples.md       # Exemplos de uso
├── requirements.txt      # Dependências
├── run.py               # Script principal
├── README.md
└── LICENSE
```

## 🛠️ Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone o repositório:**
```bash
git clone https://github.com/SavioCodes/blockchain-do-zero.git
cd blockchain-do-zero
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

### Iniciando a API

```bash
python run.py
```

A API estará disponível em: `http://localhost:5000`

### Executando os Testes

```bash
# Todos os testes
pytest

# Com verbose
pytest -v

# Cobertura de código
pytest --cov=src
```

## 🔌 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/blockchain` | Retorna toda a blockchain |
| `GET` | `/blocks/<index>` | Retorna um bloco específico |
| `GET` | `/transactions` | Lista todas as transações |
| `POST` | `/transactions` | Adiciona nova transação |
| `POST` | `/mine` | Minera um novo bloco |
| `GET` | `/balance/<address>` | Consulta saldo de endereço |
| `GET` | `/validate` | Valida a blockchain |
| `GET` | `/stats` | Estatísticas da blockchain |

## 💡 Exemplos de Uso

### 1. Consultando a Blockchain

```bash
curl -X GET http://localhost:5000/blockchain
```

**Resposta:**
```json
{
  "chain": [
    {
      "index": 0,
      "timestamp": "2024-01-01T12:00:00",
      "transactions": [...],
      "previous_hash": "0",
      "hash": "0012abc...",
      "nonce": 1234
    }
  ],
  "difficulty": 2,
  "pending_transactions": [],
  "mining_reward": 10
}
```

### 2. Adicionando uma Transação

```bash
curl -X POST http://localhost:5000/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "sender": "Alice",
    "recipient": "Bob",
    "amount": 50.0
  }'
```

**Resposta:**
```json
{
  "message": "Transação adicionada com sucesso",
  "transaction": {
    "sender": "Alice",
    "recipient": "Bob",
    "amount": 50.0,
    "timestamp": "2024-01-01T12:00:00"
  },
  "pending_transactions": 1
}
```

### 3. Minerando um Bloco

```bash
curl -X POST http://localhost:5000/mine \
  -H "Content-Type: application/json" \
  -d '{"miner_address": "Minerador1"}'
```

**Saída no Terminal:**
```
Minerando bloco 1...
Bloco 1 minerado em 2.34s!
Hash: 00a1b2c3d4e5f6789012345678901234567890
Nonce: 45672
--------------------------------------------------
```

**Resposta da API:**
```json
{
  "message": "Bloco minerado com sucesso",
  "block": {
    "index": 1,
    "timestamp": "2024-01-01T12:05:00",
    "transactions": [...],
    "hash": "00a1b2c3...",
    "nonce": 45672
  },
  "miner_balance": 10.0
}
```

### 4. Consultando Saldo

```bash
curl -X GET http://localhost:5000/balance/Alice
```

**Resposta:**
```json
{
  "address": "Alice",
  "balance": -50.0
}
```

### 5. Validando a Blockchain

```bash
curl -X GET http://localhost:5000/validate
```

**Resposta:**
```json
{
  "is_valid": true,
  "message": "Blockchain válida"
}
```

## 🔧 Personalização

### Ajustando a Dificuldade

No arquivo `src/blockchain.py`, altere o valor:

```python
self.difficulty = 4  # Aumenta a dificuldade (mais zeros no hash)
```

### Modificando a Recompensa

```python
self.mining_reward = 25  # Recompensa de 25 por bloco minerado
```

## 🧪 Exemplo Completo de Teste

Execute este script para testar toda a funcionalidade:

```bash
# Terminal 1: Inicie a API
python run.py

# Terminal 2: Execute os comandos
# Adicionar transações
curl -X POST http://localhost:5000/transactions -H "Content-Type: application/json" -d '{"sender": "Alice", "recipient": "Bob", "amount": 100.0}'

curl -X POST http://localhost:5000/transactions -H "Content-Type: application/json" -d '{"sender": "Bob", "recipient": "Charlie", "amount": 30.0}'

# Minerar bloco
curl -X POST http://localhost:5000/mine -H "Content-Type: application/json" -d '{"miner_address": "Minerador1"}'

# Verificar saldos
curl -X GET http://localhost:5000/balance/Alice     # -100.0
curl -X GET http://localhost:5000/balance/Bob       # 70.0 (100 - 30)
curl -X GET http://localhost:5000/balance/Charlie   # 30.0
curl -X GET http://localhost:5000/balance/Minerador1 # 10.0 (recompensa)

# Validar blockchain
curl -X GET http://localhost:5000/validate
```

## 📊 Capturas de Tela

### Mineração em Ação
```
🚀 Iniciando Blockchain do Zero...
📚 Desenvolvido por Sávio - https://github.com/SavioCodes
🌐 API rodando em: http://localhost:5000
📖 Documentação disponível no README.md
--------------------------------------------------

Minerando bloco 1...
Bloco 1 minerado em 1.23s!
Hash: 0087a2b1c4f892d3e5a7b9c2f1e4d8a6b3c9f2e5
Nonce: 12847
--------------------------------------------------

Minerando bloco 2...
Bloco 2 minerado em 3.45s!
Hash: 00f9e8d7c6b5a4938271605f4e3d2c1b0a998877
Nonce: 67234
--------------------------------------------------
```

## 🤝 Como Contribuir

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/nova-feature`)
3. **Commit** suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. **Push** para a branch (`git push origin feature/nova-feature`)
5. Abra um **Pull Request**

## 📝 Roadmap

- [ ] Interface web para interação visual
- [ ] Persistência em arquivo/banco de dados
- [ ] Rede P2P entre múltiplas instâncias
- [ ] Smart contracts básicos
- [ ] Carteira digital
- [ ] Dashboard com métricas avançadas

## ❓ FAQ

**P: Por que os saldos ficam negativos?**
R: Alice começa sem saldo e faz uma transação de 100. Por isso fica com -100. Em uma blockchain real, seria verificado se há saldo suficiente.

**P: Como funciona a mineração?**
R: O algoritmo tenta encontrar um hash que comece com zeros (definido pela dificuldade). Quanto mais zeros, mais difícil e demorado.

**P: Posso usar em produção?**
R: Este é um projeto educativo. Para produção, considere frameworks como Hyperledger ou Ethereum.

## 🐛 Problemas Conhecidos

- Não há verificação de saldo antes das transações
- Não há persistência (dados são perdidos ao reiniciar)
- Mineração pode ser lenta com alta dificuldade

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Sávio** 
- GitHub: [@SavioCodes](https://github.com/SavioCodes)

---

⭐ **Gostou do projeto? Deixe uma star!** ⭐

**Blockchain do Zero** - Aprendendo blockchain na prática! 🚀
