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
        "health": 100 * level,
        "exp": 7 * level,
    }

    return new_npc

def create_monsters (n_npcs):
    for x in range(n_npcs):
        npc = create_monster(x + 1)
        npcs_list.append(npc)

def show_npcs():
    for npc in npcs_list:
        print(f"Name: {npc['name']} // Level: {npc['level']} // Damage: {npc['damage']} // Health: {npc['health']} // Exp: {npc['exp']}")

def atack_npc(npc):
    npc["health"] -= player["damage"]

create_monsters(5)
show_npcs()

npc_select = npcs_list[0]

print("NPC selecionado", npc_select)
atack_npc(npc_select)

print("NPC atacado", npc_select)
