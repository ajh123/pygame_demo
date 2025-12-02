import pygame
from typing import Tuple
from player import Player


class HUD:
    """HUD showing health, points, and lives in the top-left corner with a required background."""
    def __init__(
        self,
        font: pygame.font.Font,
        player: Player,
        padding: int = 8,
        bg_color: Tuple[int, int, int] = (0, 0, 0),
        bar_color: Tuple[int, int, int] = (200, 50, 50),
        bar_bg_color: Tuple[int, int, int] = (80, 0, 0),
        text_color: Tuple[int, int, int] = (255, 255, 255)
    ):
        self.player = player
        self.font = font

        self.padding = padding
        self.bg_color = bg_color
        self.bar_color = bar_color
        self.bar_bg_color = bar_bg_color
        self.text_color = text_color

        self.health_bar_width = 200
        self.health_bar_height = 20

    def draw(self, surface: pygame.Surface):
        x = self.padding
        y = self.padding

        points_surf = self.font.render(f"Points: {self.player.points}", True, self.text_color)
        lives_surf = self.font.render(f"Lives: {self.player.lives}", True, self.text_color)
        health_label = self.font.render("Health", True, self.text_color)

        content_width = max(
            self.health_bar_width,
            health_label.get_width(),
            points_surf.get_width(),
            lives_surf.get_width()
        )

        content_height = (
            self.health_bar_height +
            self.padding +
            points_surf.get_height() +
            self.padding +
            lives_surf.get_height()
        )

        bg_rect = pygame.Rect(
            x - self.padding,
            y - self.padding,
            content_width + self.padding * 2,
            content_height + self.padding * 2
        )

        pygame.draw.rect(surface, self.bg_color, bg_rect)

        # Health bar
        fill_ratio = self.player.health / self.player.max_health
        bar_bg_rect = pygame.Rect(x, y, self.health_bar_width, self.health_bar_height)
        bar_rect = pygame.Rect(x, y, int(self.health_bar_width * fill_ratio), self.health_bar_height)

        pygame.draw.rect(surface, self.bar_bg_color, bar_bg_rect)
        pygame.draw.rect(surface, self.bar_color, bar_rect)

        # Label positioned on top of the bar (centered)
        label_x = x + (self.health_bar_width - health_label.get_width()) // 2
        label_y = y + (self.health_bar_height - health_label.get_height()) // 2
        surface.blit(health_label, (label_x, label_y))

        y += self.health_bar_height + self.padding

        # Points
        surface.blit(points_surf, (x, y))
        y += points_surf.get_height() + self.padding

        # Lives
        surface.blit(lives_surf, (x, y))
