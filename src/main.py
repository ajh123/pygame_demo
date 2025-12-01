import pygame
from camera import Camera
from tiles import TileMap, GRASS, STONE, SAND
from renderer import Renderer

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    camera = Camera(screen.get_width(), screen.get_height())
    tile_map = TileMap()
    renderer = Renderer(screen, camera, tile_map)

    # Add some tiles to the map. Start at -25, -25 to center around (0,0)
    for x in range(-25, 25):
        for y in range(-25, 25):
            if (x + y) % 3 == 0:
                tile_map.add_tile(x, y, GRASS)
            elif (x + y) % 3 == 1:
                tile_map.add_tile(x, y, STONE)
            else:
                tile_map.add_tile(x, y, SAND)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                camera.width = event.w
                camera.height = event.h

        camera.handle_input()
        camera.tick()
        renderer.render()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()