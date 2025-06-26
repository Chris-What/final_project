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

    def handle_input(self, key):
        for box in self.boxes:
            if box.hovered:
                if key == "left mouse down":
                    new = Button(
                        color=color.white,
                        model="cube",
                        position=box.position + mouse.normal,
                        texture="grass.png",
                        parent=self,
                        origin_y=0.5
                    )
                    self.boxes.append(new)
                
                elif key == "right mouse down":
                    self.boxes.remove(box)
                    destroy(box)

class MyApp(Ursina):
    def __init__(self):
        super().__init__()
        self.player = FirstPersonController()
        self.sky = Sky()
        self.world = World()