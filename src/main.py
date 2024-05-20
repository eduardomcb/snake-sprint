import random
import pygame

from src.config import WIDTH, HEIGHT, CELL_SIZE, WHITE, BLACK, FPS, GAME_TITLE
from src.particle import Particle
from src.ui_menus import main_menu, game_over_menu
from src.utils import random_color, draw_text, resource_path

# Inicialização do jogo
pygame.init()

try:
    sfx_impact = pygame.mixer.Sound(resource_path("assets/sounds/sfx-impact.mp3"))
    sfx_fail = pygame.mixer.Sound(resource_path("assets/sounds/sfx-fail.wav"))
except pygame.error as e:
    print(f"Erro ao carregar sons: {e}")
    pygame.quit()

snake_pos = [(WIDTH // 2, HEIGHT // 2)]
snake_body = []
snake_direction = (-1, 0)  # Por padrão, começa indo para a esquerda
food_pos = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
food_color = random_color()
particles = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_TITLE)

clock = pygame.time.Clock()

paused = False


def collision(c1, c2):
    return c1 == c2


def check_self_collision():
    return snake_pos[0] in snake_body[1:]


def on_grid_random():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return x, y


def draw_snake():
    for pos in snake_body:
        pygame.draw.rect(screen, food_color, (pos[0], pos[1], CELL_SIZE, CELL_SIZE))


def draw_food():
    pygame.draw.rect(screen, food_color, (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))


def pause_game():
    main_menu(screen, WIDTH, paused=True)


def reset_game():
    global snake_pos, snake_body, snake_direction, food_pos, food_color, particles
    snake_pos = [(WIDTH // 2, HEIGHT // 2)]
    snake_body = [snake_pos[0]]
    snake_direction = (-1, 0)
    food_pos = on_grid_random()
    food_color = random_color()
    particles = []


# Função principal do jogo
def main_game():
    global snake_pos, snake_body, snake_direction, food_pos, food_color, paused

    running = True

    while running:
        screen.fill(BLACK)

        if paused:
            pause_game()
            paused = False

        # Verifica colisão da cobra consigo mesma
        if check_self_collision():
            sfx_fail.play()
            action = game_over_menu(screen, WIDTH)
            if action == "restart":
                reset_game()
            else:
                running = False

        # Verifica se a cobrinha comeu
        if collision(snake_pos[0], food_pos):
            for _ in range(50):  # Número de partículas
                particles.append(Particle(food_pos, food_color))

            sfx_impact.play()
            food_color = random_color()
            food_pos = on_grid_random()
            snake_body.append(snake_pos[-1])

        for particle in particles[:]:
            particle.update()
            if particle.lifetime <= 0:
                particles.remove(particle)
            else:
                particle.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)
                elif event.key == pygame.K_SPACE:
                    paused = True

        snake_pos[0] = (snake_pos[0][0] + snake_direction[0] * CELL_SIZE,
                        snake_pos[0][1] + snake_direction[1] * CELL_SIZE)

        # Verificação para não sair da tela
        snake_pos[0] = (snake_pos[0][0] % WIDTH, snake_pos[0][1] % HEIGHT)

        # Atualiza todas as partes do corpo da cobra para seguir a cabeça
        snake_body = [snake_pos[0]] + snake_body[:-1]

        draw_snake()
        draw_food()

        draw_text("Press space to pause", pygame.font.Font(None, 21), WHITE, screen, WIDTH // 2, HEIGHT - 10)
        draw_text(f"Foods: {len(snake_body) - 1}", pygame.font.Font(None, 32), WHITE, screen, WIDTH - 60, 25)

        pygame.display.flip()
        clock.tick(FPS)


# Executar o menu principal
main_menu(screen, WIDTH)
# Iniciar o jogo
main_game()

pygame.quit()
