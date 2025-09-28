
"""
Módulo para representar transações na blockchain.
"""
import json
from datetime import datetime


class Transaction:
    """
    Representa uma transação na blockchain.
    """
    
    def __init__(self, sender: str, recipient: str, amount: float, timestamp: datetime = None):
        """
        Inicializa uma nova transação.
        
        Args:
            sender (str): Endereço do remetente
            recipient (str): Endereço do destinatário
            amount (float): Valor da transação
            timestamp (datetime, optional): Timestamp da transação
        """
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = timestamp or datetime.now()
    
    def to_dict(self) -> dict:
        """
        Converte a transação para dicionário.
        
        Returns:
            dict: Representação da transação em dicionário
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp.isoformat()
        }
    
    def to_json(self) -> str:
        """
        Converte a transação para JSON.
        
        Returns:
            str: Representação da transação em JSON
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)
    
    def __str__(self) -> str:
        """
        Representação em string da transação.
        
        Returns:
            str: String formatada da transação
        """
        return f"{self.sender} -> {self.recipient}: {self.amount}"
