from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = SkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # columns
        for i in range(50):
            add(Cube(app, pos=(15, i * s, -9 + i), tex_id=1))
            add(Cube(app, pos=(15, i * s, 5 - i), tex_id=1))

        # cat
        add(Cat(app, pos=(0, -2, -10), scale=(0.7, 0.7, 0.7)))

        # moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

    def update(self):
        self.moving_cube.rot.xyz = self.app.time

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()