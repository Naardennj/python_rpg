from random import randint

npcs_list = [] 

def create_monster():
    level = randint(0, 50)
    
    new_npc = {
        "Name" : f"Monster #{level}",
        "Level": level,
        "Damage": 5 * level,
        "Health": 100 * level,
    }

    return new_npc

def create_monsters (n_npcs):
    for x in range(n_npcs):
        new_npc =  create_monster()
        npcs_list.append(new_npc)

def show_npcs():
    for npc in npcs_list:
        print(f"Name: {npc['Name']} // Level: {npc['Level']} // Damage: {npc['Damage']} // Health: {npc['Health']}")

create_monsters(5)
show_npcs()
