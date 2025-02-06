# functions.py

import copy
import threading
import time
import sys
from IPython.display import Image, display  # Importamos las funciones necesarias para mostrar imágenes

# Variables globales para controlar el juego y el tiempo restante
game_running = True
time_left_display = ""

# URLs de imágenes para cada habitación
room_images = {
    "game room": "images/game_room.jpg",
    "bedroom 1": "images/bedroom1.jpg",
    "bedroom 2": "images/bedroom2.jpg",
    "living room": "images/living_room.jpg",
    "outside": "images/outside.jpg"
}


def start_timer():
    """
    Inicia una cuenta atrás de 300 segundos.
    Si el jugador no escapa en ese tiempo, pierde el juego.
    """
    global game_running, time_left_display
    seconds_left = 300  # 5 minutos

    while seconds_left > 0 and game_running:
        mins, secs = divmod(seconds_left, 60)
        time_left_display = f"Time left: {mins:02}:{secs:02} minutes"
        # Muestra solo el tiempo en la misma línea sin generar múltiples líneas
        sys.stdout.write(f"\r{time_left_display}. ") 
        sys.stdout.flush()
        time.sleep(1)
        seconds_left -= 1

    if game_running:  # Si el juego sigue activo cuando el tiempo se acaba, pierdes
        print("\n\nTime's up! You couldn't escape in time. Game Over!")
        sys.exit()  # Termina la ejecución del programa

def linebreak():
    """Print a line break"""
    print("\n\n")

def explore_room(room, object_relations):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations.get(room["name"], [])]
    print(f"You explore the room. This is {room['name']}. You find {', '.join(items)}")
    
    # Mostrar la imagen de la habitación
    if room["name"] in room_images:
        display(Image(room_images[room["name"]]))

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

def play_room(game_state, room, object_relations):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    global game_running
    game_state["current_room"] = room
    
    if game_state["current_room"] == game_state["target_room"]:
        game_running = False  # Detenemos el temporizador porque el jugador ha ganado
        print("\nCongrats! You escaped the house just in time!")
        sys.exit()  # Termina el programa

    else:
        print(f"\n{time_left_display}")  # Muestra el tiempo restante
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

def start_game(game_state, object_relations):
    """
    Start the game and initiate the timer thread.
    """
    global game_running
    game_running = True

    # Iniciar el temporizador en un hilo separado
    timer_thread = threading.Thread(target=start_timer, daemon=True)
    timer_thread.start()

    print("\nYou wake up on a couch and find yourself in a strange house with no windows which you have never been to before.")
    print("You don't remember why you are here and what had happened before.")
    print("You feel some unknown danger is approaching and you must get out of the house, NOW!\n")
    
    play_room(game_state, game_state["current_room"], object_relations)