from duckduckgo_search import DDGS

def main():
    # Inicializa o DDGS
    ddgs = DDGS()

    # Solicita a entrada do usuário
    user_query = input("Digite sua consulta: ")

    # 1. Resposta de Chat IA
    try:
        chat_response = ddgs.chat(user_query)
        print("\n--- Resposta do Chat IA ---")
        print(chat_response if chat_response else "Sem resposta do Chat IA.")
    except Exception as e:
        print(f"Erro no Chat IA: {e}")
    print("\n")

    # 2. Pesquisa de Texto
    try:
        text_results = ddgs.text(user_query, max_results=5)
        print("--- Resultados de Pesquisa de Texto ---")
        if text_results:
            for result in text_results:
                print(f"Título: {result['title']}")
                print(f"Link: {result['href']}")
                print(f"Trecho: {result['body']}")
                print("-" * 50)
        else:
            print("Nenhum resultado encontrado.")
    except Exception as e:
        print(f"Erro na Pesquisa de Texto: {e}")
    print("\n")

if __name__ == "__main__":
    main()
