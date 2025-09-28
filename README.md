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

### 🎯 Modo Fácil - Interface CLI

Para usar a blockchain de forma mais simples, use a interface de linha de comando:

```bash
# Em um terminal, inicie a API:
python run.py

# Em outro terminal, use a CLI:
python blockchain_cli.py
```

### 🚀 Exemplo Rápido

Execute o exemplo prático completo:

```bash
# Terminal 1: API
python run.py

# Terminal 2: Exemplo
python exemplo_simples.py
```

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
| `GET` | `/` | Página inicial com instruções |
| `GET` | `/blockchain` | Retorna toda a blockchain |
| `GET` | `/blocks/<index>` | Retorna um bloco específico |
| `GET` | `/transactions` | Lista todas as transações |
| `POST` | `/transactions` | Adiciona nova transação |
| `POST` | `/mine` | Minera um novo bloco |
| `GET` | `/balance/<address>` | Consulta saldo de endereço |
| `GET` | `/validate` | Valida a blockchain |
| `GET` | `/stats` | Estatísticas da blockchain |
| `GET` | `/debug/print` | Imprime blockchain no terminal |

## 🎮 Formas de Usar

### 1. Interface CLI (Mais Fácil)
```bash
python blockchain_cli.py
```

### 2. Exemplo Automático
```bash
python exemplo_simples.py
```

### 3. Comandos curl (Manual)
```bash
curl -X GET http://localhost:5000/
```

## 💡 Exemplos de Uso

### 🌐 Acessando a API

Primeiro, acesse a página inicial:

```bash
curl -X GET http://localhost:5000/
```

**Resposta:**
```json
{
  "message": "🔗 Blockchain do Zero - API",
  "author": "Sávio - https://github.com/SavioCodes",
  "endpoints": {...},
  "example_transaction": {...}
}
```

### 1. Consultando a Blockchain

```bash
curl -X GET http://localhost:5000/blockchain
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

### 3. Minerando um Bloco

```bash
curl -X POST http://localhost:5000/mine \
  -H "Content-Type: application/json" \
  -d '{"miner_address": "Minerador1"}'
```

**Saída no Terminal da API:**
```
⛏️  Minerando bloco 1... (Dificuldade: 1)
✅ Bloco 1 minerado com sucesso!
   ⏱️  Tempo: 0.02s
   🔑 Hash: 0a1b2c3d4e5f6789012345678901234567890
   🎲 Nonce: 156
   📦 Transações: 2
   --------------------------------------------------
```

### 4. Consultando Saldo

```bash
curl -X GET http://localhost:5000/balance/Alice
```

### 5. Validando a Blockchain

```bash
curl -X GET http://localhost:5000/validate
```

### 6. Visualização Completa

```bash
curl -X GET http://localhost:5000/debug/print
```

Isso imprimirá no terminal da API uma visualização completa e organizada da blockchain.

## 🔧 Personalização

### Ajustando a Dificuldade

No arquivo `src/blockchain.py`, altere o valor:

```python
self.difficulty = 2  # Aumenta a dificuldade (mais zeros no hash)
```

### Modificando a Recompensa

```python
self.mining_reward = 25  # Recompensa de 25 por bloco minerado
```

## 🧪 Teste Completo Automático

### Opção 1: Exemplo Automático
```bash
# Terminal 1: Inicie a API
python run.py

# Terminal 2: Execute o exemplo
python exemplo_simples.py
```

### Opção 2: Interface Interativa
```bash
# Terminal 1: Inicie a API
python run.py

# Terminal 2: Use a CLI
python blockchain_cli.py
```

### Opção 3: Comandos Manuais

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

# Ver visualização completa
curl -X GET http://localhost:5000/debug/print
```

## 📊 Capturas de Tela

### Mineração em Ação
```
🚀 Iniciando Blockchain do Zero...
📚 Desenvolvido por Sávio - https://github.com/SavioCodes
🌐 API rodando em: http://localhost:5000
📖 Documentação disponível no README.md
--------------------------------------------------

⛏️  Minerando bloco 1... (Dificuldade: 1)
✅ Bloco 1 minerado com sucesso!
   ⏱️  Tempo: 0.05s
   🔑 Hash: 0a87b2c1d4f892e3f5a7b9c2f1e4d8a6b3c9f2e5
   🎲 Nonce: 234
   📦 Transações: 2
   --------------------------------------------------

⛏️  Minerando bloco 2... (Dificuldade: 1)
✅ Bloco 2 minerado com sucesso!
   ⏱️  Tempo: 0.12s
   🔑 Hash: 0f9e8d7c6b5a4938271605f4e3d2c1b0a998877
   🎲 Nonce: 891
   📦 Transações: 3
   --------------------------------------------------
```

### Interface CLI
```
🔗 BLOCKCHAIN DO ZERO - CLI
📚 Desenvolvido por Sávio - https://github.com/SavioCodes
============================================================

📋 OPÇÕES DISPONÍVEIS:
1. 📖 Ver blockchain completa
2. 📦 Ver bloco específico
3. 💸 Adicionar transação
4. ⛏️  Minerar bloco
5. 💰 Ver saldo
6. ✅ Validar blockchain
7. 📊 Ver estatísticas
8. 🖨️  Imprimir blockchain (debug)
9. ❌ Sair

🔢 Escolha uma opção (1-9):
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
R: O algoritmo tenta encontrar um hash que comece com zeros (definido pela dificuldade). A dificuldade padrão é 1 para testes rápidos.

**P: Posso usar em produção?**
R: Este é um projeto educativo. Para produção, considere frameworks como Hyperledger ou Ethereum.

**P: Como usar de forma mais fácil?**
R: Use `python blockchain_cli.py` para uma interface amigável ou `python exemplo_simples.py` para ver tudo funcionando automaticamente.

## 🐛 Problemas Conhecidos

- Não há verificação de saldo antes das transações
- Não há persistência (dados são perdidos ao reiniciar)
- Dificuldade baixa (1) para facilitar testes

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Sávio** 
- GitHub: [@SavioCodes](https://github.com/SavioCodes)

---

⭐ **Gostou do projeto? Deixe uma star!** ⭐

**Blockchain do Zero** - Aprendendo blockchain na prática! 🚀
