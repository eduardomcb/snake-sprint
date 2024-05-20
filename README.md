Para documentação em português, consulte o [README em Português](docs/README.pt.md).

# SnakeSprint

A simple Snake game developed with Pygame.

## Project Structure

```
snake-sprint/
├── assets/
│   ├── sounds/
│   │   ├── sfx-impact.mp3
│   │   └── sfx-fail.wav
│   └── images/
│       └── me.jpg
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── ui_menus.py
│   ├── ui_buttons.py
│   ├── utils.py
│   ├── particle.py
│   └── config.py
├── setup.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/eduardomcb/snake-sprint.git
    cd snake-sprint
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Packaging the Game

To create an executable of the game, use the `setup.py` script:

    ```bash
    python setup.py
    ```

The executable will be created in the `dist` folder.

## How to Play

- Use the arrow keys to move the snake.
- Press the spacebar to pause the game.
- The goal is to collect as much food as possible without colliding with yourself.

## Contact

If you have any questions or suggestions, feel free to open an issue or get in touch.

---

Made with ❤️ by [Eduardo Mateus](https://github.com/eduardomcb)