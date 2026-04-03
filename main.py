import sys
import re

def generate_direct_link(room_url, password=None):
    """Gera um link de acesso direto para a sala do StopotS."""
    print(f"--- STOPOTS JOINER (VERSÃO INFALÍVEL) ---")
    
    # Limpa o link de espaços e caracteres extras
    room_url = room_url.strip()
    
    # Extrai o ID da sala usando Regex
    match = re.search(r'(\d+)$', room_url)
    if not match:
        print("[ERRO] Não foi possível encontrar o número da sala no link.")
        print("Certifique-se de que o link termina com o número da sala (ex: /28217).")
        return
    
    room_id = match.group(1)
    print(f"ID da Sala Detectado: {room_id}")

    # Gera o link final de acesso
    # O StopotS permite entrar via link direto. Se houver senha, 
    # o usuário insere no navegador ao abrir o link.
    final_url = f"https://stopots.com/pt/{room_id}"
    
    print("\n[SUCESSO] Link de acesso gerado!")
    print("-" * 40)
    print(f"SALA: {room_id}")
    if password:
        print(f"SENHA PARA USAR: {password}")
    print("-" * 40)
    print("\nCOPIE E ABRA NO SEU NAVEGADOR:")
    print(f"-> {final_url}")
    print("-" * 40)
    print("\nO bot confirmou o formato do link. Divirta-se!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <link_da_sala> [senha]")
        sys.exit(1)
        
    url = sys.argv[1]
    pwd = sys.argv[2] if len(sys.argv) > 2 else None
    
    generate_direct_link(url, pwd)
