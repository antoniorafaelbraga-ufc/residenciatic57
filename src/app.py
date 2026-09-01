import sys
from src.client import enviar_prompt_llm

def executar_cli():
    """
    Interface de Linha de Comando (CLI) que interage com o usuário no terminal.
    Controla o fluxo do programa, impede entradas vazias e exibe respostas de forma legível.
    
    Competências exercitadas: C01 (Python) e C04 (Interface console / ambiente funcional).
    """
    print("=" * 60)
    print("TrendsIA - Kit de Início P0 (Nivelamento)")
    print("=" * 60)
    print("Digite sua mensagem para o LLM (ou digite 'sair' para encerrar).\n")

    while True:
        try:
            prompt = input("Usuário > ").strip()
            
            # Condição de saída amigável
            if prompt.lower() in ['sair', 'exit', 'quit']:
                print("\nEncerrando aplicação. Até logo!")
                break
                
            # Impedir prompts vazios (economia de recursos e robustez)
            if not prompt:
                print("Sistema > Entrada vazia detectada. Por favor, escreva uma mensagem ou pergunta.\n")
                continue

            print("Sistema > Enviando requisição ao LLM institucional...")
            resposta = enviar_prompt_llm(prompt)
            
            print(f"\nIA > {resposta}\n")
            print("-" * 60)

        except KeyboardInterrupt:
            print("\nAplicação interrompida pelo usuário via teclado. Saindo...")
            sys.exit(0)
        except Exception as e:
            print(f"\nSistema > Ocorreu um erro na execução: {str(e)}\n")

if __name__ == "__main__":
    executar_cli()
