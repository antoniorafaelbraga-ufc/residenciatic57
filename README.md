# Kit de Início P0 - Estrutura de Arquivos e Código-Fonte

Este Kit de Início P0 é o alicerce técnico do programa TrendsIA (Residência em TIC 57). No contexto da Aprendizagem Baseada em Projetos (PBL), o desenvolvimento de um fluxo inicial com LLM (*Large Language Model*) não é apenas um exercício de codificação, mas a fundação estratégica para a construção de agentes de IA complexos.

Este kit funciona como um desbloqueador de execução: ele remove o atrito inicial da configuração de ambiente e autenticação, permitindo que o desenvolvedor foque imediatamente na lógica de processamento e no comportamento do modelo.

A importância deste kit reside na sua capacidade de transformar uma tarefa técnica intimidadora em um processo reprodutível. Ao estabelecer padrões de organização desde o "Dia 0", garantimos que o projeto seja escalável.

Este projeto consolida todo o código-fonte, configurações e documentação do **Kit de Início (Starter Kit) para o Projeto P0 (Primeiro fluxo com LLM)** do TrendsIA.

Os arquivos estão organizados para garantir a reprodutibilidade, segurança e isolamento do ambiente exigidos pelas diretrizes pedagógicas da **Softex**.

---

## Estrutura de Pastas do Projeto
O projeto deve ser organizado localmente na seguinte estrutura de arquivos:
```text
kit-inicio-p0/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── client.py
│   └── app.py
└── tests/
    ├── __init__.py
    └── test_client.py
```

---

## Documentação do Projeto (`README.md`)

Este é o documento principal que orienta qualquer pessoa externa a instalar e configurar o projeto de forma totalmente reproduzível (C04).

```markdown
# TrendsIA - Projeto P0: Primeiro fluxo com LLM

Este repositório contém o Kit de Início do projeto P0, desenvolvido para realizar a primeira integração com o LLM institucional seguindo as melhores práticas técnicas de segurança, reprodutibilidade e tratamento de falhas.

---

## Como Executar em sua Máquina Local (Passo a Passo)

### Passo 1: Clonar ou Baixar o Repositório
Abra seu terminal e navegue até a pasta de sua escolha. Clone ou descompacte os arquivos:
```bash
git clone <url-do-seu-repositorio>
cd kit-inicio-p0
```

### Passo 2: Criar o Ambiente Virtual Isolado (`venv`)
Este passo é obrigatório para evitar conflitos entre bibliotecas da sua máquina e do projeto (C04).

**No Windows (Prompt de Comando ou PowerShell):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**No macOS ou Linux (Terminal):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

*(Você saberá que o ambiente está ativo quando o nome `(.venv)` aparecer no início da linha de comandos de seu terminal).*

---

### Passo 3: Instalar as Dependências do Projeto
Com o ambiente virtual ativado, instale as dependências declaradas:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Passo 4: Configurar as Credenciais e Variáveis de Ambiente
Sua chave de acesso à API do LLM **nunca deve ser inserida diretamente em arquivos de código público**.

1. Crie uma cópia do arquivo `.env.example` e mude o nome da cópia para `.env`:
   ```bash
   cp .env.example .env
   ```
2. Abra o arquivo `.env` gerado em seu VS Code ou editor de texto.
3. Substitua as credenciais fictícias pelas suas chaves de acesso institucionais oficiais:
   ```ini
   LLM_API_BASE_URL=https://api.institucional.ai/v1/chat/completions
   LLM_API_KEY=sua_chave_real_aqui_sem_vazar
   LLM_MODEL_NAME=modelo-institucional-v1
   # Parâmetros adicionais opcionais
   LLM_TEMPERATURE=0.7
   LLM_MAX_TOKENS=1000
   ```

---

### Passo 5: Executar a Aplicação Interativa
Com o ambiente configurado, inicialize a interface de console digitando:
```bash
python -m src.app
```
Siga as instruções impressas na tela. Para sair da CLI amigável, digite **`sair`** ou use **`Ctrl+C`**.

---

### Passo 6: Rodar os Testes Unitários Locais
Você pode testar a robustez do tratamento de falhas e validações sem consumir nenhum crédito de API. Para rodar a bateria de testes automatizados, execute:
```bash
pytest -v
```

---
