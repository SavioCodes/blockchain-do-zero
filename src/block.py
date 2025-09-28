"""
Módulo para representar blocos na blockchain.
"""
import hashlib
import json
from datetime import datetime
from typing import List, Union
from .transaction import Transaction


class Block:
    """
    Representa um bloco na blockchain.
    """
    
    def __init__(self, index: int, transactions: List[Transaction], previous_hash: str, timestamp: datetime = None):
        """
        Inicializa um novo bloco.
        
        Args:
            index (int): Índice do bloco na chain
            transactions (List[Transaction]): Lista de transações do bloco
            previous_hash (str): Hash do bloco anterior
            timestamp (datetime, optional): Timestamp do bloco
        """
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = timestamp or datetime.now()
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """
        Calcula o hash SHA-256 do bloco.
        
        Returns:
            str: Hash SHA-256 do bloco
        """
        # Converte as transações para string
        transactions_str = json.dumps([tx.to_dict() for tx in self.transactions], 
                                    sort_keys=True, ensure_ascii=False)
        
        # Cria a string do bloco
        block_string = f"{self.index}{transactions_str}{self.previous_hash}{self.timestamp.isoformat()}{self.nonce}"
        
        # Calcula o hash SHA-256
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()
    
    def mine_block(self, difficulty: int) -> None:
        """
        Minera o bloco usando Proof of Work.
        
        Args:
            difficulty (int): Dificuldade da mineração (número de zeros no início do hash)
        """
        target = "0" * difficulty
        
        print(f"⛏️  Minerando bloco {self.index}... (Dificuldade: {difficulty})")
        start_time = datetime.now()
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            
            # Mostra progresso a cada 10000 tentativas
            if self.nonce % 10000 == 0:
                print(f"   Tentativa {self.nonce}... (Hash atual: {self.hash[:16]}...)")
        
        end_time = datetime.now()
        mining_time = (end_time - start_time).total_seconds()
        
        print(f"✅ Bloco {self.index} minerado com sucesso!")
        print(f"   ⏱️  Tempo: {mining_time:.2f}s")
        print(f"   🔑 Hash: {self.hash}")
        print(f"   🎲 Nonce: {self.nonce}")
        print(f"   📦 Transações: {len(self.transactions)}")
        print("   " + "-" * 50)
    
    def is_valid(self) -> bool:
        """
        Verifica se o bloco é válido.
        
        Returns:
            bool: True se o bloco é válido, False caso contrário
        """
        return self.hash == self.calculate_hash()
    
    def to_dict(self) -> dict:
        """
        Converte o bloco para dicionário.
        
        Returns:
            dict: Representação do bloco em dicionário
        """
        return {
            'index': self.index,
            'timestamp': self.timestamp.isoformat(),
            'transactions': [tx.to_dict() for tx in self.transactions],
            'previous_hash': self.previous_hash,
            'hash': self.hash,
            'nonce': self.nonce
        }
    
    def to_json(self) -> str:
        """
        Converte o bloco para JSON.
        
        Returns:
            str: Representação do bloco em JSON
        """
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
