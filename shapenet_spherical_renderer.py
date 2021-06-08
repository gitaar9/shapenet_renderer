import argparse
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(__file__))

import util
import blender_interface

p = argparse.ArgumentParser(description='Renders given obj file by rotation a camera around it.')
p.add_argument('--mesh_fpath', type=str, required=True, help='The path the output will be dumped to.')
p.add_argument('--output_dir', type=str, required=True, help='The path the output will be dumped to.')
p.add_argument('--num_observations', type=int, required=True, help='The path the output will be dumped to.')
p.add_argument('--sphere_radius', type=float, required=True, help='The path the output will be dumped to.')
p.add_argument('--mode', type=str, required=True, help='Options: train and test')

argv = sys.argv
argv = sys.argv[sys.argv.index("--") + 1:]

opt = p.parse_args(argv)

instance_name = opt.mesh_fpath.split('/')[-3]
instance_dir = os.path.join(opt.output_dir, instance_name)
if os.path.exists(instance_dir):
    print("{} already exists".format(instance_dir))
    exit()

renderer = blender_interface.BlenderInterface(resolution=128)

if opt.mode == 'train':
    cam_locations = util.sample_sherical_uniform_angles(opt.num_observations, opt.sphere_radius)
elif opt.mode == 'test':
    cam_locations = util.get_archimedean_spiral(opt.sphere_radius, opt.num_observations)

obj_location = np.zeros((1, 3))

cv_poses = util.look_at(cam_locations, obj_location)
blender_poses = [util.cv_cam2world_to_bcam2world(m) for m in cv_poses]

shapenet_rotation_mat = np.array([[1.0000000e+00,  0.0000000e+00,  0.0000000e+00],
                                  [0.0000000e+00, -1.0000000e+00, -1.2246468e-16],
                                  [0.0000000e+00,  1.2246468e-16, -1.0000000e+00]])
rot_mat = np.eye(3)
hom_coords = np.array([[0., 0., 0., 1.]]).reshape(1, 4)
obj_pose = np.concatenate((rot_mat, obj_location.reshape(3, 1)), axis=-1)
obj_pose = np.concatenate((obj_pose, hom_coords), axis=0)

scale = 0.575 * opt.sphere_radius  # because we use a fov of 30
# scale *= .005
# scale = 1
renderer.import_mesh(opt.mesh_fpath, scale=scale, object_world_matrix=obj_pose)
renderer.render(instance_dir, blender_poses, write_cam_params=True)



# blender --background --python shapenet_spherical_renderer.py -- --output_dir . --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train
# blender --background --python shapenet_spherical_renderer.py -- --output_dir shiprenders --mesh_fpath /home/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/12a01b67cb987d385859fb379730f7f7/models/model_normalized.obj --num_observations 50 --sphere_radius 1 --mode=train

# find ~/Downloads/02691156/ -name *.ply -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir /tmp --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train
# find /shome/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./ship_renders --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train



# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./ship_renders --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train
# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./ship_renders_black --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train

# for cars 15-04-2021:
# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/02958343/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./car_renders_train_upper_hemisphere --mesh_fpath {} --num_observations 50 --sphere_radius 1 --mode=train

# for cars 16-04-2021:
# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/02958343/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./car_renders_train_upper_hemisphere_30_fov --mesh_fpath {} --num_observations 50 --sphere_radius 10 --mode=train

# for ships 16-04-2021:
# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./ship_renders_train_upper_hemisphere --mesh_fpath {} --num_observations 50 --sphere_radius 10 --mode=train

# for cars 26-04-2021:
# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/02958343/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./car_renders_train_varying_radius_7_13 --mesh_fpath {} --num_observations 50 --sphere_radius 10 --mode=train

# For inference
# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/04530566/1fb07d5bf3421a46e2b83b21c9537e1b/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./inference_poses --mesh_fpath {} --num_observations 4 --sphere_radius 10 --mode=train
# find /home/gitaar9/AI/TNO/pixel-nerf/datasets/02958343/1b1a7af332f8f154487edd538b3d83f6/ -name *.obj -print0 | xargs -0 -n1 -P1 -I {} blender --background --python shapenet_spherical_renderer.py -- --output_dir ./inference_poses/cars --mesh_fpath {} --num_observations 4 --sphere_radius 10 --mode=train