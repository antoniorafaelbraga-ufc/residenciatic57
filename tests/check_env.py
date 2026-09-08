import sys
import os

def check_environment():
    print("=" * 60)
    print("DIAGNÓSTICO DE AMBIENTE PYTHON (TRENDSIA)")
    print("=" * 60)
    
    # 1. Verifica se o interpretador atual é de um ambiente virtual
    in_venv = sys.prefix != sys.base_prefix or 'VIRTUAL_ENV' in os.environ
    venv_path = os.environ.get('VIRTUAL_ENV', 'Nenhum ambiente ativado no terminal')
    
    print(f"Interpretador Ativo:  {sys.executable}")
    print(f"Versão do Python:     {sys.version.split()[0]}")
    print(f"Ambiente Virtual Ativo no Terminal?: {'Sim (Isolado)' if in_venv else 'Não (Global/Inseguro)'}")
    print(f"Pasta do venv detectada:             {venv_path}")
    
    # 2. Testa importação crítica do P0
    print("-" * 60)
    try:
        import requests
        import dotenv
        print("✅ Sucesso: Todas as dependências essenciais do P0 foram importadas corretamente!")
    except ImportError as e:
        print(f"❌ Erro de Importação Detectado: {e}")
        print("\n👉 CAUSA PROVÁVEL: Suas dependências foram instaladas no escopo global ou em outro interpretador.")
        print("👉 SOLUÇÃO: Ative o venv de acordo com seu SO e execute: pip install -r requirements.txt")
    print("=" * 60)

if __name__ == "__main__":
    check_environment()
