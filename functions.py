# functions.py

import copy

def linebreak():
    """Print a line break"""
    print("\n\n")

def start_game(game_state, object_relations):
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state, game_state["current_room"], object_relations)

def play_room(game_state, room, object_relations):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if game_state["current_room"] == game_state["target_room"]:
        print("Congrats! You escaped the room!")
    else:
        print(f"You are now in {room['name']}")
        intended_action = input("What would you like to do? Type 'explore' or 'examine'? ").strip()
        if intended_action == "explore":
            explore_room(room, object_relations)
            play_room(game_state, room, object_relations)
        elif intended_action == "examine":
            examine_item(game_state, input("What would you like to examine? ").strip(), object_relations)
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(game_state, room, object_relations)
        linebreak()

def explore_room(room, object_relations):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations.get(room["name"], [])]
    print(f"You explore the room. This is {room['name']}. You find {', '.join(items)}")

def get_next_room_of_door(door, current_room, object_relations):
    """
    Find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations.get(door["name"], [])
    for room in connected_rooms:
        if room != current_room:
            return room
    return None

def examine_item(game_state, item_name, object_relations):
    """
    Examine an item which can be a door or furniture.
    """
    current_room = game_state["current_room"]
    next_room = None
    output = None
    
    for item in object_relations.get(current_room["name"], []):
        if item["name"] == item_name:
            output = f"You examine {item_name}. "
            if item["type"] == "door":
                have_key = any(key["target"] == item for key in game_state["keys_collected"])
                if have_key:
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room, object_relations)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if item["name"] in object_relations and object_relations[item["name"]]:
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += f"You find {item_found['name']}."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if output is None:
        print("The item you requested is not found in the current room.")
    
    if next_room and input("Do you want to go to the next room? Enter 'yes' or 'no': ").strip().lower() == 'yes':
        play_room(game_state, next_room, object_relations)
    else:
        play_room(game_state, current_room, object_relations)
