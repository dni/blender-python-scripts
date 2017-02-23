import bpy, math

steps = 300
c = 1.05
angle = 137.5
mesh = bpy.ops.mesh.primitive_uv_sphere_add

#cleanup previous
bpy.ops.object.select_all()
bpy.ops.object.delete()
for item in bpy.data.meshes:
    bpy.data.meshes.remove(item)

# draw objects
for n in range(steps):
    a = n * angle
    r = c * math.sqrt(n)
    x = r * math.cos(a)
    y = r * math.sin(a)
    z = n * 0.11
    
    mesh(location=(x,y,z), size=2)
