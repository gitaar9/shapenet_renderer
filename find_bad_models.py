import glob
import os
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def handle_user_input():
    k = chr(cv2.waitKey(100000))  # Wait for keyboard input
    bad_car_idxs = []
    stop = False
    while k != '+':
        if k in '0123456789':
            bad_car_idxs.append(int(k))
        if k == '-':
            stop = True
        print(f"Bad cars {bad_car_idxs}")
        k = chr(cv2.waitKey(100000))  # Wait for keyboard input
    return bad_car_idxs, stop


object_name = 'ship'
root_dir = './ship_renders_train_upper_hemisphere_30_fov'

image_paths = glob.glob(os.path.join(root_dir, '*', 'rgb', '000000.png'))
print(image_paths[0])
print(len(image_paths))

bad_models = list(np.load(f'bad_{object_name}_models.npy'))
seen_cars = list(np.load(f'seen_{object_name}s.npy'))

try:
    cv2.namedWindow("Bad model finder")
    total_iterations = len(list(grouper(image_paths, 10)))
    for iter, image_path_group in enumerate(grouper(image_paths, 10)):
        print(f"{iter}/{total_iterations} ({len(bad_models)}/{len(seen_cars)} bad models)")
        images = []
        for idx, image_path in enumerate(image_path_group):
            if image_path not in seen_cars:
                image = cv2.imread(image_path)  # Load the image
                pil_img = Image.fromarray(image)
                draw = ImageDraw.Draw(pil_img)
                draw.text((60, 0), str(idx), (0, 0, 0))
                images.append(np.array(pil_img))
        if len(images) == 0:
            continue
        image = np.hstack(images)
        cv2.imshow("Bad model finder", image.astype(np.uint8))  # Show the image

        bad_car_idxs, stop = handle_user_input()
        for car_idx in bad_car_idxs:
            bad_models.append(image_path_group[car_idx])
        seen_cars.extend(image_path_group)
        if stop:
            break
except ValueError:
    print('Time ran out closing the program')
except:
    print('Unkown error, saving to backup files')
    np.save(f'seen_{object_name}s_temp.npy', np.asarray(seen_cars))
    np.save(f'bad_{object_name}_models_temp.npy', np.asarray(bad_models))
    print(bad_models)
    exit()

# Save the dataframes in the end as well
np.save(f'seen_{object_name}s.npy', np.asarray(seen_cars))
np.save(f'bad_{object_name}_models.npy', np.asarray(bad_models))

cv2.destroyAllWindows()
