For English documentation, please see the [English README](../README.md).

# SnakeSprint

Um jogo simples de Snake desenvolvido com Pygame.

## Estrutura do Projeto

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

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/eduardomcb/snake-sprint.git
    cd snake-sprint
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Empacotando o Jogo

Para criar um executável do jogo, use o script `setup.py`:

    ```bash
    python setup.py
    ```

O executável será criado na pasta `dist`.

## Como Jogar

- Use as setas do teclado para mover a cobra.
- Pressione a barra de espaço para pausar o jogo.
- O objetivo é coletar o máximo de alimentos possível sem colidir com você mesmo.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue ou entrar em contato.

---

Feito com ❤️ por [Eduardo Mateus](https://github.com/eduardomcb)
