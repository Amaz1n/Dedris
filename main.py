# Tetris but legally distinct
import pygame
import random
import Block as blockClass

# Main
if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((800, 1000))
    clock = pygame.time.Clock()
    dt = 0

    block = blockClass.Block()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        window.fill("black")

        block.print()
        block.rotate(False)

        pygame.display.flip()
        dt = clock.tick(24) / 1000

    pygame.quit()
