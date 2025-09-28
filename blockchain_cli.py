#!/usr/bin/env python3
"""
Interface de linha de comando para a blockchain.
Facilita o uso da blockchain sem precisar usar curl.
"""
import requests
import json
import sys
from datetime import datetime

BASE_URL = "http://localhost:5000"

def print_header():
    """Imprime o cabeçalho da CLI."""
    print("\n" + "="*60)
    print("🔗 BLOCKCHAIN DO ZERO - CLI")
    print("📚 Desenvolvido por Sávio - https://github.com/SavioCodes")
    print("="*60)

def print_menu():
    """Imprime o menu de opções."""
    print("\n📋 OPÇÕES DISPONÍVEIS:")
    print("1. 📖 Ver blockchain completa")
    print("2. 📦 Ver bloco específico")
    print("3. 💸 Adicionar transação")
    print("4. ⛏️  Minerar bloco")
    print("5. 💰 Ver saldo")
    print("6. ✅ Validar blockchain")
    print("7. 📊 Ver estatísticas")
    print("8. 🖨️  Imprimir blockchain (debug)")
    print("9. ❌ Sair")

def check_api():
    """Verifica se a API está rodando."""
    try:
        response = requests.get(f"{BASE_URL}/", timeout=2)
        return response.status_code == 200
    except:
        return False

def get_blockchain():
    """Consulta a blockchain completa."""
    try:
        response = requests.get(f"{BASE_URL}/blockchain")
        if response.status_code == 200:
            data = response.json()
            print(f"\n✅ Blockchain com {len(data['chain'])} blocos:")
            for i, block in enumerate(data['chain']):
                print(f"   📦 Bloco {i}: {len(block['transactions'])} transações")
                print(f"      Hash: {block['hash'][:32]}...")
        else:
            print("❌ Erro ao consultar blockchain")
    except Exception as e:
        print(f"❌ Erro: {e}")

def get_block():
    """Consulta um bloco específico."""
    try:
        index = int(input("📦 Digite o índice do bloco: "))
        response = requests.get(f"{BASE_URL}/blocks/{index}")
        if response.status_code == 200:
            block = response.json()
            print(f"\n✅ Bloco {block['index']}:")
            print(f"   Hash: {block['hash']}")
            print(f"   Hash Anterior: {block['previous_hash']}")
            print(f"   Timestamp: {block['timestamp']}")
            print(f"   Nonce: {block['nonce']}")
            print(f"   Transações: {len(block['transactions'])}")
            for i, tx in enumerate(block['transactions']):
                print(f"      {i+1}. {tx['sender']} → {tx['recipient']}: {tx['amount']}")
        else:
            print("❌ Bloco não encontrado")
    except ValueError:
        print("❌ Índice inválido")
    except Exception as e:
        print(f"❌ Erro: {e}")

def add_transaction():
    """Adiciona uma nova transação."""
    try:
        print("\n💸 NOVA TRANSAÇÃO:")
        sender = input("   Remetente: ")
        recipient = input("   Destinatário: ")
        amount = float(input("   Valor: "))
        
        data = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        
        response = requests.post(f"{BASE_URL}/transactions", json=data)
        if response.status_code == 201:
            result = response.json()
            print(f"✅ Transação adicionada com sucesso!")
            print(f"   {sender} → {recipient}: {amount}")
            print(f"   Transações pendentes: {result['pending_transactions']}")
        else:
            print("❌ Erro ao adicionar transação")
    except ValueError:
        print("❌ Valor inválido")
    except Exception as e:
        print(f"❌ Erro: {e}")

def mine_block():
    """Minera um novo bloco."""
    try:
        miner = input("⛏️  Digite o endereço do minerador: ")
        
        data = {"miner_address": miner}
        
        print("🚀 Iniciando mineração...")
        response = requests.post(f"{BASE_URL}/mine", json=data)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Bloco minerado com sucesso!")
            print(f"   Minerador: {miner}")
            print(f"   Novo saldo: {result['miner_balance']}")
            print(f"   Hash do bloco: {result['block']['hash'][:32]}...")
        else:
            error = response.json()
            print(f"❌ Erro: {error['error']}")
    except Exception as e:
        print(f"❌ Erro: {e}")

def get_balance():
    """Consulta o saldo de um endereço."""
    try:
        address = input("💰 Digite o endereço: ")
        response = requests.get(f"{BASE_URL}/balance/{address}")
        if response.status_code == 200:
            result = response.json()
            balance = result['balance']
            emoji = "💚" if balance > 0 else "❌" if balance < 0 else "⚪"
            print(f"{emoji} Saldo de {address}: {balance}")
        else:
            print("❌ Erro ao consultar saldo")
    except Exception as e:
        print(f"❌ Erro: {e}")

def validate_blockchain():
    """Valida a blockchain."""
    try:
        response = requests.get(f"{BASE_URL}/validate")
        if response.status_code == 200:
            result = response.json()
            if result['is_valid']:
                print("✅ Blockchain válida!")
            else:
                print("❌ Blockchain inválida!")
        else:
            print("❌ Erro ao validar blockchain")
    except Exception as e:
        print(f"❌ Erro: {e}")

def get_stats():
    """Consulta estatísticas da blockchain."""
    try:
        response = requests.get(f"{BASE_URL}/stats")
        if response.status_code == 200:
            stats = response.json()
            print("\n📊 ESTATÍSTICAS:")
            print(f"   📦 Total de blocos: {stats['total_blocks']}")
            print(f"   💸 Total de transações: {stats['total_transactions']}")
            print(f"   ⏳ Transações pendentes: {stats['pending_transactions']}")
            print(f"   ⚙️  Dificuldade: {stats['difficulty']}")
            print(f"   💰 Recompensa de mineração: {stats['mining_reward']}")
        else:
            print("❌ Erro ao consultar estatísticas")
    except Exception as e:
        print(f"❌ Erro: {e}")

def debug_print():
    """Imprime a blockchain no terminal da API."""
    try:
        response = requests.get(f"{BASE_URL}/debug/print")
        if response.status_code == 200:
            print("✅ Blockchain impressa no terminal da API!")
        else:
            print("❌ Erro ao imprimir blockchain")
    except Exception as e:
        print(f"❌ Erro: {e}")

def main():
    """Função principal da CLI."""
    print_header()
    
    # Verifica se a API está rodando
    if not check_api():
        print("❌ API não está rodando!")
        print("   Execute: python run.py")
        sys.exit(1)
    
    print("✅ API conectada com sucesso!")
    
    while True:
        print_menu()
        try:
            choice = input("\n🔢 Escolha uma opção (1-9): ").strip()
            
            if choice == "1":
                get_blockchain()
            elif choice == "2":
                get_block()
            elif choice == "3":
                add_transaction()
            elif choice == "4":
                mine_block()
            elif choice == "5":
                get_balance()
            elif choice == "6":
                validate_blockchain()
            elif choice == "7":
                get_stats()
            elif choice == "8":
                debug_print()
            elif choice == "9":
                print("\n👋 Até logo!")
                break
            else:
                print("❌ Opção inválida!")
                
        except KeyboardInterrupt:
            print("\n\n👋 Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
