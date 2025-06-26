from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class World(Entity):
    def __init__(self, size_x=50, size_z=50):
        super().__init__()
        self.boxes = []
        self.build_world(size_x, size_z)