import bpy, math
import numpy as np

sphere = bpy.ops.mesh.primitive_uv_sphere_add

class Planet:

    def __init__(self, r, d, v):
        self.r = r
        self.d = d
        self.v = v
        self.a =  math.pi
        self.pos = np.array([0, 0])
        self.moons = []

    def spawnMoons(l, j):
        for i in range(j):
            r = self.r / (j*2)
            d = math.rand(50,150)
            v = math.rand(-0.1,0.1)
            self.moons[i] = Planet(r, d/j, v)
            if j < 3:
                self.moons[i].spawnMoons(3, j+1)


    def orbit():
        self.a = self.a + self.v
        if self.moons:
            for moon in self.moons:
                moon.orbit()


    def show(self):
        sphere(size=self.r, location=(self.pos[0], self.pos[1], 0))


# sun = Planet(None, 100, 0, 1)
# planet.show()
