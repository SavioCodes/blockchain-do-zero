#!/usr/bin/env python3
"""
Script principal para executar a API da blockchain.
"""
from src.api import app

if __name__ == '__main__':
    print("🚀 Iniciando Blockchain do Zero...")
    print("📚 Desenvolvido por Sávio - https://github.com/SavioCodes")
    print("🌐 API rodando em: http://localhost:5000")
    print("📖 Documentação disponível no README.md")
    print("-" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
