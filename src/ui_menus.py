import sys
import webbrowser

import pygame

from src.config import BLACK, WHITE, GAME_TITLE
from src.ui_buttons import Button
from src.utils import draw_text, resource_path


def main_menu(screen, width, paused=False):
    while True:
        screen.fill(BLACK)
        draw_text(GAME_TITLE, pygame.font.Font(None, 64), WHITE, screen, width // 2, 100)

        font = pygame.font.Font(None, 36)

        start_button_text = "Continue" if paused else "Start"

        # Button start
        button_start = Button(start_button_text, font, BLACK, WHITE, screen, width // 2 - 100, 200)
        button_start.draw()

        if button_start.is_clicked():
            return

        # Button credits
        button_credits = Button("Credits", font, BLACK, WHITE, screen, width // 2 - 100, 265)
        button_credits.draw()

        if button_credits.is_clicked():
            credits_menu(screen, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def credits_menu(screen, width):
    while True:
        screen.fill(BLACK)

        profile_picture = pygame.image.load(resource_path("assets/images/me.jpg"))
        # Redimensiona a imagem

        new_width = 150
        new_height = 150
        profile_picture = pygame.transform.scale(profile_picture, (new_width, new_height))

        screen.blit(profile_picture, (width // 2 - profile_picture.get_width() // 2, 150))

        font = pygame.font.Font(None, 36)

        # Button github
        button_github = Button("See my github", font, BLACK, WHITE, screen, width // 2 - 100, 330)
        button_github.draw()

        draw_text("Eduardo Mateus", pygame.font.Font(None, 36), WHITE, screen, width // 2, 430)
        draw_text("Programador :)", pygame.font.Font(None, 24), WHITE, screen, width // 2, 480)

        if button_github.is_clicked():
            webbrowser.open("https://github.com/eduardomcb")

        # Button back
        button_back = Button("Back", font, BLACK, WHITE, screen, 40, 45)
        button_back.draw()
        if button_back.is_clicked():
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def game_over_menu(screen, width):
    while True:
        screen.fill(BLACK)
        draw_text("Game Over", pygame.font.Font(None, 64), WHITE, screen, width // 2, 100)

        font = pygame.font.Font(None, 36)

        # Button restart
        button_restart = Button("Restart", font, BLACK, WHITE, screen, width // 2 - 100, 200)
        button_restart.draw()

        if button_restart.is_clicked():
            return "restart"

        # Button quit
        button_quit = Button("Quit", font, BLACK, WHITE, screen, width // 2 - 100, 265)
        button_quit.draw()

        if button_quit.is_clicked():
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
