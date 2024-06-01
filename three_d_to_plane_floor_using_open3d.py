import open3d as o3d
import numpy as np


pcd = o3d.io.read_point_cloud("Mercedes-Benz CLK 430 Convertible.ply")

o3d.visualization.draw_geometries([pcd])


pcd = pcd.voxel_down_sample(voxel_size=0.05)


plane_model, inliers = pcd.segment_plane(distance_threshold=0.01,
                                         ransac_n=3,
                                         num_iterations=1000)


inlier_cloud = pcd.select_by_index(inliers)


floor_points = np.asarray(inlier_cloud.points)
floor_points[:, 2] = 0


floor_plane_pcd = o3d.geometry.PointCloud()
floor_plane_pcd.points = o3d.utility.Vector3dVector(floor_points)


o3d.visualization.draw_geometries([floor_plane_pcd], window_name="Floor Plane Projection")
