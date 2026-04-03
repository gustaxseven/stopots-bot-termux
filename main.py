import os
import sys
from openai import OpenAI

# Tenta pegar a chave da variável de ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    print("\n[ERRO] Chave da OpenAI não encontrada!")
    print("Por favor, configure sua chave com o comando:")
    print("export OPENAI_API_KEY='sua_chave_aqui'")
    sys.exit(1)

# Configuração do cliente OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def get_words(letter, categories):
    """Gera palavras válidas para cada categoria com a letra sorteada."""
    prompt = f"Gere uma palavra para cada uma das seguintes categorias que comece com a letra '{letter}'. Responda apenas com a lista de palavras separadas por vírgula, na mesma ordem das categorias.\nCategorias: {', '.join(categories)}"
    
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente especialista no jogo Stop (Adedonha). Gere apenas palavras válidas e comuns."},
                {"role": "user", "content": prompt}
            ]
        )
        words = response.choices[0].message.content.strip().split(',')
        return [word.strip() for word in words]
    except Exception as e:
        print(f"Erro ao gerar palavras: {e}")
        return []

def main():
    print("--- STOPOTS BOT PARA TERMUX ---")
    print("Este bot gera respostas rápidas para você copiar e colar no jogo.")
    
    while True:
        print("\n--- NOVA RODADA ---")
        letter = input("Digite a letra sorteada (ou 'sair' para encerrar): ").strip().upper()
        
        if letter == 'SAIR':
            break
            
        if not letter.isalpha() or len(letter) != 1:
            print("Letra inválida! Digite apenas uma letra.")
            continue
            
        categories_input = input("Digite as categorias separadas por vírgula: ").strip()
        if not categories_input:
            print("Categorias não podem estar vazias!")
            continue
            
        categories = [c.strip() for c in categories_input.split(',')]
        
        print(f"Gerando respostas para a letra '{letter}'...")
        words = get_words(letter, categories)
        
        if words:
            print("\n--- RESPOSTAS GERADAS ---")
            for i, word in enumerate(words):
                cat = categories[i] if i < len(categories) else "Extra"
                print(f"{cat}: {word}")
            
            print("\nCopie e cole no jogo!")
        else:
            print("Não foi possível gerar as respostas.")

if __name__ == "__main__":
    main()
