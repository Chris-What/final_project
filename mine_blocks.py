#import necessary game components.
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class World(Entity):
    def __init__(self, size_x=50, size_z=50):
        super().__init__()
        self.boxes = []
        self.build_world(size_x, size_z)

    #loop through a grid of size_x and size_z, and place a cube at each position.
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

    #check all boxes, if hovered:left click to add a new cube next to it, or right click to destroy a cube.
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

#create the game engine app, a player that can walk around using a first person camera and controls, a sky background, and the world of blocks.
app = Ursina()
player = FirstPersonController()
sky = Sky()
world = World()

#input functions that listens to the user's actions
def input(key):
    world.handle_input(key)

#start the game loop
app.run()