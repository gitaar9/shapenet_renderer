import numpy as np
import shutil


def remove_ids_from_folder(folder_root, ids):
    for bad_car_id in ids:
        path = folder_root.format(bad_car_id)
        print(f"Removing: {path}")
        shutil.rmtree(path, ignore_errors=True)


def main():
    bad_car_ids = [
        '65577c66f22fd84d6eb9a4c3b55eb0c4', '429dea3aadb0c3bdc753f4f2b4288d6', 'e2446b9f4b9fb179f525bb02d30fbbfe',
        '2ba37ef44fa116f8300ca77569ad3884', '3a68e8dc897fba988332d0d58794c3c4', 'f90a485c72b6047b102edba1bfa321c4',
        '61df71a58a9d0161202de8d12c6f7633', '2e447f96f152a33a7428866500a95dd8', '372ff5cab89350d23217bd20648fc12d',
        '5bcfb42ffc3490c4af802a9d0ab09410'
    ]

    # # For a single folder
    # root_folder = '/samsung_hdd/Files/AI/TNO/shapenet_renderer/car_renders_train_upper_hemisphere_30_fov/{}'
    # remove_ids_from_folder(folder_root=root_folder, ids=bad_car_ids)
    # For test/train/val split
    root_folder = '/scratch/s2576597/graf_datasets/ship_renders_train_upper_hemisphere_30_fov/{}'
    root_folder = '/samsung_hdd/Files/AI/TNO/pixel-nerf/datasets/04530566/{}'

    remove_ids_from_folder(folder_root=root_folder, ids=bad_car_ids)

main()
