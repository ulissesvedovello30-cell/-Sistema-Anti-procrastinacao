"""
Esse código se trata de um auxilio para estudos,
bloqueando sites como youtube, instagram, tik tok etc.
"""

import time
import keyboard
import pygetwindow as gw

# A biblioteca pygetwindow é usada para obter as janelas abertas no sistema
# e fechar as janelas dos sites bloqueados

# ========== VARIÁVEIS GLOBAIS ==========
está_em_trégua = False

# ========== SITES BLOQUEADOS ==========
sites_bloqueados = [
    # Redes Sociais
    "YouTube",
    "Instagram",
    "TikTok",
    "Facebook",
    "X",  # Antigo Twitter
    "Reddit",
    "Snapchat",
    "Pinterest",
    "WeChat",
    "Telegram",
    # Streaming & Vídeos
    "Netflix",
    "Amazon Prime",
    "Disney+",
    "Crunchyroll",
    "Vimeo",
    "Dailymotion",
    # Plataformas de Comunicação
    "Twitch",
    "Discord",
    # Música
    "Spotify",
    "SoundCloud",
    "YouTube Music",
    # Jogos Online
    "Steam",
    "Gamdie",
    "slither.io",
    "roblox.com",
    "agar.io",
    "Jogos 360",
    "Click Jogos",
    "Miniclip",
    "Kizi",
    "Y8",
    "Armor Games",
    "Addicting Games",
    "Kongregate",
    "CrazyGames",
    "Poki",
    "GamePix",
    "Agame",
    "Friv",
    "Coolmath Games",
    "Newgrounds",
    "Caberet",
    "NitroType",
    "Cartoon Network",
    "4Jogos",
    "JogosOnline",
    "Uol Jogos",
    "Onlinefutbol",
    "Arcade",
    "JogoLegal",
    "BGames",
    # Comunidades & Fóruns
    "Quora",
    "9gag",
    "Imgur",
    "Wattpad",
    # Compras & Marketplace
    "Amazon",
    "Mercado Livre",
    "AliExpress",
    "eBay",
    "Shopee"
    # Outros
    "Wikipedia",
    "Medium",
    "IMDB",
    "Patreon",
]


# ========== FUNÇÕES ==========
def iniciar_trégua():
    """
    Ativa/desativa o modo trégua que pausa o bloqueio de sites.
    O modo trégua é para ser usado apenas caso seja necessário instalar algo durante o estudo.
    """
    global está_em_trégua
    está_em_trégua = not está_em_trégua
    print(f"\n[SISTEMA] Modo Trégua: {está_em_trégua}")


def iniciar_foco(minutos):
    """
    Inicia o temporizador de foco por um número determinado de minutos.
    
    Durante o foco, o sistema bloqueia os sites especificados e exibe um contador regressivo.
    """
    global está_em_trégua
    segundos_restantes = minutos * 60
    
    while segundos_restantes > 0:
        if está_em_trégua:
            print("\n[SISTEMA] Modo trégua ativado, o timer foi pausado.", 
                  end='\r', flush=True)
            time.sleep(1)
            continue
        
        # Calcula minutos e segundos restantes
        minutos_display, segundos_display = divmod(segundos_restantes, 60)
        
        print(f'Você consegue alcançar seu objetivo! Tempo restante: {minutos_display:02d}:{segundos_display:02d}', 
              end='\r', flush=True)
        
        time.sleep(1)
        bloquear_sites()  # chama a função para bloquear sites proibidos
        segundos_restantes -= 1

def bloquear_sites():
    if está_em_trégua:
        return # Se estiver em trégua, não bloqueia os sites
    
    janelas = gw.getAllWindows() # Obtém todas as janelas abertas no sistema

    for janela in janelas:
        for site in sites_bloqueados:
            if site.lower() in janela.title.lower():
                print(f"\n[SISTEMA] Bloqueando {site}...")
                try:
                    janela.activate() 
                    # fecha apenas a aba ativa
                    keyboard.press_and_release('ctrl+w')
                except Exception as e:
                    # Como fallback, fecha a janela inteira
                    print(f"> Erro ao fechar aba, fechando janela: {e}")
                    janela.close()
                break


# ========== CONFIGURAÇÃO DE ATALHOS ==========
keyboard.add_hotkey('ctrl+shift+p', iniciar_trégua)

# ========== EXECUÇÃO PRINCIPAL ==========
if __name__ == "__main__":
    print("=== SISTEMA ANTI-PROCRSTINAÇÃO ===")
    print("Atalho para trégua: Ctrl + Shift + P")
    print("Olá, seja bem-vindo ao sistema anti-procrastinação! " \
"Desenvolvido pelo aluno da FATEC Rio Claro, Ulisses Vedovello Macedo. " \
"O sistema tem como objetivo ajudar a manter o foco durante os estudos, " \
"bloqueando sites que possam causar distração. " \
"Para ativar o sistema, digite o tempo de foco em minutos e o sistema irá bloquear " \
"os sites especificados durante esse período. Lembrando que esse projeto " \
"apenas oferece ajuda ao estudante, vai da consciência do próprio usuário querer procrastinar ou não. " \
"Se precisar de uma pausa, use o atalho Ctrl + Shift + P para ativar o modo trégua.")
    print("\nMensagem acima é o objetivo do sistema e a orientação de uso.")
    print()
    try:
        minutos_foco = int(input("Digite o tempo de foco em minutos: "))
        if minutos_foco <= 0:
            print("Erro: O tempo de foco deve ser um numero positivo.")
        else:
            iniciar_foco(minutos_foco)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um numero inteiro.")