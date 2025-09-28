"""
Testes para a API Flask.
"""
import pytest
import json
from src.api import app


@pytest.fixture
def client():
    """
    Fixture para o cliente de teste do Flask.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestAPI:
    """
    Classe de testes para a API.
    """
    
    def test_get_blockchain(self, client):
        """
        Testa o endpoint GET /blockchain.
        """
        response = client.get('/blockchain')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'chain' in data
        assert 'difficulty' in data
        assert 'pending_transactions' in data
        assert 'mining_reward' in data
    
    def test_get_block_valid_index(self, client):
        """
        Testa o endpoint GET /blocks/<index> com índice válido.
        """
        response = client.get('/blocks/0')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert data['index'] == 0
    
    def test_get_block_invalid_index(self, client):
        """
        Testa o endpoint GET /blocks/<index> com índice inválido.
        """
        response = client.get('/blocks/999')
        assert response.status_code == 404
    
    def test_add_transaction_valid(self, client):
        """
        Testa o endpoint POST /transactions com dados válidos.
        """
        transaction_data = {
            'sender': 'Alice',
            'recipient': 'Bob',
            'amount': 50.0
        }
        
        response = client.post('/transactions',
                             data=json.dumps(transaction_data),
                             content_type='application/json')
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['message'] == 'Transação adicionada com sucesso'
    
    def test_add_transaction_invalid_data(self, client):
        """
        Testa o endpoint POST /transactions com dados inválidos.
        """
        # Dados incompletos
        invalid_data = {
            'sender': 'Alice',
            'amount': 50.0
            # Faltando 'recipient'
        }
        
        response = client.post('/transactions',
                             data=json.dumps(invalid_data),
                             content_type='application/json')
        
        assert response.status_code == 400
    
    def test_get_balance(self, client):
        """
        Testa o endpoint GET /balance/<address>.
        """
        response = client.get('/balance/Alice')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'address' in data
        assert 'balance' in data
        assert data['address'] == 'Alice'
    
    def test_validate_blockchain(self, client):
        """
        Testa o endpoint GET /validate.
        """
        response = client.get('/validate')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'is_valid' in data
        assert 'message' in data
        assert data['is_valid'] == True
    
    def test_get_stats(self, client):
        """
        Testa o endpoint GET /stats.
        """
        response = client.get('/stats')
        assert response.status_code == 200
        
        data = json.loads(response.data)
        assert 'total_blocks' in data
        assert 'total_transactions' in data
        assert 'pending_transactions' in data
        assert 'difficulty' in data
        assert 'mining_reward' in data
