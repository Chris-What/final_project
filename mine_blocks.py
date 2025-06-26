from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class World(Entity):
    def __init__(self, size_x=50, size_z=50):
        super().__init__()
        self.boxes = []
        self.build_world(size_x, size_z)

    def build_world(self, size_x, size_z):
        for block in range(size_x):
            for cube in range(size_z):
                box = Button(
                    color=color.white,
                    model="cube",
                    position=(cube, 0, block),
                    texture="grass.png",
                    parent=self,
                    origin_y=0.5
                )
                self.boxes.append(box)