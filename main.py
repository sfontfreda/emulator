import pygame
import config
from ui.screens.home_screen import HomeScreen
from core import game_scanner

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    pygame.display.set_caption("pokemachine")
    clock = pygame.time.Clock()
    roms = game_scanner.get_roms()
    home = HomeScreen(roms)

    while True:
        events = pygame.event.get()
        home.handle_events(events)
        screen.fill(config.BLACK)
        home.draw(screen)
        pygame.display.flip()
        clock.tick(config.FPS)

if __name__ == "__main__":
    main()