# 🏃‍♂️ Real-Time Escape Room Game in Python

Welcome! This project offers a simple "Escape Room" game written in Python, where you need to find keys, open doors, and escape before time runs out.

---

## 1. Introduction 📖

In this game, you wake up in a strange house and must explore various rooms, collect items, and find a way to escape. The main challenge is to find the right keys to open the doors that will lead you out of the house, all before the 5-minute timer runs out.

---

## 2. Installation 🛠️

1. Ensure you have **Python 3.x** installed.
2. (Optional) Install [Jupyter Notebook](https://jupyter.org/) or run the project in a notebook-compatible environment (e.g., Google Colab).
3. Clone or download this repository to your local machine.
4. From your terminal, navigate to the project folder and install the necessary libraries to play:

``` python
pip install -r requirements.txt
```

---

## 3. Game Map 🗺️

In this map, you can visualize the connection between the different rooms of the house:

![Game Map](images/map.jpg)

---

## 4. How to Play 🎮

1. Run the **main.ipynb** notebook from your Python/Jupyter environment.
2. At the start of the game, an introductory text will be displayed, and you will begin in the *Game Room*.
3. Type `explore` to explore the room; you will see a list of objects you can examine.
4. Type `examine` to inspect a specific object. If you find a key, it will be added to your inventory.
5. Use the keys to open locked doors and move to other rooms.
6. The main objective is to reach the `outside` room before the 5-minute timer runs out.

Enjoy the challenge and good luck escaping in time!

---

## 5. Room Descriptions 🏠

The game includes five main scenarios, each with its own reference image:

1. **Game Room**  
   ![Game Room](images/game_room.jpg)  
   Here you start your adventure, with a piano, a sofa, and the first door you need to unlock.

2. **Bedroom 1**  
   ![Bedroom 1](images/bedroom1.jpg)  
   You will find a bed and several connecting doors.

3. **Bedroom 2**  
   ![Bedroom 2](images/bedroom2.jpg)  
   A second room containing another bed and a cabinet where you might find useful items.

4. **Living Room**  
   ![Living Room](images/living_room.jpg)  
   You are close to the end! Find the door to freedom.

5. **Outside**  
   ![Outside](images/outside.jpg)  
   Your final goal is to get here within 5 minutes!

---

## 6. File and Code Structure 📂

- **main.ipynb**  
  The main entry point of the game in Jupyter Notebook (or an equivalent notebook). Here, rooms, keys, and the function that starts the game (`start_game`) are defined. You can run all the cells from this file to start playing.

- **functions.py**  
  Contains the base functions and logic of the game. Some key parts include:

  - `start_game(game_state, object_relations)`: Starts the game and launches the timer in a separate thread.
  - `play_room(game_state, room, object_relations)`: Manages player interaction with each room.
  - `examine_item(game_state, item_name, object_relations)`: Allows inspecting objects and collecting keys.
  - `start_timer()`: Controls the 5-minute countdown. If time runs out, the game ends.

These functions work together to provide a real-time "Escape Room" experience. As you explore, you will see the remaining time on the screen, and if you do not manage to escape before the timer reaches zero, you will lose the game.

---

## 7. Authors ✍️

- @Cristina-Puertas-Camarero: <https://github.com/Cristina-Puertas-Camarero>
- @LuchoRosario: <https://github.com/LuchoRosario>
- @jesuserro: <https://github.com/jesuserro>