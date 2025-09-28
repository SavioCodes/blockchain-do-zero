"""
Testes para a classe Transaction.
"""
import pytest
from datetime import datetime
from src.transaction import Transaction


class TestTransaction:
    """
    Classe de testes para Transaction.
    """
    
    def test_transaction_creation(self):
        """
        Testa a criação de uma transação.
        """
        transaction = Transaction("Alice", "Bob", 50.0)
        
        assert transaction.sender == "Alice"
        assert transaction.recipient == "Bob"
        assert transaction.amount == 50.0
        assert isinstance(transaction.timestamp, datetime)
    
    def test_transaction_with_custom_timestamp(self):
        """
        Testa a criação de uma transação com timestamp customizado.
        """
        custom_timestamp = datetime(2024, 1, 1, 12, 0, 0)
        transaction = Transaction("Alice", "Bob", 25.0, custom_timestamp)
        
        assert transaction.timestamp == custom_timestamp
    
    def test_transaction_to_dict(self):
        """
        Testa a conversão da transação para dicionário.
        """
        transaction = Transaction("Alice", "Bob", 75.0)
        tx_dict = transaction.to_dict()
        
        assert tx_dict['sender'] == "Alice"
        assert tx_dict['recipient'] == "Bob"
        assert tx_dict['amount'] == 75.0
        assert 'timestamp' in tx_dict
    
    def test_transaction_to_json(self):
        """
        Testa a conversão da transação para JSON.
        """
        transaction = Transaction("Alice", "Bob", 100.0)
        json_str = transaction.to_json()
        
        assert isinstance(json_str, str)
        assert "Alice" in json_str
        assert "Bob" in json_str
        assert "100.0" in json_str
    
    def test_transaction_str_representation(self):
        """
        Testa a representação em string da transação.
        """
        transaction = Transaction("Alice", "Bob", 150.0)
        str_repr = str(transaction)
        
        assert str_repr == "Alice -> Bob: 150.0"
