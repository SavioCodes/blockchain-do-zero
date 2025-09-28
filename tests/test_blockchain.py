"""
Testes para a classe Blockchain.
"""
import pytest
from src.blockchain import Blockchain
from src.transaction import Transaction


class TestBlockchain:
    """
    Classe de testes para Blockchain.
    """
    
    def test_blockchain_creation(self):
        """
        Testa a criação da blockchain.
        """
        blockchain = Blockchain()
        
        assert len(blockchain.chain) == 1  # Bloco gênesis
        assert blockchain.difficulty == 2
        assert blockchain.mining_reward == 10
        assert len(blockchain.pending_transactions) == 0
    
    def test_genesis_block(self):
        """
        Testa o bloco gênesis.
        """
        blockchain = Blockchain()
        genesis_block = blockchain.chain[0]
        
        assert genesis_block.index == 0
        assert genesis_block.previous_hash == "0"
        assert len(genesis_block.transactions) == 1
    
    def test_add_transaction(self):
        """
        Testa a adição de transações.
        """
        blockchain = Blockchain()
        transaction = Transaction("Alice", "Bob", 50.0)
        
        blockchain.add_transaction(transaction)
        
        assert len(blockchain.pending_transactions) == 1
        assert blockchain.pending_transactions[0] == transaction
    
    def test_mine_pending_transactions(self):
        """
        Testa a mineração de transações pendentes.
        """
        blockchain = Blockchain()
        transaction = Transaction("Alice", "Bob", 50.0)
        blockchain.add_transaction(transaction)
        
        miner_address = "Miner1"
        new_block = blockchain.mine_pending_transactions(miner_address)
        
        assert len(blockchain.chain) == 2
        assert len(blockchain.pending_transactions) == 0
        assert new_block.index == 1
        # Deve haver 2 transações: a original + a recompensa
        assert len(new_block.transactions) == 2
    
    def test_get_balance(self):
        """
        Testa o cálculo de saldo.
        """
        blockchain = Blockchain()
        
        # Adiciona transações
        blockchain.add_transaction(Transaction("Alice", "Bob", 50.0))
        blockchain.add_transaction(Transaction("Alice", "Charlie", 25.0))
        blockchain.mine_pending_transactions("Miner1")
        
        # Alice enviou 75, então deveria ter -75
        assert blockchain.get_balance("Alice") == -75.0
        # Bob recebeu 50
        assert blockchain.get_balance("Bob") == 50.0
        # Charlie recebeu 25
        assert blockchain.get_balance("Charlie") == 25.0
        # Miner1 recebeu a recompensa
        assert blockchain.get_balance("Miner1") == 10.0
    
    def test_chain_validation(self):
        """
        Testa a validação da blockchain.
        """
        blockchain = Blockchain()
        
        # Blockchain inicial deve ser válida
        assert blockchain.is_chain_valid() == True
        
        # Adiciona e minera um bloco
        blockchain.add_transaction(Transaction("Alice", "Bob", 50.0))
        blockchain.mine_pending_transactions("Miner1")
        
        # Blockchain ainda deve ser válida
        assert blockchain.is_chain_valid() == True
        
        # Corrompe um bloco
        blockchain.chain[1].hash = "invalid_hash"
        
        # Blockchain deve ser inválida
        assert blockchain.is_chain_valid() == False
    
    def test_get_block_by_index(self):
        """
        Testa a obtenção de bloco por índice.
        """
        blockchain = Blockchain()
        
        # Teste com índice válido
        block = blockchain.get_block_by_index(0)
        assert block is not None
        assert block.index == 0
        
        # Teste com índice inválido
        block = blockchain.get_block_by_index(999)
        assert block is None
