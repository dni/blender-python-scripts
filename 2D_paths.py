import bpy, math
from bpy_extras.io_utils import unpack_list
from mathutils import Vector

pos = -2
length = 20
depth = 1
points = []

# graphing in 3D
# def f(x):
#     return math.log(x) * math.sin(20*x) * 5

# def g(x):
#     return 1
#     return math.sin(x)

# while pos < length:
#     v = Vector((pos, f(pos), g(pos), 1))
#     points.append(v)
#     pos += depth

# drawing a vase contour

def f(x):
  p = 0.9882235373
  q = 4.960882158
  r = 4.978373717
  s = 5.015096102
  t = 6.043658926

  pw = math.pow
  return p*pw(x, 5) - q*pw(x, 4) +  r*pw(x, 3) + s*pw(x, 2) - t*x - 1

pos = -1
while pos < 3:
   v = Vector((pos, f(pos), 0, 1))
   points.append(v)
   pos += 0.05



# draw the whole path
curve = bpy.data.curves.new("Bezier", 'CURVE')
spline = curve.splines.new('POLY')
spline.points.add(len(points)-1)
spline.points.foreach_set("co", unpack_list(points))
obj = bpy.data.objects.new("curve", curve)
bpy.context.scene.objects.link(obj)
