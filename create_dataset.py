import argparse
import os
import subprocess
import numpy as np


def load_bad_models(path):
    bad_models = np.load(path)
    return list(bad_models)


def main(output_dir, mesh_base_path, amount_of_train_images, bad_models_path):
    from car_train_test_val import test as object_ids

    if bad_models_path:
        bad_models = load_bad_models(bad_models_path)
        object_ids = [i for i in object_ids if i not in bad_models]

    cmd = 'blender --background --python shapenet_spherical_renderer.py -- --output_dir {} --mesh_fpath {} ' \
          '--num_observations {} --sphere_radius 10 --mode=train'

    for idx, object_id in enumerate(object_ids):
        print(f"{idx + 1}/{len(object_ids)}: Rendering images for object {object_id}")
        mesh_path = os.path.join(mesh_base_path, object_id, 'models/model_normalized.obj')
        # _ = subprocess.run(cmd.format(output_dir, mesh_path, amount_of_train_images), shell=True)
        _ = subprocess.run(cmd.format(output_dir, mesh_path, amount_of_train_images), shell=True, capture_output=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', type=str)
    parser.add_argument('--mesh_base_path', type=str, default="/home/gitaar9/AI/TNO/pixel-nerf/datasets/02958343/")
    parser.add_argument('--amount_of_train_images', type=int, default=30)
    parser.add_argument('--bad_models_path', type=str, default='bad_car_models_final.npy')

    opt = parser.parse_args()

    main(opt.output_dir, opt.mesh_base_path, opt.amount_of_train_images, opt.bad_models_path)
