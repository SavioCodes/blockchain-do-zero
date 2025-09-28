"""
Módulo principal da blockchain.
"""
from datetime import datetime
from typing import List, Optional
from .block import Block
from .transaction import Transaction


class Blockchain:
    """
    Implementação de uma blockchain simples.
    """
    
    def __init__(self):
        """
        Inicializa a blockchain com o bloco gênesis.
        """
        self.chain: List[Block] = []
        self.difficulty = 2  # Dificuldade da mineração
        self.pending_transactions: List[Transaction] = []
        self.mining_reward = 10  # Recompensa por minerar um bloco
        
        # Cria o bloco gênesis
        self.create_genesis_block()
    
    def create_genesis_block(self) -> None:
        """
        Cria o primeiro bloco (bloco gênesis) da blockchain.
        """
        genesis_transaction = Transaction("Genesis", "Genesis", 0)
        genesis_block = Block(0, [genesis_transaction], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> Block:
        """
        Retorna o último bloco da chain.
        
        Returns:
            Block: Último bloco da chain
        """
        return self.chain[-1]
    
    def add_transaction(self, transaction: Transaction) -> None:
        """
        Adiciona uma transação à lista de transações pendentes.
        
        Args:
            transaction (Transaction): Transação a ser adicionada
        """
        self.pending_transactions.append(transaction)
    
    def mine_pending_transactions(self, mining_reward_address: str) -> Block:
        """
        Minera todas as transações pendentes e adiciona um novo bloco à chain.
        
        Args:
            mining_reward_address (str): Endereço que receberá a recompensa da mineração
            
        Returns:
            Block: Novo bloco minerado
        """
        # Adiciona a transação de recompensa
        reward_transaction = Transaction(None, mining_reward_address, self.mining_reward)
        self.pending_transactions.append(reward_transaction)
        
        # Cria um novo bloco
        new_block = Block(
            len(self.chain),
            self.pending_transactions,
            self.get_latest_block().hash
        )
        
        # Minera o bloco
        new_block.mine_block(self.difficulty)
        
        # Adiciona o bloco à chain
        self.chain.append(new_block)
        
        # Limpa as transações pendentes
        self.pending_transactions = []
        
        return new_block
    
    def get_balance(self, address: str) -> float:
        """
        Calcula o saldo de um endereço.
        
        Args:
            address (str): Endereço para calcular o saldo
            
        Returns:
            float: Saldo do endereço
        """
        balance = 0
        
        # Percorre todos os blocos da chain
        for block in self.chain:
            for transaction in block.transactions:
                # Se o endereço é o remetente, subtrai o valor
                if transaction.sender == address:
                    balance -= transaction.amount
                
                # Se o endereço é o destinatário, adiciona o valor
                if transaction.recipient == address:
                    balance += transaction.amount
        
        return balance
    
    def is_chain_valid(self) -> bool:
        """
        Valida toda a blockchain.
        
        Returns:
            bool: True se a chain é válida, False caso contrário
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verifica se o bloco atual é válido
            if not current_block.is_valid():
                print(f"Bloco {current_block.index} é inválido!")
                return False
            
            # Verifica se o hash anterior está correto
            if current_block.previous_hash != previous_block.hash:
                print(f"Bloco {current_block.index} tem hash anterior incorreto!")
                return False
        
        return True
    
    def get_block_by_index(self, index: int) -> Optional[Block]:
        """
        Retorna um bloco pelo índice.
        
        Args:
            index (int): Índice do bloco
            
        Returns:
            Optional[Block]: Bloco encontrado ou None
        """
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None
    
    def get_all_transactions(self) -> List[Transaction]:
        """
        Retorna todas as transações da blockchain.
        
        Returns:
            List[Transaction]: Lista com todas as transações
        """
        all_transactions = []
        for block in self.chain:
            all_transactions.extend(block.transactions)
        return all_transactions
    
    def to_dict(self) -> dict:
        """
        Converte a blockchain para dicionário.
        
        Returns:
            dict: Representação da blockchain em dicionário
        """
        return {
            'chain': [block.to_dict() for block in self.chain],
            'difficulty': self.difficulty,
            'pending_transactions': [tx.to_dict() for tx in self.pending_transactions],
            'mining_reward': self.mining_reward
        }
