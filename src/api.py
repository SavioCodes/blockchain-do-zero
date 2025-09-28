"""
API Flask para interagir com a blockchain.
"""
from flask import Flask, jsonify, request
from datetime import datetime
from .blockchain import Blockchain
from .transaction import Transaction

app = Flask(__name__)

# Instância global da blockchain
blockchain = Blockchain()


@app.route('/', methods=['GET'])
def home():
    """
    Página inicial da API.
    """
    return jsonify({
        'message': '🔗 Blockchain do Zero - API',
        'author': 'Sávio - https://github.com/SavioCodes',
        'endpoints': {
            'GET /': 'Esta página',
            'GET /blockchain': 'Ver blockchain completa',
            'GET /blocks/<index>': 'Ver bloco específico',
            'GET /transactions': 'Ver todas as transações',
            'POST /transactions': 'Adicionar nova transação',
            'POST /mine': 'Minerar novo bloco',
            'GET /balance/<address>': 'Ver saldo de endereço',
            'GET /validate': 'Validar blockchain',
            'GET /stats': 'Ver estatísticas'
        },
        'example_transaction': {
            'sender': 'Alice',
            'recipient': 'Bob',
            'amount': 50.0
        },
        'example_mine': {
            'miner_address': 'Minerador1'
        }
    }), 200


@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    """
    Retorna toda a blockchain.
    
    Returns:
        JSON: Blockchain completa
    """
    print("📖 Consultando blockchain completa...")
    return jsonify(blockchain.to_dict()), 200


@app.route('/blocks/<int:index>', methods=['GET'])
def get_block(index):
    """
    Retorna um bloco específico pelo índice.
    
    Args:
        index (int): Índice do bloco
        
    Returns:
        JSON: Bloco encontrado ou erro
    """
    print(f"🔍 Buscando bloco {index}...")
    block = blockchain.get_block_by_index(index)
    if block:
        print(f"✅ Bloco {index} encontrado!")
        return jsonify(block.to_dict()), 200
    else:
        print(f"❌ Bloco {index} não encontrado!")
        return jsonify({'error': 'Bloco não encontrado'}), 404


@app.route('/transactions', methods=['GET'])
def get_transactions():
    """
    Retorna todas as transações da blockchain.
    
    Returns:
        JSON: Lista de todas as transações
    """
    print("📋 Listando todas as transações...")
    transactions = blockchain.get_all_transactions()
    return jsonify([tx.to_dict() for tx in transactions]), 200


@app.route('/transactions', methods=['POST'])
def add_transaction():
    """
    Adiciona uma nova transação à blockchain.
    
    Returns:
        JSON: Confirmação da transação adicionada
    """
    data = request.get_json()
    
    # Valida os dados da requisição
    if not data or 'sender' not in data or 'recipient' not in data or 'amount' not in data:
        print("❌ Dados de transação inválidos!")
        return jsonify({'error': 'Dados inválidos. Campos obrigatórios: sender, recipient, amount'}), 400
    
    try:
        amount = float(data['amount'])
        if amount <= 0:
            print("❌ Valor da transação deve ser positivo!")
            return jsonify({'error': 'O valor deve ser positivo'}), 400
    except ValueError:
        print("❌ Valor da transação inválido!")
        return jsonify({'error': 'Valor inválido'}), 400
    
    # Cria e adiciona a transação
    transaction = Transaction(
        sender=data['sender'],
        recipient=data['recipient'],
        amount=amount
    )
    
    blockchain.add_transaction(transaction)
    print(f"✅ Nova transação adicionada: {transaction.sender} → {transaction.recipient}: {transaction.amount}")
    
    return jsonify({
        'message': 'Transação adicionada com sucesso',
        'transaction': transaction.to_dict(),
        'pending_transactions': len(blockchain.pending_transactions)
    }), 201


@app.route('/mine', methods=['POST'])
def mine_block():
    """
    Minera um novo bloco com as transações pendentes.
    
    Returns:
        JSON: Informações do bloco minerado
    """
    data = request.get_json()
    
    if not data or 'miner_address' not in data:
        print("❌ Endereço do minerador não fornecido!")
        return jsonify({'error': 'Endereço do minerador é obrigatório'}), 400
    
    miner_address = data['miner_address']
    
    if not blockchain.pending_transactions:
        print("❌ Não há transações pendentes para minerar!")
        return jsonify({'error': 'Não há transações pendentes para minerar'}), 400
    
    print(f"🚀 Iniciando mineração para {miner_address}...")
    print(f"📋 Transações pendentes: {len(blockchain.pending_transactions)}")
    
    # Minera o bloco
    new_block = blockchain.mine_pending_transactions(miner_address)
    
    print(f"🎉 Mineração concluída! Novo saldo do minerador: {blockchain.get_balance(miner_address)}")
    
    return jsonify({
        'message': 'Bloco minerado com sucesso',
        'block': new_block.to_dict(),
        'miner_balance': blockchain.get_balance(miner_address)
    }), 200


@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    """
    Retorna o saldo de um endereço.
    
    Args:
        address (str): Endereço para consultar o saldo
        
    Returns:
        JSON: Saldo do endereço
    """
    balance = blockchain.get_balance(address)
    print(f"💰 Saldo de {address}: {balance}")
    return jsonify({
        'address': address,
        'balance': balance
    }), 200


@app.route('/validate', methods=['GET'])
def validate_blockchain():
    """
    Valida a integridade da blockchain.
    
    Returns:
        JSON: Resultado da validação
    """
    print("🔍 Validando integridade da blockchain...")
    is_valid = blockchain.is_chain_valid()
    status = "✅ Blockchain válida!" if is_valid else "❌ Blockchain inválida!"
    print(status)
    return jsonify({
        'is_valid': is_valid,
        'message': 'Blockchain válida' if is_valid else 'Blockchain inválida'
    }), 200


@app.route('/stats', methods=['GET'])
def get_stats():
    """
    Retorna estatísticas da blockchain.
    
    Returns:
        JSON: Estatísticas da blockchain
    """
    total_blocks = len(blockchain.chain)
    total_transactions = sum(len(block.transactions) for block in blockchain.chain)
    pending_transactions = len(blockchain.pending_transactions)
    
    print("📊 Consultando estatísticas da blockchain...")
    
    return jsonify({
        'total_blocks': total_blocks,
        'total_transactions': total_transactions,
        'pending_transactions': pending_transactions,
        'difficulty': blockchain.difficulty,
        'mining_reward': blockchain.mining_reward
    }), 200


@app.route('/debug/print', methods=['GET'])
def debug_print():
    """
    Imprime a blockchain no terminal (para debug).
    """
    blockchain.print_blockchain()
    blockchain.print_balances()
    return jsonify({'message': 'Blockchain impressa no terminal'}), 200


@app.errorhandler(404)
def not_found(error):
    """
    Handler para erro 404.
    """
    return jsonify({'error': 'Endpoint não encontrado'}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handler para erro 500.
    """
    return jsonify({'error': 'Erro interno do servidor'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
