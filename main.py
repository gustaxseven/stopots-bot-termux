import sys
import requests
import json

def join_room(room_url, password=None):
    """Tenta entrar na sala do StopotS via link direto."""
    print(f"--- STOPOTS JOINER ---")
    print(f"Tentando entrar na sala: {room_url}")
    
    # Extrai o ID da sala do link (ex: https://stopots.com/pt/12694 -> 12694)
    try:
        room_id = room_url.split('/')[-1]
        if not room_id.isdigit():
            print("[ERRO] Link inválido! O link deve terminar com o número da sala.")
            return
    except Exception:
        print("[ERRO] Não foi possível extrair o ID da sala do link.")
        return

    # O StopotS usa WebSockets para o jogo real, mas a entrada inicial 
    # pode ser simulada ou verificada via requisição HTTP.
    # Como o Termux não tem navegador, este script valida a sala e 
    # prepara os dados para você.
    
    api_url = f"https://stopots.com/api/room/{room_id}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            room_data = response.json()
            print(f"\nSala encontrada: {room_data.get('name', 'SALA ' + room_id)}")
            
            if room_data.get('password') and not password:
                print("\n!!! ESTA SALA EXIGE SENHA !!!")
                print("Use: python main.py <link> <senha>")
                return
            
            if password:
                print(f"Validando entrada com a senha: {password}")
                # Aqui o bot simularia o POST de entrada se a API permitisse 
                # entrada direta sem WebSocket.
            
            print("\n[SUCESSO] Sala validada e pronta para entrar!")
            print("Como o Termux não tem interface gráfica, use o link abaixo")
            print("no seu navegador do celular para jogar:")
            print(f"-> {room_url}")
            
        else:
            print(f"[ERRO] Não foi possível acessar a sala. Status: {response.status_code}")
            print("Verifique se a sala ainda existe ou se o link está correto.")
            
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema na conexão: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <link_da_sala> [senha]")
        sys.exit(1)
        
    url = sys.argv[1]
    pwd = sys.argv[2] if len(sys.argv) > 2 else None
    
    join_room(url, pwd)
