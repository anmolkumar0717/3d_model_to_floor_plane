import trimesh
import matplotlib.pyplot as plt


mesh = trimesh.load('Mercedes-Benz CLK 430 Convertible.obj')



vertices = mesh.vertices
faces = mesh.faces


projected_vertices = vertices[:, :2]


edges = mesh.edges

plt.figure(figsize=(10, 10))
for edge in edges:
    start, end = projected_vertices[edge]
    plt.plot([start[0], end[0]], [start[1], end[1]], 'k-')

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Floor Plan Projection')
plt.show()
