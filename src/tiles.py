import pygame


class Tile:
    def __init__(self, name: str, image: pygame.Surface):
        self.name = name
        self.image = image

class TileMap:
    def __init__(self):
        self.tiles: dict[tuple[int, int], Tile] = {}

    def add_tile(self, x: int, y: int, tile: Tile):
        self.tiles[(x, y)] = tile

    def get_tile(self, x: int, y: int) -> Tile | None:
        return self.tiles.get((x, y))

    def remove_tile(self, x: int, y: int):
        self.tiles.pop((x, y), None)
    
GRASS = Tile("grass", pygame.Surface((32, 32)))
GRASS.image.fill((0, 255, 0))  # Fill grass tile with green color
STONE = Tile("stone", pygame.Surface((32, 32)))
STONE.image.fill((128, 128, 128))  # Fill stone tile with gray color
SAND = Tile("sand", pygame.Surface((32, 32)))
SAND.image.fill((194, 178, 128))  # Fill sand tile with sandy color