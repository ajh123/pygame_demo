import pygame


class Camera:
    def __init__(self, width: int, height: int, speed: float = 5.0):
        self.width = width
        self.height = height
        self.x = 0.0  # world coordinates of camera center
        self.y = 0.0
        self.speed = speed
        self._input_dx = 0.0
        self._input_dy = 0.0

    def handle_input(self):
        """Read input and store movement vector."""
        keys = pygame.key.get_pressed()
        dx = dy = 0.0
        if keys[pygame.K_LEFT]:
            dx -= 1
        if keys[pygame.K_RIGHT]:
            dx += 1
        if keys[pygame.K_UP]:
            dy -= 1
        if keys[pygame.K_DOWN]:
            dy += 1
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            factor = 0.7071  # 1/sqrt(2)
            dx *= factor
            dy *= factor
        self._input_dx = dx * self.speed
        self._input_dy = dy * self.speed

    def tick(self):
        """Update camera position based on input."""
        self.x += self._input_dx
        self.y += self._input_dy

    def world_to_screen(self, world_x: int, world_y: int, tile_size: int) -> tuple[int, int]:
        screen_x = int((world_x * tile_size) - self.x + (self.width // 2))
        screen_y = int((world_y * tile_size) - self.y + (self.height // 2))
        return screen_x, screen_y