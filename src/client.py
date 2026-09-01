import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

def enviar_prompt_llm(prompt: str) -> str:
    """
    Consome a API REST do LLM institucional de forma robusta,
    tratando falhas de conexão, timeouts e erros de credenciais.
    
    Competências exercitadas: C01 (Python) e C03 (APIs REST e tratamento de erros).
    """
    if not prompt or not prompt.strip():
        raise ValueError("O prompt enviado ao modelo não pode estar vazio.")

    # Recupera as configurações das variáveis de ambiente
    api_url = os.getenv("LLM_API_BASE_URL")
    api_key = os.getenv("LLM_API_KEY")
    model_name = os.getenv("LLM_MODEL_NAME", "modelo-padrao")
    
    # Parâmetros de geração opcionais com fallback para erros de conversão
    try:
        temperature = float(os.getenv("LLM_TEMPERATURE", "0.7"))
    except (ValueError, TypeError):
        temperature = 0.7
        
    try:
        max_tokens = int(os.getenv("LLM_MAX_TOKENS", "1000"))
    except (ValueError, TypeError):
        max_tokens = 1000

    if not api_url or not api_key:
        raise ValueError(
            "Configuração incompleta: LLM_API_BASE_URL ou LLM_API_KEY não foram definidos no arquivo .env."
        )

    # Configuração dos cabeçalhos HTTP para autenticação e tipo de conteúdo
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Estruturação do Payload JSON seguindo o padrão das APIs de chat
    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    try:
        # Envia a requisição POST com um timeout de 30 segundos (evita travamentos)
        response = requests.post(api_url, json=payload, headers=headers, timeout=30.0)
        
        # Tratamento de códigos de status HTTP específicos de erro de autenticação e rate limit
        if response.status_code == 401:
            return "Erro de Autenticação (401): A chave de API fornecida é inválida ou expirou."
        elif response.status_code == 429:
            return "Erro de Limite de Requisições (429): Você atingiu o limite de taxa de chamadas do LLM."
        
        # Dispara exceção para outros códigos de status 4xx/5xx
        response.raise_for_status()
        
        # Extrai o texto gerado de forma segura do JSON de retorno
        data = response.json()
        return data["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "Erro de Conexão: A API do LLM demorou muito para responder (Timeout de 30s excedido)."
    except requests.exceptions.ConnectionError:
        return "Erro de Rede: Não foi possível estabelecer conexão física com o servidor do LLM. Verifique sua internet."
    except requests.exceptions.RequestException as e:
        return f"Erro Inesperado na Chamada da API: {str(e)}"
