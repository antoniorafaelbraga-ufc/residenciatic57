import pytest
from src.client import enviar_prompt_llm

def test_prompt_vazio_dispara_erro():
    """Valida que o cliente do LLM recusa strings vazias localmente, sem ir para a rede."""
    with pytest.raises(ValueError, match="O prompt enviado ao modelo não pode estar vazio"):
        enviar_prompt_llm("")

def test_configuracao_ausente_dispara_erro(monkeypatch):
    """Garante que se as variáveis cruciais de ambiente sumirem, o código avisa antes do requests."""
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    with pytest.raises(ValueError, match="Configuração incompleta"):
        enviar_prompt_llm("Olá, mundo!")

def test_chamada_sucesso_com_mock(monkeypatch, requests_mock):
    """
    Simula uma requisição HTTP de sucesso para a API do LLM usando um dublê de testes (Mock).
    Garante que validamos a montagem do payload e o parsing do JSON sem conexões físicas ou custos de API.
    
    Evidência de validação exigida: 'Teste sem chamada real'.
    """
    mock_url = "https://api.institucional.ai/v1/chat/completions"
    monkeypatch.setenv("LLM_API_BASE_URL", mock_url)
    monkeypatch.setenv("LLM_API_KEY", "chave_secreta_local_testes")
    monkeypatch.setenv("LLM_MODEL_NAME", "modelo-teste")

    mock_json_response = {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Esta é uma resposta mockada com sucesso!"
                }
            }
        ]
    }

    # Configura o mock do requests para interceptar chamadas POST a essa URL específica
    requests_mock.post(mock_url, json=mock_json_response, status_code=200)

    resultado = enviar_prompt_llm("Olá, IA!")
    assert resultado == "Esta é uma resposta mockada com sucesso!"
    assert requests_mock.called
    assert requests_mock.call_count == 1

def test_erro_401_com_mock(monkeypatch, requests_mock):
    """Garante o tratamento gracioso e amigável quando as chaves de API forem inválidas (HTTP 401)."""
    mock_url = "https://api.institucional.ai/v1/chat/completions"
    monkeypatch.setenv("LLM_API_BASE_URL", mock_url)
    monkeypatch.setenv("LLM_API_KEY", "chave_invalida")

    requests_mock.post(mock_url, status_code=401)

    resultado = enviar_prompt_llm("Olá, IA!")
    assert "Erro de Autenticação (401)" in resultado

def test_erro_timeout_com_mock(monkeypatch, requests_mock):
    """Testa se o timeout físico da rede é apanhado e devolve uma mensagem limpa e compreensível."""
    import requests
    mock_url = "https://api.institucional.ai/v1/chat/completions"
    monkeypatch.setenv("LLM_API_BASE_URL", mock_url)
    monkeypatch.setenv("LLM_API_KEY", "chave_correta")

    # Força o mock a disparar uma exceção de timeout física
    requests_mock.post(mock_url, exc=requests.exceptions.Timeout)

    resultado = enviar_prompt_llm("Olá, IA!")
    assert "Erro de Conexão" in resultado
    assert "Timeout" in resultado
