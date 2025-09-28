#!/usr/bin/env python3
"""
Exemplo simples de uso da blockchain.
Execute este arquivo para ver a blockchain funcionando!
"""
import requests
import json
import time

BASE_URL = "http://localhost:5000"

def print_separator(title):
    """Imprime um separador com título."""
    print("\n" + "="*60)
    print(f"🔗 {title}")
    print("="*60)

def check_api():
    """Verifica se a API está rodando."""
    try:
        response = requests.get(f"{BASE_URL}/", timeout=2)
        return response.status_code == 200
    except:
        return False

def main():
    """Exemplo completo de uso da blockchain."""
    print_separator("BLOCKCHAIN DO ZERO - EXEMPLO PRÁTICO")
    print("📚 Desenvolvido por Sávio - https://github.com/SavioCodes")
    
    # Verifica se a API está rodando
    if not check_api():
        print("\n❌ ERRO: API não está rodando!")
        print("   Execute em outro terminal: python run.py")
        return
    
    print("\n✅ API conectada com sucesso!")
    
    # 1. Consultar blockchain inicial
    print_separator("1. BLOCKCHAIN INICIAL")
    response = requests.get(f"{BASE_URL}/stats")
    stats = response.json()
    print(f"📦 Blocos: {stats['total_blocks']}")
    print(f"💸 Transações: {stats['total_transactions']}")
    print(f"⏳ Pendentes: {stats['pending_transactions']}")
    
    # 2. Adicionar transações
    print_separator("2. ADICIONANDO TRANSAÇÕES")
    
    transactions = [
        {"sender": "Alice", "recipient": "Bob", "amount": 100.0},
        {"sender": "Bob", "recipient": "Charlie", "amount": 30.0},
        {"sender": "Alice", "recipient": "Charlie", "amount": 25.0}
    ]
    
    for tx in transactions:
        response = requests.post(f"{BASE_URL}/transactions", json=tx)
        if response.status_code == 201:
            print(f"✅ {tx['sender']} → {tx['recipient']}: {tx['amount']}")
        else:
            print(f"❌ Erro ao adicionar transação")
    
    # 3. Verificar transações pendentes
    print_separator("3. TRANSAÇÕES PENDENTES")
    response = requests.get(f"{BASE_URL}/stats")
    stats = response.json()
    print(f"⏳ Transações pendentes: {stats['pending_transactions']}")
    
    # 4. Minerar bloco
    print_separator("4. MINERANDO BLOCO")
    print("⛏️  Iniciando mineração...")
    
    mine_data = {"miner_address": "Minerador1"}
    response = requests.post(f"{BASE_URL}/mine", json=mine_data)
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Bloco minerado com sucesso!")
        print(f"   Hash: {result['block']['hash'][:32]}...")
        print(f"   Nonce: {result['block']['nonce']}")
        print(f"   Saldo do minerador: {result['miner_balance']}")
    else:
        print("❌ Erro na mineração")
    
    # 5. Verificar saldos
    print_separator("5. SALDOS FINAIS")
    
    addresses = ["Alice", "Bob", "Charlie", "Minerador1"]
    for address in addresses:
        response = requests.get(f"{BASE_URL}/balance/{address}")
        if response.status_code == 200:
            balance = response.json()['balance']
            emoji = "💚" if balance > 0 else "❌" if balance < 0 else "⚪"
            print(f"{emoji} {address}: {balance}")
    
    # 6. Validar blockchain
    print_separator("6. VALIDAÇÃO DA BLOCKCHAIN")
    response = requests.get(f"{BASE_URL}/validate")
    if response.status_code == 200:
        result = response.json()
        if result['is_valid']:
            print("✅ Blockchain válida!")
        else:
            print("❌ Blockchain inválida!")
    
    # 7. Estatísticas finais
    print_separator("7. ESTATÍSTICAS FINAIS")
    response = requests.get(f"{BASE_URL}/stats")
    stats = response.json()
    print(f"📦 Total de blocos: {stats['total_blocks']}")
    print(f"💸 Total de transações: {stats['total_transactions']}")
    print(f"⏳ Transações pendentes: {stats['pending_transactions']}")
    
    # 8. Imprimir blockchain no terminal da API
    print_separator("8. VISUALIZAÇÃO COMPLETA")
    print("🖨️  Imprimindo blockchain no terminal da API...")
    requests.get(f"{BASE_URL}/debug/print")
    
    print_separator("EXEMPLO CONCLUÍDO")
    print("🎉 Blockchain funcionando perfeitamente!")
    print("💡 Use 'python blockchain_cli.py' para interface interativa")
    print("📖 Ou consulte o README.md para mais exemplos")

if __name__ == "__main__":
    main()
