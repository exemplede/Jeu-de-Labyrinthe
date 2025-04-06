from collections import deque 
from colorama import Fore, Back, Style, init
import time
import os

# Initialisation de colorama
init(autoreset=True)

filename = "monlaby_1.txt"
map = []
with open(filename, "r") as f:
    map = [list(line.strip()) for line in f.readlines()]

# Personnages et éléments du jeu
aventurier = {
    "position": [6, 0],
    "etat": 0,
    "symbole": '🧙',
    "couleur": Fore.BLUE
}

joyau = {
    "symbole": '💎',
    "position": [4, 7],
    "couleur": Fore.YELLOW
}

# Styles visuels
WALL_STYLE = Fore.RED + '▓▓'
PATH_STYLE = Fore.WHITE + '░░'
BORDER_STYLE = Fore.CYAN + '║'
TITLE_STYLE = Fore.MAGENTA + Style.BRIGHT


def print_header(temps_mis, moves_count):
    print(TITLE_STYLE + "══════════════════════════════════")
    print(f"        LABYRINTHE MAGIQUE")
    print(f" Temps: {temps_mis:.1f}s • Mouvements: {moves_count}")
    print("══════════════════════════════════" + Style.RESET_ALL)
    print(f"Contrôles: Z (haut), Q (gauche), S (bas), D (droite)")
    print(f"          M (menu), Q (quitter)\n")

def printmap(map, aventurier, joyau):
    os.system("clear")
    temps_mis = time.time() - start_time
    print_header(temps_mis, moves_count)
    
    print(BORDER_STYLE + "╔" + "══" * len(map[0]) + "╗")
    for i in range(len(map)):
        print(BORDER_STYLE + "║", end="")
        for j in range(len(map[i])):
            if [i, j] == aventurier["position"]:
                print(aventurier["couleur"] + aventurier["symbole"], end=" ")
            elif [i, j] == joyau["position"]:
                print(joyau["couleur"] + joyau["symbole"], end=" ")
            elif map[i][j] == '1':
                print(WALL_STYLE, end=" ")
            elif map[i][j] == '0':
                print(PATH_STYLE, end=" ")
        print(BORDER_STYLE + "║")
    print(BORDER_STYLE + "╚" + "══" * len(map[0]) + "╝")

# Contrôles (configuration française ZQSD)
controls = {
    'h': [-1, 0],  # haut
    'g': [0, -1],  # gauche
    'b': [1, 0],   # bas
    'd': [0, 1],   # droite
    '8': [-1, 0],  # haut (num pad)
    '4': [0, -1],  # gauche (num pad)
    '2': [1, 0],   # bas (num pad)
    '6': [0, 1]    # droite (num pad)
}

def move_aventurier(direction):
    global moves_count
    new_pos = [
        aventurier["position"][0] + direction[0],
        aventurier["position"][1] + direction[1]
    ]
    
    if est_autoriser(new_pos, map):
        aventurier["position"] = new_pos
        moves_count += 1
        return True
    else:
        print(Fore.RED + "Mouvement impossible!")
        time.sleep(0.5)
        return False

def est_autoriser(position, map):
    return (
        0 <= position[0] < len(map) and 
        0 <= position[1] < len(map[0]) and 
        map[position[0]][position[1]] != '1'
    )

# Initialisation du jeu
start_time = time.time()
moves_count = 0
historique_positions = [aventurier["position"].copy()]

while True:
    printmap(map, aventurier, joyau)
    
    if aventurier["position"] == joyau["position"]:
        end_time = time.time()
        print(Fore.GREEN + Style.BRIGHT + "\n╔════════════════════════════╗")
        print("║   FÉLICITATIONS !!!     ║")
        print("║   Vous avez trouvé le   ║")
        print("║      trésor 💎         ║")
        print(f"║   Temps: {end_time-start_time:.1f}s    ║")
        print(f"║   Mouvements: {moves_count}     ║")
        print("╚════════════════════════════╝")
        break
    
    command = input("\nVotre mouvement (ZQSD/M/Q) > ").lower()
    
    if command == 'q':
        print(Fore.YELLOW + "\nPartie terminée. À bientôt!")
        break
    elif command == 'm':
        print("\nMenu:")
        print("1. Continuer")
        print("2. Quitter")
        choice = input("Choix: ")
        if choice == '2':
            break
        continue
    elif command in controls:
        move_aventurier(controls[command])
    else:
        print(Fore.RED + "Commande invalide! Utilisez Z,Q,S,D")
        time.sleep(0.5)