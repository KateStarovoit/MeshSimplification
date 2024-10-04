import igl
import scipy as sp
import numpy as np
from meshplot import plot, subplot, interact
import os
import polyscope as ps
root_folder = os.getcwd()

v, f = igl.read_triangle_mesh(os.path.join(root_folder, "data", "decimated-knight.off"))
v2, f2 = igl.read_triangle_mesh(os.path.join(root_folder, "data", "knight2.obj"))
v3, f3 = igl.read_triangle_mesh(os.path.join(root_folder, "data", "knight3.obj"))


ps.init()
mesh = ps.register_surface_mesh('original',v,f)
mesh = ps.register_surface_mesh('t02',v3,f3)
mesh = ps.register_surface_mesh('t01',v2,f2)

points = ps.register_point_cloud('pointsv', v)
#ints = ps.register_point_cloud('pointsv1', v1)
ints = ps.register_point_cloud('pointsv2', v2)
ints = ps.register_point_cloud('pointsv3', v3)
ps.show()