"""
Testes para a classe Block.
"""
import pytest
from datetime import datetime
from src.block import Block
from src.transaction import Transaction


class TestBlock:
    """
    Classe de testes para Block.
    """
    
    def test_block_creation(self):
        """
        Testa a criação de um bloco.
        """
        transactions = [Transaction("Alice", "Bob", 50.0)]
        block = Block(1, transactions, "previous_hash")
        
        assert block.index == 1
        assert len(block.transactions) == 1
        assert block.previous_hash == "previous_hash"
        assert isinstance(block.timestamp, datetime)
        assert block.nonce == 0
        assert block.hash is not None
    
    def test_block_hash_calculation(self):
        """
        Testa o cálculo do hash do bloco.
        """
        transactions = [Transaction("Alice", "Bob", 50.0)]
        block = Block(1, transactions, "previous_hash")
        
        initial_hash = block.hash
        recalculated_hash = block.calculate_hash()
        
        assert initial_hash == recalculated_hash
    
    def test_block_mining(self):
        """
        Testa a mineração do bloco.
        """
        transactions = [Transaction("Alice", "Bob", 50.0)]
        block = Block(1, transactions, "previous_hash")
        
        difficulty = 2
        block.mine_block(difficulty)
        
        assert block.hash.startswith("0" * difficulty)
        assert block.nonce > 0
    
    def test_block_validation(self):
        """
        Testa a validação do bloco.
        """
        transactions = [Transaction("Alice", "Bob", 50.0)]
        block = Block(1, transactions, "previous_hash")
        
        assert block.is_valid() == True
        
        # Modifica o hash manualmente para torná-lo inválido
        block.hash = "invalid_hash"
        assert block.is_valid() == False
    
    def test_block_to_dict(self):
        """
        Testa a conversão do bloco para dicionário.
        """
        transactions = [Transaction("Alice", "Bob", 50.0)]
        block = Block(1, transactions, "previous_hash")
        block_dict = block.to_dict()
        
        assert block_dict['index'] == 1
        assert block_dict['previous_hash'] == "previous_hash"
        assert len(block_dict['transactions']) == 1
        assert 'timestamp' in block_dict
        assert 'hash' in block_dict
        assert 'nonce' in block_dict
