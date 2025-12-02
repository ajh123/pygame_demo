from typing import List, Sequence, Type, TYPE_CHECKING
if TYPE_CHECKING:
    from .entity import Entity
from .tiles import TileMap, Tile


class World:
    def __init__(self):
        self.tile_map = TileMap()
        self.entities: List[Entity] = []

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def get_tile_map(self) -> TileMap:
        return self.tile_map

    def get_entities(self) -> List[Entity]:
        return self.entities

    def get_tile_at(self, x: int, y: int) -> Tile | None:
        return self.tile_map.get_tile(x, y)

    def has_collision(self, source: Entity, excluded: Sequence[Type[Entity]] | None = None) -> Entity | None:
        """
        Check if the source entity collides with any other entity in the world,
        excluding entities of the specified types.

        Uses axis-aligned bounding box (AABB) collision detection.
        """
        for entity in self.get_entities():
            if entity is source:
                continue
            if excluded and isinstance(entity, tuple(excluded)):
                continue

            if (source.x < entity.x + entity.world_units_width and
                source.x + source.world_units_width > entity.x and
                source.y < entity.y + entity.world_units_height and
                source.y + source.world_units_height > entity.y):
                return entity
        return None