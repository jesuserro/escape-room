# `Escape Room` Game

¡Bienvenidos! Este proyecto ofrece un sencillo juego de tipo "Escape Room" escrito en Python, en el que tendrás que encontrar llaves, abrir puertas y escapar antes de que se agote el tiempo.

---

## 1. Introducción

En este juego despertarás en una casa extraña y deberás explorar varias habitaciones, recolectar objetos y descubrir la forma de escapar. El desafío principal consiste en encontrar las llaves adecuadas para abrir las puertas que te conducirán fuera de la casa, todo antes de que se agote el temporizador de 5 minutos.

---

## 2. Instalación

1. Asegúrate de tener instalado **Python 3.x**.
2. (Opcional) Instala [Jupyter Notebook](https://jupyter.org/) o ejecuta el proyecto en un entorno compatible con notebooks (por ejemplo, Google Colab).
3. Clona o descarga este repositorio en tu máquina local.
4. Desde tu terminal, ubícate en la carpeta del proyecto e instala las librerías necesarias para jugar:

``` python
pip install -r requirements.txt
```

---

## 3. Mapa del juego

En este mapa podrás visualizar la conexión entre las distintas habitaciones de la casa:

![Mapa del juego](images/map.jpg)

---

## 4. ¿Cómo Jugar?

1. Ejecuta el notebook **main.ipynb** desde tu entorno de Python/Jupyter.
2. Al iniciarse el juego, se mostrará un texto introductorio y comenzarás en la *Game Room*.
3. Escribe `explore` para explorar la habitación, verás un listado de objetos que puedes examinar.
4. Escribe `examine` para inspeccionar un objeto específico. Si encuentras una llave, se guardará en tu inventario.
5. Usa las llaves para abrir puertas bloqueadas y moverte a otras habitaciones.
6. El objetivo principal es llegar a la habitación `outside` antes de que el contador de 5 minutos llegue a cero.

¡Disfruta del desafío y buena suerte escapando a tiempo!

---

## 5. Descripción de las Habitaciones

El juego incluye cinco escenarios principales, cada uno con su propia imagen de referencia:

1. **Sala de Juegos (Game Room)**  
![Game Room](images/game_room.jpg)  
Aquí comienzas tu aventura, con un piano, un sofá y la primera puerta que deberás desbloquear.

2. **Dormitorio 1 (Bedroom 1)**  
![Bedroom 1](images/bedroom1.jpg)  
Encontrarás una cama y varias puertas de conexión.

3. **Dormitorio 2 (Bedroom 2)**  
![Bedroom 2](images/bedroom2.jpg)  
Una segunda habitación que contiene otra cama y un mueble donde podrías encontrar objetos útiles.

4. **Sala de Estar (Living Room)**  
![Living Room](images/living_room.jpg)  
¡Ya estás cerca del final! Encuentra la puerta hacia la libertad.

1. **Exterior (Outside)**  
![Exterior](images/outside.jpg)  
Tu objetivo final es llegar aquí ¡en 5 minutos!.

---

## 6. Estructura de Archivos y Código

- **main.ipynb**  
Es el punto de entrada principal del juego en Jupyter Notebook (o un notebook equivalente). Aquí se definen las habitaciones, las llaves y la función que inicia el juego (`start_game`). Desde este archivo puedes ejecutar todas las celdas para comenzar a jugar.

- **functions.py**  
Contiene las funciones y la lógica base del juego. Algunas de sus partes clave:

  - `start_game(game_state, object_relations)`: Inicia el juego y lanza el temporizador en un hilo independiente.
  - `play_room(game_state, room, object_relations)`: Gestiona la interacción del jugador con cada habitación.
  - `examine_item(game_state, item_name, object_relations)`: Permite inspeccionar objetos y recoger llaves.
  - `start_timer()`: Controla la cuenta regresiva de 5 minutos. Si el tiempo se agota, el juego termina.

Estas funciones trabajan juntas para ofrecer una experiencia de "Escape Room" en tiempo real. Mientras exploras, podrás ver el tiempo restante en pantalla y, si no logras salir antes de que el contador llegue a cero, perderás la partida.

## 7. Authors

- @Cristina-Puertas-Camarero: <https://github.com/Cristina-Puertas-Camarero>
- @LuchoRosario: <https://github.com/LuchoRosario>
- @jesuserro: <https://github.com/jesuserro>
