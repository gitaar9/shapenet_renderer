import argparse
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(__file__))
from mathutils import Matrix, Vector

import util
import blender_interface


cam_locations = util.get_archimedean_spiral(1, 250)

obj_location = np.zeros((1,3))

cv_poses = util.look_at(cam_locations, obj_location)
blender_poses = [util.cv_cam2world_to_bcam2world(m) for m in cv_poses]

print(blender_poses[0])
# shapenet_rotation_mat = np.array([[1.0000000e+00,  0.0000000e+00,  0.0000000e+00],
#                                   [0.0000000e+00, -1.0000000e+00, -1.2246468e-16],
#                                   [0.0000000e+00,  1.2246468e-16, -1.0000000e+00]])
# rot_mat = np.eye(3)
# hom_coords = np.array([[0., 0., 0., 1.]]).reshape(1, 4)
# obj_pose = np.concatenate((rot_mat, obj_location.reshape(3,1)), axis=-1)
# obj_pose = np.concatenate((obj_pose, hom_coords), axis=0)
#
# renderer.import_mesh(opt.mesh_fpath, scale=1., object_world_matrix=obj_pose)
# renderer.render(instance_dir, blender_poses, write_cam_params=True)



# blender --background --python shapenet_spherical_renderer.py -- --output_dir . --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train
# blender --background --python shapenet_spherical_renderer.py -- --output_dir shiprenders --mesh_fpath /home/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/12a01b67cb987d385859fb379730f7f7/models/model_normalized.obj --num_observations 50 --sphere_radius 1 --mode=train

# find ~/Downloads/02691156/ -name *.ply -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir /tmp --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train
# find /shome/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./ship_renders --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train



# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./ship_renders --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train