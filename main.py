from random import randint

npcs_list = []

player = {
    "name": "Gabriel",
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "damage": 25,
}

def create_monster(level):
    
    new_npc = {
        "name" : f"Monster #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level,
    }

    return new_npc

def create_monsters (n_npcs):
    for x in range(n_npcs):
        npc = create_monster(x + 1)
        npcs_list.append(npc)

def show_npcs():
    for npc in npcs_list:
        show_npc(npc)
    
def show_npc(npc):
    print(f"Name: {npc['name']} // Level: {npc['level']} // Damage: {npc['damage']} // Health: {npc['hp']} // Exp: {npc['exp']}")

def show_player():
    print(f"Name: {player['name']} // Level: {player['level']} // Damage: {player['damage']} // Health: {player['hp']} / {player['hp_max']} // Exp: {player['exp']} / {player['exp_max']}")

def start_battle(npc):
    while player["hp"] > 0 and npc["hp"] > 0:
        atack_npc(npc)
        atack_player(npc)
        show_info_battle(npc)
    
    if player["hp"] > 0:
        print(f"O {player['name']} venceu e ganhou {npc['exp']} de EXP!")
        player["exp"] += npc["exp"]
        show_player()
    else:
        print(f"O {player['name']} foi derrotado pelo {npc['name']}!")
        show_npc(npc)

def atack_npc(npc):
    npc["hp"] -= player["damage"]

def atack_player(npc):
    player["hp"] -= npc["damage"]

def show_info_battle(npc):
    print(f"Player:{player['hp']} // {player['hp_max']}")
    print(f"NPC: {npc['name']}: {npc['hp']} // {npc['hp_max']}")
    print("-------------------------------------\n")

create_monsters(5)
# show_npcs()

npc_select = npcs_list[0]
start_battle(npc_select)
