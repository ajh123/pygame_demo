import pygame
from .world import World


class Entity:
    def __init__(self, world: World, x: float, y: float, width: int, height: int, image_map: dict[str, pygame.Surface]):
        self.world = world
        self.world.add_entity(self)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity_dx = 0.0
        self.velocity_dy = 0.0
        self.image_map = image_map
        self.current_image_key: str | None = None
        self.health = -1 # -1 means infinite health

    def tick(self):
        """Update entity position based on its velocity."""
        self.x += self.velocity_dx
        self.y += self.velocity_dy

    def take_damage(self, amount: float):
        if self.health < 0:
            return  # Infinite health

        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        self.world.get_entities().remove(self)

    def set_velocity(self, dx: float, dy: float):
        self.velocity_dx = dx
        self.velocity_dy = dy

    def get_position(self) -> tuple[float, float]:
        return self.x, self.y
    
    def set_image_state(self, key: str):
        if key in self.image_map:
            self.current_image_key = key

    def get_current_image(self) -> pygame.Surface | None:
        if self.current_image_key:
            return self.image_map[self.current_image_key]
        return None
