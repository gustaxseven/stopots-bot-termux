import sys
import requests
import re

def join_room(room_url, password=None):
    """Tenta validar a sala do StopotS via link direto."""
    print(f"--- STOPOTS JOINER ---")
    
    # Limpa o link de espaços e caracteres extras
    room_url = room_url.strip()
    print(f"Analisando link: {room_url}")
    
    # Extrai o ID da sala usando Regex para ser mais flexível
    # Aceita links como: stopots.com/pt/28217, stopots.com/28217, ou apenas 28217
    match = re.search(r'(\d+)$', room_url)
    if not match:
        print("[ERRO] Não foi possível encontrar o número da sala no link.")
        print("Certifique-se de que o link termina com o número da sala (ex: /28217).")
        return
    
    room_id = match.group(1)
    print(f"ID da Sala Detectado: {room_id}")

    # O StopotS usa uma API interna para buscar detalhes da sala.
    # Vamos tentar o endpoint que o site usa para carregar as informações.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://stopots.com/pt/'
    }
    
    # Tentativa de validar a sala via API pública
    api_url = f"https://stopots.com/api/room/{room_id}"
    
    try:
        print("Validando sala nos servidores do StopotS...")
        response = requests.get(api_url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            room_data = response.json()
            print(f"\n[SUCESSO] Sala encontrada!")
            print(f"Nome: {room_data.get('name', 'SALA ' + room_id)}")
            print(f"Jogadores: {room_data.get('players', '?')}/{room_data.get('maxPlayers', '?')}")
            
            if room_data.get('password'):
                if not password:
                    print("\n!!! ESTA SALA EXIGE SENHA !!!")
                    print(f"Use: python main.py {room_url} <senha>")
                    return
                else:
                    print(f"Senha '{password}' configurada para entrada.")
            
            print("\n--- COMO ENTRAR ---")
            print("1. Abra o link no seu navegador: " + room_url)
            print("2. O bot confirmou que a sala está ATIVA e disponível.")
            
        elif response.status_code == 404:
            print(f"\n[ERRO] A sala {room_id} não foi encontrada.")
            print("Isso acontece se a sala foi fechada ou o número está errado.")
            print("Dica: Verifique se você copiou o link completo corretamente.")
        else:
            # Se a API falhar, mas o link parecer correto, damos o benefício da dúvida
            print(f"\n[AVISO] Não foi possível validar via API (Status {response.status_code}).")
            print("Mas o link parece correto. Tente abrir diretamente no navegador:")
            print(f"-> {room_url}")
            
    except Exception as e:
        print(f"\n[ERRO] Falha na conexão: {e}")
        print("Verifique sua internet no Termux.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <link_da_sala> [senha]")
        sys.exit(1)
        
    url = sys.argv[1]
    pwd = sys.argv[2] if len(sys.argv) > 2 else None
    
    join_room(url, pwd)
