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


@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    """
    Retorna toda a blockchain.
    
    Returns:
        JSON: Blockchain completa
    """
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
    block = blockchain.get_block_by_index(index)
    if block:
        return jsonify(block.to_dict()), 200
    else:
        return jsonify({'error': 'Bloco não encontrado'}), 404


@app.route('/transactions', methods=['GET'])
def get_transactions():
    """
    Retorna todas as transações da blockchain.
    
    Returns:
        JSON: Lista de todas as transações
    """
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
        return jsonify({'error': 'Dados inválidos. Campos obrigatórios: sender, recipient, amount'}), 400
    
    try:
        amount = float(data['amount'])
        if amount <= 0:
            return jsonify({'error': 'O valor deve ser positivo'}), 400
    except ValueError:
        return jsonify({'error': 'Valor inválido'}), 400
    
    # Cria e adiciona a transação
    transaction = Transaction(
        sender=data['sender'],
        recipient=data['recipient'],
        amount=amount
    )
    
    blockchain.add_transaction(transaction)
    
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
        return jsonify({'error': 'Endereço do minerador é obrigatório'}), 400
    
    miner_address = data['miner_address']
    
    if not blockchain.pending_transactions:
        return jsonify({'error': 'Não há transações pendentes para minerar'}), 400
    
    # Minera o bloco
    new_block = blockchain.mine_pending_transactions(miner_address)
    
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
    is_valid = blockchain.is_chain_valid()
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
    
    return jsonify({
        'total_blocks': total_blocks,
        'total_transactions': total_transactions,
        'pending_transactions': pending_transactions,
        'difficulty': blockchain.difficulty,
        'mining_reward': blockchain.mining_reward
    }), 200


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
